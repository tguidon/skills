---
name: create-ios-product-theme
description: Interview a product owner and create or revise PRODUCT-THEME.md for an iOS 26+ app. Use when Codex defines visual character, themes iPhone and iPad products, or translates design references into independent rules. Use when coding agents need app-specific direction without a rigid design system.
---

# Create an iOS Product Theme

Create the product-specific layer that pairs with a reusable iOS design playbook. Preserve platform behavior and make product expression explicit.

## Start

1. Find and read `DESIGN.md` and any existing `PRODUCT-THEME.md` in the current workspace.
2. Use `assets/PRODUCT-THEME-TEMPLATE.md` as the output structure.
3. If `DESIGN.md` is absent, explain that the theme will lack its foundation. Continue only if the user wants a standalone theme.
4. Ask where to save the file only when the user requests a name other than `PRODUCT-THEME.md` or multiple candidate roots exist.

If an implemented app already has a meaningful visual language, use `$capture-ios-product-theme` when the user wants to preserve it. Continue here when the user wants new direction or an owner-led revision.

## Interview

Interview in short rounds. Ask one to three related questions per round.

Use structured multiple-choice questions for every interview prompt:

- Use `request_user_input` when the tool is available.
- Ask one to three questions in each tool call.
- Give each question two or three mutually exclusive choices.
- Put the recommended choice first. Add `(Recommended)` to its label.
- Keep each label between one and five words.
- Explain the effect or trade-off of each choice in one sentence.
- Do not add an `Other` choice. The client supplies a free-form `Other` response.
- If the tool is unavailable, show the same choices in plain text. Tell the user that they can type a custom answer.
- If exact text is required, offer useful starter choices. Let the free-form response collect the exact value.

Ask only unresolved questions. Use existing product documents, code, and prior conversation before you ask.

### Round 1: Product truth

Resolve these items first:

- Product purpose and important outcome.
- Primary audience, context, and expertise.
- Core repeated task.
- Trust promise and cost of user error.

Challenge vague terms. Use a concrete scenario when two interpretations remain possible.

### Round 2: Character

Resolve these items:

- Platform-native, calm-precision, and expressive-delight percentages. The total is 100%.
- Three to five character words.
- Three to five opposing words.
- The emotional difference between routine, important, and celebratory moments.
- The boundary between the core product theme and any feature, content, or context themes.

If the user names a reference app, ask which qualities matter. Translate those qualities into independent rules. Do not require the team to know the reference app.

### Round 3: Hierarchy and density

Resolve these items:

- The first signal on the primary screen.
- The evidence that supports that signal.
- The default information density.
- Information that stays visible and information that waits behind interaction.
- The app's treatment of numbers, units, comparisons, timelines, and status.

Use a realistic high-pressure or edge-case screen to make sure that the hierarchy remains useful.

### Round 4: Visual expression

Resolve these items:

- Product accent and semantic color roles.
- Type character and any display typeface role.
- Content surfaces, separators, depth, and custom shape family.
- Imagery, symbols, charts, sound, and texture.
- Product-specific Liquid Glass emphasis within the playbook boundary.

Keep custom color semantic. Require light, dark, and increased-contrast behavior.

### Round 5: Interaction and adaptation

Resolve these items:

- Motion character and one signature moment.
- Haptic meanings and reduced-motion replacements.
- iPhone composition and reachable actions.
- iPad relationships, tools, input methods, and window adaptation.
- Product boundaries and deliberate exceptions to `SHOULD` statements.

Do not accept an exception that overrides a `MUST` in `DESIGN.md`. Explain the conflict and find another expression.

## Synthesize

After the interview:

1. State the design thesis in one sentence.
2. Show a short decision summary and resolve contradictions with the user.
3. Create `PRODUCT-THEME.md` from the bundled template.
4. Delete all bracketed prompts and unused sections.
5. Keep the document code-free and concise.
6. Record rules that an agent can observe in a rendered interface.
7. Give each signature pattern a job, anatomy, variation range, state set, and restraint.
8. Record each playbook exception with its reason and affected scope.
9. Give each scoped theme a trigger, inheritance rule, permitted replacements, invariants, and fallback behavior.

Do not edit `DESIGN.md` unless the user asks. If the interview reveals a reusable foundation rule, propose that change separately.

## Make sure that the theme is complete

Before delivery, make sure that:

- The character percentages total 100%.
- The theme has one product purpose, one core task, and one trust promise.
- Color roles have one meaning and cover all required appearances.
- Custom components explain meaning or task flow.
- Motion has a purpose and a reduced-motion replacement.
- iPhone and iPad share anatomy but use suitable compositions.
- Each scoped theme inherits more than it replaces.
- The theme does not override a playbook `MUST`.
- No bracketed prompt or unresolved placeholder remains.
- The document gives enough direction to design one unfamiliar feature.

Report the output path and the three most consequential product choices.
