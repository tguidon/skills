# My Skills

Personal Codex skills that stay versioned in this repository and load through local symlinks.

## iOS design-direction system

### `apply-ios-design-direction`

Applies and reviews a reusable iOS 26+ design playbook. It covers HIG, Liquid Glass, hierarchy, color, motion, accessibility, adaptive iPhone and iPad layouts, system surfaces, and custom components.

Use it when an agent designs, implements, refactors, or reviews a native interface.

### `create-ios-product-theme`

Runs a short product interview and creates `PRODUCT-THEME.md`. The theme adds product character without replacing the shared playbook.

Each prompt offers two or three choices. The recommended choice appears first, and the interface also accepts a custom answer.

Use it when a new app needs direction or an existing theme needs a deliberate revision.

## Install with symlinks

Run these commands from this repository:

```sh
ln -s "$(pwd)/apply-ios-design-direction" "${CODEX_HOME:-$HOME/.codex}/skills/apply-ios-design-direction"
ln -s "$(pwd)/create-ios-product-theme" "${CODEX_HOME:-$HOME/.codex}/skills/create-ios-product-theme"
```

Codex then reads each skill directly from this repository. A pull or local edit updates the installed skill without another install step.

## Project guidance

Add this short contract to a project's `AGENTS.md` when the project uses the system:

```md
## iOS design direction

- Use `$apply-ios-design-direction` for iPhone and iPad interface work.
- Read `PRODUCT-THEME.md` after the shared playbook when the app has one.
- Use `$create-ios-product-theme` when the product theme is missing or needs revision.
- A product theme can replace a playbook `SHOULD` or select a `MAY`. It cannot override a `MUST`.
```

## Development

Validate a skill before you commit changes:

```sh
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py apply-ios-design-direction
python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py create-ios-product-theme
```
