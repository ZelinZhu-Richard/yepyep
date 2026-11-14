import importlib.util
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
