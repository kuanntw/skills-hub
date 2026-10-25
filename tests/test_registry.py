import copy
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from build_index import build, load_entries, render_indexes
from route_candidates import candidates, path_matches, trigger_matches


class RegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = load_entries()

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for directory in ("registry", "schemas", "skills"):
            shutil.copytree(ROOT / directory, self.root / directory)

    def change(self, mutate, name="docx-template"):
        path = self.root / f"registry/{name}.json"
        entry = json.loads(path.read_text())
        mutate(entry)
        path.write_text(json.dumps(entry))

    def test_preserves_all_ten_entries_and_types(self):
        self.assertEqual(len(self.entries), 10)
        types = {e["id"]: e["type"] for e in self.entries}
        self.assertEqual(types["skills-spec"], "reference")
        self.assertEqual(types["vibe-coding-skills"], "framework")

    def test_generated_outputs_match_registry(self):
        self.assertEqual(build(check=True), 10)
        full = json.loads(render_indexes(self.entries)["skills.index.json"])
        self.assertEqual(full["skills"], self.entries)
        self.assertEqual(full["schema_version"], "0.1.0")

    def test_generation_is_deterministic(self):
        build(self.root)
        before = {p.name: p.read_bytes() for p in self.root.glob("skills.*")}
        build(self.root)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.glob("skills.*")})
        self.assertEqual(build(self.root, check=True), 10)

    def test_check_is_readonly_and_detects_drift(self):
        build(self.root)
        path = self.root / "skills.index.md"
        path.write_text("stale index\n")
        with self.assertRaisesRegex(ValueError, "stale"):
            build(self.root, check=True)
        self.assertEqual(path.read_text(), "stale index\n")

    def test_compact_catalog_does_not_duplicate_installation(self):
        outputs = render_indexes(self.entries)
        compact = json.loads(outputs["skills.catalog.json"])
        self.assertLess(len(outputs["skills.catalog.json"]), len(outputs["skills.index.json"]) / 3)
        for entry in compact["skills"]:
            self.assertEqual(set(entry), {"id", "name", "type", "description", "registry"})
            self.assertTrue((ROOT / entry["registry"]).is_file())

    def test_ndf_chinese_triggers_restored(self):
        ndf = next(e for e in self.entries if e["id"] == "taiwan-ndf-investment-review")
        for trigger in ["國發基金", "估值", "投資審查", "投委會", "上市櫃"]:
            with self.subTest(trigger=trigger):
                self.assertIn(trigger, ndf["triggers"])
                self.assertEqual([e["id"] for e in candidates([ndf], f"請協助{trigger}評估")], [ndf["id"]])

    def test_schema_rejects_invalid_entries(self):
        mutations = [
            lambda e: e.pop("avoid_when"),
            lambda e: e.update(description="   "),
            lambda e: e.update(type="executable-framework"),
            lambda e: e.update(triggers=[]),
            lambda e: e.update(triggers=["same", "same"]),
            lambda e: e.update(unknown="not in schema"),
            lambda e: e["source"].update(url="http://example.com/untrusted"),
            lambda e: e["source"].update(entry="../escape/SKILL.md"),
            lambda e: e["source"].update(entry="nested/../../SKILL.md"),
            lambda e: e["source"].update(entry="/etc/passwd"),
            lambda e: e["source"].update(entry="C:\\escape"),
            lambda e: e["source"].update(observed_revision="main"),
            lambda e: e["source"].update(observed_at="2026-02-30"),
            lambda e: e["source"].pop("observed_at"),
        ]
        original = (ROOT / "registry/docx-template.json").read_text()
        for mutation in mutations:
            with self.subTest(mutation=mutation):
                (self.root / "registry/docx-template.json").write_text(original)
                self.change(mutation)
                with self.assertRaises(ValueError):
                    load_entries(self.root)

    def test_id_must_match_filename(self):
        self.change(lambda e: e.update(id="wrong-id"))
        with self.assertRaisesRegex(ValueError, "filename"):
            load_entries(self.root)

    def test_local_source_must_exist(self):
        self.change(lambda e: e["source"].update(entry="missing/SKILL.md"), "taiwan-ndf-investment-review")
        with self.assertRaisesRegex(ValueError, "missing or escapes"):
            load_entries(self.root)

    def test_local_symlink_escape_is_rejected(self):
        outside = self.root.parent / f"{self.root.name}-outside.md"
        outside.write_text("not in repository")
        self.addCleanup(outside.unlink)
        (self.root / "escape.md").symlink_to(outside)
        self.change(lambda e: e["source"].update(entry="escape.md"), "taiwan-ndf-investment-review")
        with self.assertRaisesRegex(ValueError, "escapes"):
            load_entries(self.root)

    def test_routing_positive_and_near_neighbor_cases(self):
        cases = json.loads((ROOT / "tests/routing_cases.json").read_text())
        for case in cases:
            with self.subTest(query=case["query"]):
                found = {e["id"] for e in candidates(self.entries, case["query"])}
                self.assertTrue(set(case["include"]) <= found)
                self.assertFalse(set(case["exclude"]) & found)

    def test_english_boundaries_and_chinese_substrings(self):
        self.assertFalse(trigger_matches("build", "UI"))
        self.assertFalse(trigger_matches("ndforum", "NDF"))
        self.assertTrue(trigger_matches("請協助國發基金評估", "國發基金"))
        self.assertTrue(trigger_matches("Use playwright.", "Playwright"))

    def test_path_and_task_type_evidence(self):
        self.assertTrue(path_matches("report.docx", "**/*.docx"))
        self.assertTrue(path_matches("docs/report.docx", "**/*.docx"))
        self.assertTrue(path_matches("app/User.php", "app/**/*.php"))
        self.assertTrue(path_matches("app/Models/User.php", "app/**/*.php"))
        self.assertFalse(path_matches("routes/nested/api.php", "routes/*.php"))
        found = {e["id"]: e for e in candidates(self.entries, "", ["report.docx"], ["i18n"])}
        self.assertEqual(found["docx-template"]["evidence"]["files"], ["report.docx"])
        self.assertEqual(found["laravel-vibe"]["evidence"]["task_types"], ["i18n"])

    def test_candidates_preserve_avoid_gate_and_never_run_commands(self):
        entries = copy.deepcopy(self.entries)
        marker = self.root / "must-not-exist"
        for entry in entries:
            entry["installation"]["command"] = f"touch {marker}"
        results = candidates(entries, "Laravel UI screenshot vibe coding")
        self.assertGreater(len(results), 0)
        self.assertFalse(marker.exists())
        for result in results:
            self.assertEqual(result["status"], "candidate_requires_context_review")
            self.assertTrue(result["avoid_when"])
            self.assertNotIn("installation", result)


if __name__ == "__main__":
    unittest.main()
