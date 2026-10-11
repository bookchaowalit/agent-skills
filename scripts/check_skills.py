#!/usr/bin/env python3
"""Validate skill packages: each <name>/SKILL.md has name/description frontmatter."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        return {}
    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        key, sep, value = line.partition(":")
        if sep and not line.startswith(" "):
            fields[key.strip()] = value.strip()
    return fields


def check(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    skills = sorted(p.parent for p in root.glob("*/SKILL.md"))
    if not skills:
        errors.append("no skills found")
    for folder in skills:
        meta = frontmatter((folder / "SKILL.md").read_text(encoding="utf-8"))
        if meta.get("name") != folder.name:
            errors.append(f"{folder.name}: frontmatter name {meta.get('name')!r} does not match folder")
        if not NAME.match(folder.name):
            errors.append(f"{folder.name}: invalid skill name")
        if not meta.get("description"):
            errors.append(f"{folder.name}: missing description")
    return errors


if __name__ == "__main__":
    problems = check()
    for problem in problems:
        print(f"error: {problem}", file=sys.stderr)
    print(f"skills check: {'FAIL' if problems else 'ok'} ({len(problems)} problem(s))")
    raise SystemExit(1 if problems else 0)
