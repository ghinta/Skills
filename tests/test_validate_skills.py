"""Unit tests for the no-dependency skill validator."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.validate_skills import validate_repository, validate_skill


class ValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name) / "skills"
        self.root.mkdir()
        self.skill = self.root / "architecture-review"
        self.skill.mkdir()

    def write_skill(self, *, name: str = "architecture-review", body: str = "# Review") -> None:
        content = (
            "---\n"
            f"name: {name}\n"
            "description: Review existing architectures when asked for an assessment.\n"
            "---\n\n"
            f"{body}\n"
        )
        (self.skill / "SKILL.md").write_text(content, encoding="utf-8")

    def test_valid_skill(self) -> None:
        self.write_skill(body="# Review\nSee [checklist](references/checklist.md).")
        references = self.skill / "references"
        references.mkdir()
        (references / "checklist.md").write_text("# Checklist\n", encoding="utf-8")
        self.assertEqual(validate_repository(self.root), [])

    def test_missing_frontmatter(self) -> None:
        (self.skill / "SKILL.md").write_text("# Review\n", encoding="utf-8")
        self.assertTrue(any("frontmatter" in x for x in validate_skill(self.skill)))

    def test_name_must_match_directory(self) -> None:
        self.write_skill(name="different-skill")
        self.assertTrue(any("match parent" in x for x in validate_skill(self.skill)))

    def test_missing_local_reference(self) -> None:
        self.write_skill(body="# Review\nSee [missing](references/missing.md).")
        self.assertTrue(any("missing local reference" in x for x in validate_skill(self.skill)))

    def test_parent_directory_escape(self) -> None:
        self.write_skill(body="# Review\nSee [unsafe](../other.md).")
        self.assertTrue(any("escaping link" in x for x in validate_skill(self.skill)))

    def test_external_reference_is_rejected(self) -> None:
        self.write_skill(body="# Review\nSee [remote](https://example.com/SKILL.md).")
        self.assertTrue(any("external or scheme-based link" in x for x in validate_skill(self.skill)))

    def test_script_directory_is_rejected(self) -> None:
        self.write_skill()
        scripts = self.skill / "scripts"
        scripts.mkdir()
        (scripts / "review.sh").write_text("echo review\n", encoding="utf-8")
        self.assertTrue(any("scripts directory prohibited" in x for x in validate_skill(self.skill)))

    def test_unsupported_frontmatter_field(self) -> None:
        self.write_skill()
        file = self.skill / "SKILL.md"
        file.write_text(file.read_text(encoding="utf-8").replace("---\n\n", "allowed-tools: Bash\n---\n\n"), encoding="utf-8")
        self.assertTrue(any("unsupported frontmatter field" in x for x in validate_skill(self.skill)))


if __name__ == "__main__":
    unittest.main()
