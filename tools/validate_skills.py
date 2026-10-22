#!/usr/bin/env python3
"""Validate the repository's intentionally restricted Agent Skills subset.

Only single-line name and description frontmatter fields are accepted.
Requires Python's standard library; does not load or execute skill content.
"""

from __future__ import annotations

import re
from pathlib import Path, PurePosixPath

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / ".agents" / "skills"
NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIELD_RE = re.compile(r"([a-z][a-z-]*):[ \t]+(.+)\Z")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
ALLOWED_SUFFIXES = {".md", ".txt", ".json", ".yaml", ".yml", ".png", ".svg", ".webp"}
ALLOWED_FIELDS = {"name", "description"}


def validate_skill(skill_dir: Path) -> list[str]:
    """Return problems found in a single, local skill directory."""
    errors: list[str] = []
    if skill_dir.is_symlink():
        return [f"{skill_dir}: symlink skill directories are forbidden"]

    skill_file = skill_dir / "SKILL.md"
    if skill_file.is_symlink() or not skill_file.is_file():
        return [f"{skill_dir}: missing regular SKILL.md"]

    lines = skill_file.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return [f"{skill_file}: missing opening YAML frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return [f"{skill_file}: missing closing YAML frontmatter delimiter"]

    fields: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        match = FIELD_RE.fullmatch(line)
        if not match:
            errors.append(f"{skill_file}:{number}: expected single-line key: value")
            continue
        key, value = match.groups()
        if key in fields:
            errors.append(f"{skill_file}:{number}: duplicate frontmatter field {key}")
        if key not in ALLOWED_FIELDS:
            errors.append(f"{skill_file}:{number}: unsupported frontmatter field {key}")
        fields[key] = value.strip().strip("\"'")

    name = fields.get("name", "")
    description = fields.get("description", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append(f"{skill_file}: invalid skill name")
    if name != skill_dir.name:
        errors.append(f"{skill_file}: name must match parent directory")
    if not 1 <= len(description) <= 1024:
        errors.append(f"{skill_file}: description must be 1-1024 characters")
    if not any(line.strip() for line in lines[end + 1 :]):
        errors.append(f"{skill_file}: missing Markdown instructions")

    body = "\n".join(lines[end + 1 :])
    for match in LINK_RE.finditer(body):
        target = match.group(1).strip().split("#", 1)[0]
        if not target:
            continue
        if "://" in target or ":" in target.split("/", 1)[0]:
            errors.append(f"{skill_file}: external or scheme-based link prohibited: {target}")
            continue
        relative = PurePosixPath(target)
        if relative.is_absolute() or ".." in relative.parts:
            errors.append(f"{skill_file}: escaping link prohibited: {target}")
            continue
        referenced = skill_dir.joinpath(*relative.parts)
        if not referenced.is_file() or referenced.is_symlink():
            errors.append(f"{skill_file}: missing local reference: {target}")

    for path in skill_dir.rglob("*"):
        if path.is_symlink():
            errors.append(f"{path}: symlink prohibited")
        elif path.is_dir() and path.name == "scripts":
            errors.append(f"{path}: executable scripts directory prohibited")
        elif path.is_file():
            if path.suffix.lower() not in ALLOWED_SUFFIXES:
                errors.append(f"{path}: unsupported asset extension")
            if path.stat().st_mode & 0o111:
                errors.append(f"{path}: executable permission prohibited")

    return errors


def validate_repository(root: Path = SKILLS_ROOT) -> list[str]:
    """Validate each immediate child skill directory."""
    if not root.is_dir():
        return [f"{root}: skills directory does not exist"]
    entries = sorted(root.iterdir())
    if not entries:
        return [f"{root}: no skills found"]

    errors: list[str] = []
    for entry in entries:
        if entry.is_dir() or entry.is_symlink():
            errors.extend(validate_skill(entry))
        else:
            errors.append(f"{entry}: only skill directories are allowed")
    return errors


def main() -> int:
    errors = validate_repository()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Skills structure: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
