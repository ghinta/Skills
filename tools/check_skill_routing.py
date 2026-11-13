#!/usr/bin/env python3
"""Check first-party Skill catalog versus Rules routing without executing either.

Both repositories must already be checked out locally. No downloads,
installation, remote imports or execution of Rules content are performed.
"""

from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
IDENT = r"[a-z0-9]+(?:-[a-z0-9]+)*"
RULE_IDENT = re.compile(r"[0-9]{2}-[a-z0-9]+(?:-[a-z0-9]+)*\Z")
CATALOG_ROW = re.compile(
    rf"^\|\s*\[(?P<label>{IDENT})\]"
    rf"\(\.agents/skills/(?P<path>{IDENT})/SKILL\.md\)"
    r"\s*\|.+\|\s*$"
)
ROUTING_ROW = re.compile(
    rf"^\|\s*\x60(?P<rules>[^\x60]+)\x60\s*\|\s*\x60(?P<skill>{IDENT})\x60"
    r"\s*\|.+\|\s*$"
)
FRONTMATTER_NAME = re.compile(r"^name:\s*(?P<name>[a-z0-9-]+)\s*$", re.M)


def _read_plain(path: Path, errors: list[str]) -> str:
    if path.is_symlink() or not path.is_file():
        errors.append(f"Missing regular text file (symlinks disallowed): {path}")
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read {path}: {exc}")
        return ""


def _rows(document: str, heading: str, label: str, errors: list[str]) -> list[str]:
    section = re.search(
        rf"(?ms)^## {re.escape(heading)}[ \t]*\n(.*?)(?=^## |\Z)",
        document,
    )
    if section is None:
        errors.append(f"{label}: missing section '## {heading}'")
        return []
    rows = [line for line in section.group(1).splitlines() if line.startswith("|")]
    if len(rows) < 3:
        errors.append(f"{label}: expected table header, separator and at least one row")
        return []
    return rows[2:]


def _duplicates(names: list[str], label: str, errors: list[str]) -> None:
    for name, count in sorted(Counter(names).items()):
        if count > 1:
            errors.append(f"{label}: duplicate entry for {name}")


def check_routing(skills_root: Path, rules_root: Path) -> list[str]:
    """Validate names and local references in two reviewed repositories."""
    errors: list[str] = []
    readme = _read_plain(skills_root / "README.md", errors)
    routing = _read_plain(rules_root / "80-agent-skills.md", errors)

    catalog: list[str] = []
    for row in _rows(readme, "Catalog", "Skills README", errors):
        match = CATALOG_ROW.fullmatch(row)
        if match is None:
            errors.append(f"Skills README: malformed catalog row: {row}")
            continue
        name, directory = match.group("label", "path")
        if name != directory:
            errors.append(f"Skills README: label {name} links to {directory}")
        catalog.append(name)
    _duplicates(catalog, "Skills README", errors)

    routes: list[str] = []
    for row in _rows(routing, "Which Skill fits the task?", "Rules routing", errors):
        match = ROUTING_ROW.fullmatch(row)
        if match is None:
            errors.append(f"Rules routing: malformed row: {row}")
            continue
        names, skill = match.group("rules", "skill")
        routes.append(skill)
        for rule in names.split(" / "):
            if not RULE_IDENT.fullmatch(rule):
                errors.append(f"Rules routing: invalid rule identifier {rule!r}")
                continue
            path = rules_root / f"{rule}.md"
            if path.is_symlink() or not path.is_file():
                errors.append(f"Rules routing: missing rule file {rule}.md")
    _duplicates(routes, "Rules routing", errors)

    skills_dir = skills_root / ".agents" / "skills"
    discovered: list[str] = []
    if not skills_dir.is_dir() or skills_dir.is_symlink():
        errors.append(f"Missing regular Skill directory: {skills_dir}")
    else:
        for directory in sorted(skills_dir.iterdir()):
            if directory.is_symlink() or not directory.is_dir():
                errors.append(f"Unexpected non-directory Skill entry: {directory.name}")
                continue
            name = directory.name
            discovered.append(name)
            content = _read_plain(directory / "SKILL.md", errors)
            if not content.startswith("---\n"):
                errors.append(f"{name}: invalid SKILL.md frontmatter")
                continue
            close = content.find("\n---\n", 4)
            if close < 0:
                errors.append(f"{name}: frontmatter missing closing delimiter")
                continue
            match = FRONTMATTER_NAME.search(content[4:close])
            if match is None or match.group("name") != name:
                errors.append(f"{name}: frontmatter name does not match directory")

    for label, names in (("Rules routing", routes), ("Skills README", catalog)):
        missing = sorted(set(discovered) - set(names))
        extra = sorted(set(names) - set(discovered))
        if missing:
            errors.append(f"{label}: missing Skill entries: {', '.join(missing)}")
        if extra:
            errors.append(f"{label}: unknown Skill entries: {', '.join(extra)}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--rules-root", type=Path, required=True,
        help="Locally checked-out Rules repository (passive input data only)",
    )
    parser.add_argument(
        "--skills-root", type=Path, default=ROOT,
        help="Locally checked-out Skills repository (defaults to script repository)",
    )
    args = parser.parse_args()
    problems = check_routing(args.skills_root, args.rules_root)
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}")
        return 1
    print("Skills/Rules routing: OK (catalog, local Skills and rule IDs match)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
