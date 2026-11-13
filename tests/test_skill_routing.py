"""Offline tests for the Skills/Rules metadata drift checker."""

from __future__ import annotations

from pathlib import Path
import tempfile
import unittest

from tools.check_skill_routing import check_routing


class RoutingTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        self.skills = root / "Skills"
        self.rules = root / "Rules"
        (self.skills / ".agents" / "skills").mkdir(parents=True)
        self.rules.mkdir()
        for name in ("alpha", "beta"):
            (self.skills / ".agents" / "skills" / name).mkdir()
            (self.skills / ".agents" / "skills" / name / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Test\n---\n\n# Test\n",
                encoding="utf-8",
            )
        self.set_catalog(("alpha", "beta"))
        self.set_routes(("alpha", "beta"))
        (self.rules / "00-core.md").write_text("# Core\n", encoding="utf-8")

    def set_catalog(self, names: tuple[str, ...]) -> None:
        rows = [
            "# Skills", "",
            "## Catalog", "",
            "| Skill | Use when | Not for | Mode |",
            "| --- | --- | --- | --- |",
        ]
        rows.extend(
            f"| [{name}](.agents/skills/{name}/SKILL.md) | Test | Other | Read-only |"
            for name in names
        )
        rows.extend(["", "## Layout", "", "Local files only.", ""])
        (self.skills / "README.md").write_text("\n".join(rows), encoding="utf-8")

    def set_routes(self, names: tuple[str, ...]) -> None:
        rows = [
            "# Routing", "",
            "## Which Skill fits the task?", "",
            "| Relevant Rules | Skill | Use when |",
            "| --- | --- | --- |",
        ]
        rows.extend(
            f"| \x60{chr(48)}0-core\x60 | \x60{name}\x60 | Explicit test task |"
            for name in names
        )
        rows.extend(["", "## Security", "", "Not executable.", ""])
        (self.rules / "80-agent-skills.md").write_text(
            "\n".join(rows), encoding="utf-8"
        )

    def problems(self) -> str:
        return "\n".join(check_routing(self.skills, self.rules))

    def test_matching_repositories(self) -> None:
        self.assertEqual(self.problems(), "")

    def test_skill_missing_from_rules(self) -> None:
        self.set_routes(("alpha",))
        self.assertIn("Rules routing: missing Skill entries: beta", self.problems())

    def test_stale_rules_reference(self) -> None:
        self.set_routes(("alpha", "beta", "removed"))
        self.assertIn("Rules routing: unknown Skill entries: removed", self.problems())

    def test_skill_missing_from_catalog(self) -> None:
        self.set_catalog(("alpha",))
        self.assertIn("Skills README: missing Skill entries: beta", self.problems())

    def test_wrong_catalog_link(self) -> None:
        path = self.skills / "README.md"
        content = path.read_text(encoding="utf-8")
        path.write_text(
            content.replace(
                "[alpha](.agents/skills/alpha/SKILL.md)",
                "[alpha](.agents/skills/beta/SKILL.md)",
            ),
            encoding="utf-8",
        )
        self.assertIn("Skills README: label alpha links to beta", self.problems())

    def test_duplicate_routing_entry(self) -> None:
        self.set_routes(("alpha", "alpha", "beta"))
        self.assertIn("Rules routing: duplicate entry for alpha", self.problems())

    def test_duplicate_catalog_entry(self) -> None:
        self.set_catalog(("alpha", "alpha", "beta"))
        self.assertIn("Skills README: duplicate entry for alpha", self.problems())

    def test_unknown_rule_file(self) -> None:
        path = self.rules / "80-agent-skills.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "\x6000-core\x60 | \x60alpha\x60",
                "\x6099-unknown\x60 | \x60alpha\x60",
            ),
            encoding="utf-8",
        )
        self.assertIn("Rules routing: missing rule file 99-unknown.md", self.problems())

    def test_frontmatter_mismatch(self) -> None:
        path = self.skills / ".agents" / "skills" / "beta" / "SKILL.md"
        path.write_text(
            "---\nname: other\ndescription: Test\n---\n\n# Test\n",
            encoding="utf-8",
        )
        self.assertIn("beta: frontmatter name does not match directory", self.problems())

    def test_rules_not_found(self) -> None:
        (self.rules / "80-agent-skills.md").unlink()
        self.assertIn("80-agent-skills.md", self.problems())

    def test_malformed_routing_row(self) -> None:
        path = self.rules / "80-agent-skills.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "| \x6000-core\x60 | \x60beta\x60 | Explicit test task |",
                "| \x6000-core\x60 | malformed | Explicit test task |",
            ),
            encoding="utf-8",
        )
        self.assertIn("Rules routing: malformed row:", self.problems())


if __name__ == "__main__":
    unittest.main()
