---
name: sync-skill-guidance
description: Safely add or refresh installed-skill guidance in a project AGENTS.md without replacing existing instructions. Use when Codex configures a repository for installed skills, updates a managed skills section, or adds persistent skill rules.
---

# Sync Skill Guidance

Add concise skill rules to the active project. Preserve all human-authored instructions outside the managed block.

## Find the target

1. Find the project root.
2. Read each `AGENTS.md` and `AGENTS.override.md` from the root to the current directory.
3. Select the file whose scope matches the requested work.
4. Use the repository root `AGENTS.md` for repository-wide guidance by default.

If an override exists beside the target file, ask which file to update. The override takes precedence in that directory.

## Select guidance

Run this command from the skill directory:

```sh
python scripts/sync_agents_guidance.py --list
```

The script discovers sibling skills that contain `agents/project-guidance.md`.

Infer the relevant guidance from the project and the user request. Ask one question when the choice changes the result.

Use structured multiple-choice questions:

- Use `request_user_input` when it is available.
- Ask one to three questions in one call.
- Give each question two or three exclusive choices.
- Put the recommended choice first and add `(Recommended)` to its label.
- Do not add an `Other` choice. The client supplies a custom response.
- If the tool is unavailable, show the same choices in plain text.
- Tell the user that a custom answer is valid in the plain-text fallback.

Treat the selected names as the complete desired managed set. Do not remove an existing selection without explicit user direction.

## Preview the merge

Run the script with the project path and each selected skill:

```sh
python scripts/sync_agents_guidance.py \
  --project /absolute/path/to/project \
  --skill skill-name \
  --dry-run
```

Add `--agents-file AGENTS.override.md` only when that file is the selected target.

Read the diff. Make sure that only the managed block changes.

Stop if the script reports malformed or duplicate markers. Do not repair ambiguous markers without user direction.

## Apply the merge

Run the same command without `--dry-run`.

The script follows these rules:

- Create the target file when it is absent.
- Append one managed block when markers are absent.
- Replace only the existing managed block when both markers are valid.
- Preserve all content outside the managed block.
- Refuse to follow a target-file symlink.
- Refuse to remove managed skill guidance unless `--allow-remove` is explicit.

## Finish

Read the final file. Report the target path and the selected skills.

State that existing guidance outside the managed block stayed unchanged.
