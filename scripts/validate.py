#!/usr/bin/env python3

"""Validate the provider-neutral RoModular agent guidance repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = ROOT / "skills"

REQUIRED_FILES = (
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRACT.md",
    "LICENSE",
    "README.md",
    "VERSION",
    "workspace/AGENTS.md",
    "workspace/CLAUDE.md",
)

REPOSITORY_ADAPTERS = (
    "CPSTL.md",
    "Foundation.md",
    "DspCore.md",
    "MCC.md",
    "MIDILAR.md",
    "RoModular.md",
    "RoModularAgents.md",
    "RoModularBuild.md",
)

SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CENTRAL_REFERENCE = re.compile(r"\.\./\.\./\.\./RoModularAgents/([^\s`)]+)")
UNFINISHED_MARKERS = ("TO" + "DO", "T" + "BD")


def read_text(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as exception:
        errors.append(f"cannot read {path.relative_to(ROOT)}: {exception}")
        return ""


def parse_frontmatter(path: Path, text: str, errors: list[str]) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        errors.append(f"{path.relative_to(ROOT)} must start with YAML front matter")
        return {}

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)} has unterminated YAML front matter")
        return {}

    fields: dict[str, str] = {}
    for line in lines[1:closing_index]:
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator or not key.strip() or not value.strip():
            errors.append(f"{path.relative_to(ROOT)} has invalid front matter: {line}")
            continue
        key = key.strip()
        if key in fields:
            errors.append(f"{path.relative_to(ROOT)} repeats front-matter field {key}")
        fields[key] = value.strip()

    if not any(line.strip() for line in lines[closing_index + 1 :]):
        errors.append(f"{path.relative_to(ROOT)} has no skill instructions")
    return fields


def validate_skill(skill_directory: Path, errors: list[str]) -> None:
    manifest = skill_directory / "SKILL.md"
    if not manifest.is_file():
        errors.append(f"{skill_directory.relative_to(ROOT)} is missing SKILL.md")
        return

    text = read_text(manifest, errors)
    fields = parse_frontmatter(manifest, text, errors)
    name = fields.get("name", "")
    description = fields.get("description", "")

    if name != skill_directory.name:
        errors.append(
            f"{manifest.relative_to(ROOT)} name must match directory {skill_directory.name}"
        )
    if name and not SKILL_NAME.fullmatch(name):
        errors.append(f"{manifest.relative_to(ROOT)} has invalid skill name {name!r}")
    if not description:
        errors.append(f"{manifest.relative_to(ROOT)} requires a description")
    elif len(description) > 1024:
        errors.append(f"{manifest.relative_to(ROOT)} description exceeds 1024 characters")

    for referenced_path in CENTRAL_REFERENCE.findall(text):
        if not (ROOT / referenced_path).exists():
            errors.append(
                f"{manifest.relative_to(ROOT)} references missing {referenced_path}"
            )


def validate_text_files(errors: list[str]) -> None:
    ignored_parts = {".git", "__pycache__"}
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix not in {"", ".md", ".py", ".yml"}:
            continue
        text = read_text(path, errors)
        for line_number, line in enumerate(text.splitlines(), start=1):
            if line.endswith((" ", "\t")):
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number} has trailing whitespace"
                )
            if any(marker in line for marker in UNFINISHED_MARKERS):
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number} contains unfinished guidance"
                )


def main() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).is_file():
            errors.append(f"missing required file: {relative_path}")

    for adapter in REPOSITORY_ADAPTERS:
        if not (ROOT / "repositories" / adapter).is_file():
            errors.append(f"missing repository adapter: repositories/{adapter}")

    skill_directories = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_directories:
        errors.append("skills/ must contain at least one skill directory")
    for skill_directory in skill_directories:
        validate_skill(skill_directory, errors)

    validate_text_files(errors)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(
        "Validated "
        f"{len(REPOSITORY_ADAPTERS)} repository adapters and "
        f"{len(skill_directories)} Agent Skills."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
