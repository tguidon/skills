# My Skills

Personal Codex skills that stay versioned here and install only in selected projects.

## iOS design-direction system

### `apply-ios-design-direction`

Applies and reviews a reusable iOS 26+ design playbook. It covers HIG, Liquid Glass, hierarchy, color, motion, accessibility, adaptive layouts, system surfaces, and custom components.

Use it when an agent designs, implements, refactors, or reviews a native interface.

### `create-ios-product-theme`

Runs a short product interview and creates `PRODUCT-THEME.md`. The theme adds product character without replacing the shared playbook.

Each prompt offers two or three choices. The recommended choice appears first. The interface also accepts a custom answer.

Use it when a new app needs direction or an existing theme needs a deliberate revision.

### `capture-ios-product-theme`

Infers the core design language of an existing app from code, assets, reusable components, and rendered behavior.

It also detects bounded feature, content, and context themes. It writes the durable result into `PRODUCT-THEME.md` for the shared playbook.

Use it before substantial design work when an implemented app lacks reliable product-theme guidance.

## Project setup

### `sync-project-skill-guidance`

Adds relevant skill rules to a project `AGENTS.md`. It preserves existing guidance and owns only a marked section.

Each skill can register concise project guidance in `agents/project-guidance.md`. The sync skill discovers these files automatically.

Use it when a project needs persistent skill rules or when registered guidance changes.

## Install in a project

Run these commands from the target project root.

First, list the available skills:

```sh
npx skills add tguidon/skills --list
```

Then install the complete iOS design-direction system:

```sh
npx skills add tguidon/skills \
  --agent codex \
  --skill apply-ios-design-direction \
  --skill create-ios-product-theme \
  --skill capture-ios-product-theme \
  --skill sync-project-skill-guidance \
  --copy \
  --yes
```

Project scope is the default. The command installs the skills in `.agents/skills/`.

Do not add `--global`. Commit `.agents/skills/` and `skills-lock.json` when a project team must use the same versions.

Update the installed project copies after this repository changes:

```sh
npx skills update --project
```

For local skill development, replace `tguidon/skills` with `/Users/taylorguidon/Developer/skills`. Omit `--copy` and select the symlink method.

## Add project guidance

Invoke `$sync-project-skill-guidance` from a project. The skill previews its change before it updates the applicable `AGENTS.md`.

The managed section looks like this:

```md
<!-- codex-skills:managed:start -->

## iOS design direction

- Use `$apply-ios-design-direction` for iPhone and iPad interface work.

<!-- codex-skills:managed:end -->
```

Text outside these markers stays unchanged. A repeated sync updates the same section instead of adding a duplicate.

Skill discovery does not require an `AGENTS.md` entry. Codex can select installed skills from their frontmatter descriptions.

Use project guidance for persistent rules, coordination between skills, and project-specific expectations.

## Add another skill

Follow the root `AGENTS.md` when you add or revise a skill.

If a skill needs persistent project rules, add `agents/project-guidance.md` to that skill. The sync skill then discovers it automatically.

## Development

Validate changed skills before you commit:

```sh
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/apply-ios-design-direction
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/create-ios-product-theme
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/capture-ios-product-theme
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/sync-project-skill-guidance
```
