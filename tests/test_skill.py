import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/breadth-first"


class SkillPackageTests(unittest.TestCase):
    def test_relative_links_resolve(self):
        for doc in [ROOT / "README.md", *SKILL.rglob("*.md")]:
            for target in re.findall(r"\]\(([^)#]+)\)", doc.read_text()):
                if not target.startswith("http"):
                    self.assertTrue((doc.parent / target).exists(), f"{doc.name}: {target}")

    def test_frontmatter_names_the_skill(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\nname: breadth-first\ndescription: "))


RECORD_REQUIRED = {"id", "packet", "claim_or_approach", "category", "source_url",
                   "accessed_at", "inspection", "evidence_type", "uncertainty"}
INSPECTION = {"full_source", "snippet_only", "user_document"}
EVIDENCE_TYPE = {"direct_measurement", "firsthand_report", "secondary_report", "hypothesis"}
SPOT_RESULT = {"pass", "stitched", "fail", "unverifiable"}
SUPPORTS = {"yes", "partial", "no", None}
PACKET_FILE = re.compile(r"^(p\d{2,3}r?|c[12]-\d+|lead)\.jsonl$")
REVIEW_FILE = re.compile(r"^(spotcheck-\d+\.jsonl|consolidation-r[01](-[a-z0-9-]+)?\.md"
                         r"|challenge-r1-\d+\.md|brief-r2-\d+\.md)$")
EVIDENCE_ID = re.compile(r"\b(?:p\d{2,3}r?|c[12]-\d+|lead)-e\d{3}\b")


class ExampleRunTests(unittest.TestCase):
    """Examples must follow the current templates, so drift fails loudly."""

    def runs(self):
        found = [d for d in (ROOT / "examples").iterdir() if d.is_dir()]
        self.assertTrue(found, "no example runs")
        return found

    def test_records_match_schema_and_file_names(self):
        for run in self.runs():
            ids = set()
            for path in sorted((run / "packets").iterdir()):
                self.assertRegex(path.name, PACKET_FILE)
                prefix = path.stem
                for n, line in enumerate(path.read_text().splitlines(), 1):
                    if not line.strip():
                        continue
                    rec = json.loads(line)
                    where = f"{path.name}:{n}"
                    self.assertTrue(RECORD_REQUIRED <= rec.keys(), where)
                    self.assertTrue(rec["id"].startswith(prefix + "-e"), where)
                    self.assertNotIn(rec["id"], ids, where)
                    ids.add(rec["id"])
                    self.assertIn(rec["inspection"], INSPECTION, where)
                    self.assertIn(rec["evidence_type"], EVIDENCE_TYPE, where)
                    if rec["inspection"] == "full_source":
                        self.assertTrue(rec.get("support_quote"), where)

    def test_review_files_and_spotcheck_values(self):
        for run in self.runs():
            for path in sorted((run / "review").iterdir()):
                self.assertRegex(path.name, REVIEW_FILE)
                if path.suffix == ".jsonl":
                    for line in path.read_text().splitlines():
                        if line.strip():
                            row = json.loads(line)
                            self.assertIn(row["result"], SPOT_RESULT, path.name)
                            self.assertIn(row["supports_claim"], SUPPORTS, path.name)

    def test_answer_cites_only_existing_records(self):
        for run in self.runs():
            ids = set()
            for path in (run / "packets").glob("*.jsonl"):
                ids |= {json.loads(l)["id"] for l in path.read_text().splitlines() if l.strip()}
            cited = set(EVIDENCE_ID.findall((run / "answer.md").read_text()))
            self.assertTrue(cited, "answer cites no evidence IDs")
            self.assertEqual(cited - ids, set(), f"{run.name}: cited IDs with no record")
            # Reviewer shorthand like "C1-2" means a fetched source was never logged.
            self.assertIsNone(re.search(r"\bC[12]-\d+\b", (run / "answer.md").read_text()),
                              f"{run.name}: answer cites an unlogged reviewer source")


class EvalScoringTests(unittest.TestCase):
    def test_scores_distinct_novel_and_duplicates(self):
        spec = importlib.util.spec_from_file_location("score", ROOT / "evals/score.py")
        score = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(score)
        result = score.score({"key_size": 4, "items": [
            {"text": "A", "valid": True, "key": "k1"},
            {"text": "A again", "valid": True, "key": "k1"},
            {"text": "Niche", "valid": True, "key": None},
            {"text": "Wrong", "valid": False, "key": None},
        ]})
        self.assertEqual(result["distinct_valid"], 2)
        self.assertEqual(result["key_matched"], 1)
        self.assertEqual(result["novel_valid"], 1)
        self.assertAlmostEqual(result["duplicate_rate"], 0.25)
        self.assertAlmostEqual(result["key_recall"], 0.25)
        self.assertEqual(result["invalid_listed"], 1)
        self.assertIsNone(score.score({"items": []})["key_recall"])

    def test_codex_policy_disables_implicit_invocation(self):
        text = (SKILL / "agents/openai.yaml").read_text()
        self.assertIn("allow_implicit_invocation: false", text)
        self.assertIn("disable-model-invocation: true", (SKILL / "SKILL.md").read_text())


class InstallationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
        cls.installer = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.installer)

    def test_installation_is_shared_and_repeatable(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            self.installer.install(root, "both")
            self.installer.install(root, "both")
            for host in (".agents", ".claude"):
                self.assertEqual((root / host / "skills/breadth-first").resolve(), SKILL)

    def test_existing_installation_is_preserved_before_any_writes(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            existing = root / ".claude/skills/breadth-first"
            existing.mkdir(parents=True)
            sentinel = existing / "SKILL.md"
            sentinel.write_text("User-owned instructions")
            with self.assertRaises(FileExistsError):
                self.installer.install(root, "both")
            self.assertEqual(sentinel.read_text(), "User-owned instructions")
            self.assertFalse((root / ".agents").exists())

    def test_repository_discovery_links_resolve_to_same_skill(self):
        for host in (".agents", ".claude"):
            self.assertEqual((ROOT / host / "skills/breadth-first").resolve(), SKILL)
            self.assertTrue((ROOT / host / "skills/breadth-first/SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
