# Skills repository guidance

## Scope

This repository contains personal Codex skills. Each folder under `skills/` is the versioned source for one skill.

## Create or revise a skill

- Use `$skill-creator` for every new skill and substantial skill revision.
- Run `init_skill.py` for each new skill.
- Keep `SKILL.md` concise and imperative.
- Put trigger conditions in the frontmatter description.
- Add only the scripts, references, and assets that the skill needs.
- Update `agents/openai.yaml` when the skill name, scope, or default prompt changes.
- Update the root `README.md` when a skill is added, removed, renamed, or installed.
- Run `quick_validate.py` for each changed skill.
- Run each changed script with representative inputs.
- Forward-test a skill when its workflow has important choices or file changes.

## Ask questions

If a skill asks questions, use `request_user_input` when the tool is available.

- Ask one to three questions in one call.
- Give each question two or three exclusive choices.
- Put the recommended choice first.
- Add `(Recommended)` to the recommended label.
- Do not add an `Other` choice. The client supplies a custom response.
- If the tool is unavailable, show the same choices in plain text.
- In the plain-text fallback, state that the user can type a custom answer.

## Register project guidance

Add `agents/project-guidance.md` only when a skill needs persistent project rules.

- Give the fragment a clear Markdown heading.
- Keep the fragment concise.
- Refer to skills with their exact `$skill-name`.
- Do not copy the skill workflow into the fragment.
- Do not add managed-block markers. The sync script owns those markers.

`$sync-project-skill-guidance` discovers these fragments without a central registry.

## Protect project instructions

The sync skill owns only this marked block:

```md
<!-- codex-skills:managed:start -->
...
<!-- codex-skills:managed:end -->
```

Preserve all text outside the block. Stop when markers are missing, duplicated, or reversed.
