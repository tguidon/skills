#!/usr/bin/env python3
"""Merge registered skill guidance into a project's AGENTS.md."""

from __future__ import annotations

import argparse
import difflib
import os
import re
import stat
import sys
import tempfile
from pathlib import Path


START_MARKER = "<!-- codex-skills:managed:start -->"
END_MARKER = "<!-- codex-skills:managed:end -->"
SKILL_MARKER = re.compile(r"<!-- codex-skill:([a-z0-9-]+) -->")


class GuidanceError(Exception):
    """Report a safe, user-actionable synchronization error."""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Safely merge registered skill guidance into AGENTS.md."
    )
    parser.add_argument("--project", type=Path, help="Target project directory.")
    parser.add_argument(
        "--agents-file",
        default="AGENTS.md",
        help="Target path relative to the project. Default: AGENTS.md",
    )
    parser.add_argument(
        "--skills-repo",
        type=Path,
        help="Skills repository. Default: the repository that contains this script.",
    )
    parser.add_argument(
        "--skill",
        action="append",
        dest="skills",
        help="Registered skill to include. Repeat for multiple skills. Default: all.",
    )
    parser.add_argument("--list", action="store_true", help="List registered guidance.")
    parser.add_argument("--dry-run", action="store_true", help="Print a diff only.")
    parser.add_argument(
        "--check", action="store_true", help="Return 1 when the target needs an update."
    )
    parser.add_argument(
        "--allow-remove",
        action="store_true",
        help="Allow removal of guidance that exists in the managed block.",
    )
    return parser.parse_args()


def default_skills_repo() -> Path:
    return Path(__file__).resolve().parents[2]


def discover_guidance(skills_repo: Path) -> dict[str, Path]:
    if not skills_repo.is_dir():
        raise GuidanceError(f"Skills repository does not exist: {skills_repo}")

    guidance: dict[str, Path] = {}
    for skill_dir in sorted(skills_repo.iterdir(), key=lambda path: path.name):
        if not skill_dir.is_dir() or not (skill_dir / "SKILL.md").is_file():
            continue
        fragment = skill_dir / "agents" / "project-guidance.md"
        if fragment.is_file() and fragment.read_text(encoding="utf-8").strip():
            guidance[skill_dir.name] = fragment
    return guidance


def select_guidance(
    available: dict[str, Path], requested: list[str] | None
) -> list[tuple[str, str]]:
    if not available:
        raise GuidanceError("No skills register project guidance.")

    names = list(available) if requested is None else list(dict.fromkeys(requested))
    unknown = sorted(set(names) - set(available))
    if unknown:
        joined = ", ".join(unknown)
        raise GuidanceError(f"These skills do not register project guidance: {joined}")

    selected: list[tuple[str, str]] = []
    for name in names:
        text = available[name].read_text(encoding="utf-8").strip()
        if START_MARKER in text or END_MARKER in text or SKILL_MARKER.search(text):
            raise GuidanceError(f"Reserved marker found in guidance for {name}.")
        selected.append((name, text))
    return selected


def make_block(selected: list[tuple[str, str]], newline: str) -> str:
    parts = [START_MARKER]
    for name, fragment in selected:
        normalized = fragment.replace("\r\n", "\n").replace("\r", "\n")
        normalized = normalized.replace("\n", newline)
        parts.extend((f"<!-- codex-skill:{name} -->", normalized))
    parts.append(END_MARKER)
    return (newline + newline).join(parts)


def find_managed_block(original: str) -> tuple[int, int] | None:
    start_count = original.count(START_MARKER)
    end_count = original.count(END_MARKER)
    if start_count == 0 and end_count == 0:
        return None
    if start_count != 1 or end_count != 1:
        raise GuidanceError("Managed markers are missing or duplicated.")

    start = original.index(START_MARKER)
    end_start = original.index(END_MARKER)
    if end_start < start:
        raise GuidanceError("Managed markers are in the wrong order.")
    end = end_start + len(END_MARKER)
    return start, end


def merge_content(
    original: str, selected: list[tuple[str, str]], allow_remove: bool
) -> str:
    newline = "\r\n" if "\r\n" in original else "\n"
    block = make_block(selected, newline)
    bounds = find_managed_block(original)

    if bounds is None:
        if not original:
            return block + newline
        separator = newline if original.endswith(("\n", "\r")) else newline + newline
        return original + separator + block + newline

    start, end = bounds
    current_block = original[start:end]
    current_names = set(SKILL_MARKER.findall(current_block))
    selected_names = {name for name, _ in selected}
    removed = sorted(current_names - selected_names)
    if removed and not allow_remove:
        joined = ", ".join(removed)
        raise GuidanceError(
            f"The update removes managed guidance for: {joined}. "
            "Re-run with --allow-remove after explicit approval."
        )
    return original[:start] + block + original[end:]


def resolve_target(project: Path, agents_file: str) -> tuple[Path, Path]:
    project = project.resolve()
    if not project.is_dir():
        raise GuidanceError(f"Project directory does not exist: {project}")

    requested = Path(agents_file)
    target = requested if requested.is_absolute() else project / requested
    resolved_parent = target.parent.resolve()
    resolved = resolved_parent / target.name
    try:
        resolved.relative_to(project)
    except ValueError as error:
        raise GuidanceError("The target AGENTS file must stay inside the project.") from error

    if target.is_symlink():
        raise GuidanceError(f"Refusing to modify a symlink: {target}")

    override = resolved.parent / "AGENTS.override.md"
    if resolved.name == "AGENTS.md" and override.is_file():
        raise GuidanceError(
            f"{override} takes precedence over {resolved}. "
            "Select the intended file explicitly."
        )
    return project, resolved


def write_atomic(target: Path, content: str) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    prior_mode = stat.S_IMODE(target.stat().st_mode) if target.exists() else 0o644
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.", dir=target.parent, text=True
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        os.chmod(temporary, prior_mode)
        os.replace(temporary, target)
    finally:
        if temporary.exists():
            temporary.unlink()


def read_text_exact(target: Path) -> str:
    with target.open("r", encoding="utf-8", newline="") as handle:
        return handle.read()


def print_diff(target: Path, original: str, updated: str) -> None:
    before = original.splitlines(keepends=True)
    after = updated.splitlines(keepends=True)
    diff = difflib.unified_diff(
        before,
        after,
        fromfile=str(target),
        tofile=str(target),
    )
    sys.stdout.writelines(diff)


def main() -> int:
    args = parse_args()
    try:
        skills_repo = (args.skills_repo or default_skills_repo()).resolve()
        available = discover_guidance(skills_repo)

        if args.list:
            for name in available:
                print(name)
            return 0

        if args.project is None:
            raise GuidanceError("--project is required unless --list is used.")

        _, target = resolve_target(args.project, args.agents_file)
        selected = select_guidance(available, args.skills)
        original = read_text_exact(target) if target.exists() else ""
        updated = merge_content(original, selected, args.allow_remove)

        if args.dry_run:
            print_diff(target, original, updated)
            return 0
        if args.check:
            if original == updated:
                print(f"Up to date: {target}")
                return 0
            print(f"Update required: {target}")
            return 1
        if original == updated:
            print(f"No change: {target}")
            return 0

        write_atomic(target, updated)
        print(f"Updated: {target}")
        print("Skills: " + ", ".join(name for name, _ in selected))
        return 0
    except (GuidanceError, OSError, UnicodeError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
