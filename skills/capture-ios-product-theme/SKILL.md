---
name: capture-ios-product-theme
description: Analyze an existing iOS codebase and rendered app to infer its design language, component system, tokens, and scoped themes. Use when an app lacks reliable design documentation and Codex must create or revise PRODUCT-THEME.md from implementation evidence.
---

# Capture an iOS Product Theme

Recover the product language that the app already expresses. Convert implementation evidence into concise direction for future design work.

## Load the foundation

1. Read the shared `DESIGN.md` playbook completely.
2. Find and read any existing `PRODUCT-THEME.md`.
3. Read `references/EVIDENCE-GUIDE.md` completely.
4. Find the `PRODUCT-THEME-TEMPLATE.md` bundled with `$create-ios-product-theme`.
5. Read the product documents, release notes, and repository guidance.

Use the shared playbook for platform rules. Use implementation evidence only for product-specific direction.

Do not modify interface code during capture. Change code only when the user asks for implementation or refactoring.

## Set the capture mode

Use coherent capture by default. Preserve strong recurring choices and remove accidental inconsistency from the documented direction.

Ask which mode to use only when the request does not make the intent clear:

- **Coherent capture:** Preserve the strongest current language and resolve accidental differences.
- **Faithful capture:** Preserve repeated differences and label uncertain theme boundaries.
- **HIG-first modernization:** Preserve product identity while moving optional choices toward the shared playbook.

Use structured multiple-choice questions:

- Use `request_user_input` when it is available.
- Ask one to three questions in one call.
- Give each question two or three exclusive choices.
- Put the recommended choice first and add `(Recommended)` to its label.
- Do not add an `Other` choice. The client supplies a custom response.
- If the tool is unavailable, show the same choices in plain text.
- State that the user can type a custom answer in the plain-text fallback.

Do not interview for facts that the repository or rendered app can answer.

## Inspect the implementation

Start with `rg --files`. Use `rg` to find design definitions and their call sites.

Inspect these evidence groups:

- App structure, navigation, presentation, and adaptive layout.
- Asset catalogs, named colors, images, symbols, icons, and fonts.
- Theme types, tokens, constants, environment values, and appearance configuration.
- Reusable views, modifiers, styles, components, and UIKit appearance code.
- Screen-level color, type, spacing, shape, material, imagery, and motion choices.
- Loading, empty, error, success, disabled, selection, and accessibility states.
- Previews, snapshot tests, onboarding, widgets, notifications, and system surfaces.
- Feature folders that contain a coherent local visual language.

Run the app and inspect representative flows when runtime tools are available. Include light, dark, compact, wide, and accessibility appearances when practical.

Treat runtime behavior as evidence of what ships. Treat code as evidence of how and where the design is defined.

## Build the evidence map

For each candidate design rule, record:

- The observed choice.
- Its semantic job.
- Its scope and recurrence.
- Its source quality.
- Its confidence level.
- Whether it is deliberate, inherited, experimental, legacy, or accidental.

Prefer semantic roles over literal values. Record “warning surface” before a specific orange value.

Do not infer intent from one constant or one screen. Search for definitions, uses, variants, and exceptions.

## Determine the theme topology

Identify one core product theme. This theme governs the shell, hierarchy, interaction character, and shared content language.

Then identify scoped themes only when evidence supports them:

- **Feature theme:** A feature has a repeatable visual language that inherits the core theme.
- **Content theme:** User content or a domain object supplies a bounded visual style, such as a flash-card deck.
- **Context mode:** A temporary state changes emphasis for focus, celebration, urgency, or immersion.

Do not promote a one-off screen treatment into a theme. A scoped theme needs a clear trigger, stable rules, and an inheritance boundary.

For each scoped theme, define:

- Scope and activation trigger.
- Core-theme rules that remain unchanged.
- Roles that the theme can replace.
- Components and content that express it.
- Entry, exit, and transition behavior.
- Accessibility and fallback behavior.

## Reconcile evidence

Use this priority for conflicting evidence:

1. Confirmed owner decisions in an existing `PRODUCT-THEME.md`.
2. Current rendered behavior in important product flows.
3. Central theme definitions and semantic assets.
4. Repeated reusable components and modifiers.
5. Repeated screen-level choices.
6. Isolated constants, experiments, previews, and legacy code.

Do not encode an accessibility failure or an Apple HIG conflict as product character.

If a recurring current choice conflicts with a playbook `MUST`, report the conflict separately. Capture the nearest safe expression in the theme.

If evidence is contradictory, preserve the stable shared rule. Record a scoped exception only when its product purpose is clear.

## Confirm the import

Before writing, show a concise summary:

- The inferred core theme.
- The strongest evidence-backed rules.
- Each proposed scoped theme.
- Important inconsistencies that will not become direction.
- Questions that code and runtime evidence cannot answer.

Ask only questions that materially change the result. Use the structured multiple-choice format above.

## Write `PRODUCT-THEME.md`

Use the shared product-theme template. Preserve confirmed owner choices from an existing file.

- Keep the file code-free and concise.
- Translate implementation details into observable design rules.
- Complete the theme-topology section.
- State that no scoped themes exist when the evidence supports none.
- Give each signature pattern a job, anatomy, variation, states, and restraint.
- Record deliberate `SHOULD` exceptions with reasons and scope.
- Do not include source-file paths or a raw token inventory in the theme.
- Do not create a second audit document unless the user asks for one.

If the product purpose, audience, core task, or trust promise cannot be inferred, ask the owner. Do not invent product truth from styling alone.

## Finish

Make sure that:

- The core theme describes the whole product.
- Each scoped theme inherits more than it replaces.
- Literal values map to semantic roles.
- The direction distinguishes product choices from historical accidents.
- The file can guide a feature that does not exist yet.
- The theme does not override a playbook `MUST`.

Report the output path, the core theme, the scoped themes, and the most important unresolved uncertainty.
