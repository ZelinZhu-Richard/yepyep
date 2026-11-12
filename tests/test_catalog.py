import copy
from datetime import datetime, timedelta, timezone
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/breadth-first"
sys.path.insert(0, str(SKILL / "scripts"))
from catalog import guard_changes, normalize, rank, validate_catalog
from refresh_models import refresh

NOW = datetime(2026, 11, 12, 12, tzinfo=timezone.utc)


def feed():
    return {
        "cheap": {"mode": "chat", "litellm_provider": "openai",
                  "input_cost_per_token": 1e-7, "output_cost_per_token": 4e-7,
                  "cache_read_input_token_cost": 5e-8,
                  "input_cost_per_token_above_200k_tokens": 2e-7},
        "reviewer": {"mode": "chat", "litellm_provider": "anthropic",
                     "input_cost_per_token": 3e-6, "output_cost_per_token": 15e-6},
        "unrelated": {"mode": "embedding", "litellm_provider": "openai",
                      "input_cost_per_token": 1e-9},
        "router": {"mode": "chat", "litellm_provider": "openrouter",
                   "input_cost_per_token": 1e-10, "output_cost_per_token": 1e-10},
    }


def encoded(value):
    return json.dumps(value).encode()


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.catalog = normalize(encoded(feed()), NOW)

    def test_extracts_only_direct_chat_models_and_converts_units(self):
        self.assertEqual([r["id"] for r in self.catalog["models"]], ["cheap", "reviewer"])
        row = self.catalog["models"][0]
        self.assertEqual(row["input_usd_per_million"], 0.1)
        self.assertEqual(row["output_usd_per_million"], 0.4)
        self.assertEqual(row["other_reported_cost_fields"]["cache_read_input_token_cost"], 5e-8)
        self.assertEqual(row["other_reported_cost_fields"]["input_cost_per_token_above_200k_tokens"], 2e-7)

    def test_ranks_only_requested_ids_with_correct_cost(self):
        result = rank(self.catalog, ["reviewer", "cheap", "cheap"], 4000, 1000, NOW)
        self.assertEqual([r["id"] for r in result["ranked"]], ["cheap", "reviewer"])
        self.assertAlmostEqual(result["ranked"][0]["estimated_standard_token_cost_usd"], 0.0008)
        self.assertEqual(len(rank(self.catalog, ["reviewer"], 10, 10, NOW)["ranked"]), 1)

    def test_unknown_models_are_not_free_or_fuzzy_matched(self):
        result = rank(self.catalog, ["cheap-new", "gpt-6-luna"], 10, 10, NOW)
        self.assertEqual(result["status"], "no_matching_prices")
        self.assertEqual(result["ranked"], [])
        self.assertEqual(result["unpriced_ids"], ["cheap-new", "gpt-6-luna"])

    def test_partial_unknowns_remain_visible(self):
        result = rank(self.catalog, ["cheap", "unpriced"], 10, 10, NOW)
        self.assertEqual(result["unpriced_ids"], ["unpriced"])

    def test_rejects_stale_and_future_timestamps(self):
        for offset in (timedelta(days=7, seconds=1), timedelta(minutes=-6)):
            with self.subTest(offset=offset), self.assertRaises(ValueError):
                rank(self.catalog, ["cheap"], 10, 10, NOW + offset)
        rank(self.catalog, ["cheap"], 10, 10, NOW + timedelta(days=7))

    def test_rejects_missing_timezone_and_invalid_dates(self):
        for value in (None, "2026-11-12T12:00:00", "yesterday"):
            data = copy.deepcopy(self.catalog)
            data["fetched_at"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_catalog(data)

    def test_rejects_negative_nan_infinite_boolean_and_string_prices(self):
        for value in (-1, float("nan"), float("inf"), True, False, "0.1"):
            data = feed()
            data["cheap"]["input_cost_per_token"] = value
            with self.subTest(value=value), self.assertRaises(ValueError):
                normalize(encoded(data), NOW)

    def test_missing_or_zero_prices_are_excluded(self):
        data = feed()
        data["unknown"] = {**data["cheap"], "input_cost_per_token": None}
        data["promotion"] = {**data["cheap"], "output_cost_per_token": 0}
        result = normalize(encoded(data), NOW)
        self.assertEqual(result["skipped_unpriced_or_zero_price_entries"], 2)
        self.assertEqual(len(result["models"]), 2)

    def test_rejects_bad_feed_shape_and_missing_provider(self):
        for value in ([], {}, {"cheap": feed()["cheap"]}):
            with self.subTest(value=value), self.assertRaises(ValueError):
                normalize(encoded(value), NOW)

    def test_rejects_duplicate_ids_and_bad_source(self):
        duplicate = copy.deepcopy(self.catalog)
        duplicate["models"].append(duplicate["models"][0])
        bad_source = copy.deepcopy(self.catalog)
        bad_source["source"]["url"] = "https://example.com/prices"
        for value in (duplicate, bad_source):
            with self.assertRaises(ValueError):
                validate_catalog(value)

    def test_token_budgets_must_be_valid(self):
        for inputs, outputs in ((-1, 10), (0, 0), (1.2, 10), (True, 10)):
            with self.subTest(inputs=inputs), self.assertRaises(ValueError):
                rank(self.catalog, ["cheap"], inputs, outputs, NOW)

    def test_large_removal_is_blocked(self):
        expanded = feed()
        expanded["another"] = dict(expanded["cheap"])
        with self.assertRaisesRegex(ValueError, "disappeared"):
            guard_changes(normalize(encoded(expanded), NOW), self.catalog)

    def test_large_price_change_is_blocked(self):
        changed = copy.deepcopy(self.catalog)
        changed["models"][0]["input_usd_per_million"] *= 11
        with self.assertRaisesRegex(ValueError, "tenfold"):
            guard_changes(self.catalog, changed)

    def test_failed_refresh_preserves_existing_bytes(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "models.json"
            original = json.dumps(self.catalog).encode()
            target.write_bytes(original)
            for payload in (b"not json", b"{}", encoded({"only": feed()["cheap"]})):
                with self.assertRaises(ValueError):
                    refresh(target, fetch=lambda: payload)
                self.assertEqual(target.read_bytes(), original)
            self.assertEqual(list(Path(folder).iterdir()), [target])

    def test_network_failure_preserves_existing_bytes(self):
        def fail():
            raise OSError("network unavailable")
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "models.json"
            target.write_text(json.dumps(self.catalog))
            original = target.read_bytes()
            with self.assertRaises(OSError):
                refresh(target, fetch=fail)
            self.assertEqual(target.read_bytes(), original)

    def test_successful_refresh_is_repeatable(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "nested/models.json"
            for _ in range(2):
                refresh(target, fetch=lambda: encoded(feed()))
                validate_catalog(json.loads(target.read_text()))
            self.assertEqual(list(target.parent.iterdir()), [target])

    def test_cli_reports_unknown_models_with_nonzero_status(self):
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / "models.json"
            target.write_text(json.dumps(normalize(encoded(feed()))))
            result = subprocess.run([sys.executable, str(SKILL / "scripts/rank_models.py"),
                                     "--catalog", str(target), "--model", "gpt-6-luna"],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(json.loads(result.stdout)["status"], "no_matching_prices")

    def test_bundled_catalog_is_well_formed(self):
        # Freshness belongs to runtime selection; offline CI remains useful after a missed schedule.
        validate_catalog(json.loads((SKILL / "references/model-catalog.json").read_text()))


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
