---
name: apply-ios-design-direction
description: Apply and review an iOS 26+ design playbook for iPhone and iPad interfaces. Use for HIG, Liquid Glass, hierarchy, color, motion, accessibility, adaptive layout, system surfaces, or custom components. Use when Codex designs, implements, refactors, or reviews native interfaces that need platform-native, product-distinct direction.
---

# Apply iOS Design Direction

Use the shared playbook as a design decision tool. Preserve native behavior and concentrate custom expression on product meaning.

## Load direction

1. Read `references/DESIGN.md` completely.
2. Find and read the app's `PRODUCT-THEME.md` when it exists.
3. Read the relevant product documents and interface code.
4. Treat the app's current system components as evidence, not as permanent design truth.

Use this priority when directions conflict:

1. Current Apple HIG and current system component behavior.
2. Current Apple design guidance and resources.
3. `PRODUCT-THEME.md`.
4. Defaults in `references/DESIGN.md`.
5. Third-party references and visual inspiration.

The product theme can replace a `SHOULD` or select a `MAY`. It cannot override a `MUST`.

## Design a feature

Before implementation, define:

- The primary task.
- The current task phase and next important question.
- The summary, evidence, detail, and action hierarchy.
- The complete state model, including data age and confidence.
- The native navigation and presentation model.
- The content layer and functional layer.
- The iPhone and resizable iPad compositions.
- The required input and accessibility behavior.

Start with system components. Add a custom component only when it clarifies domain meaning, data, progress, causality, or a necessary interaction.

For a new signature pattern, explore at least three different information structures. Select the structure that answers the primary question with the least interpretation.

## Implement a feature

Apply the design decisions during implementation. Do not add a separate design artifact unless the user asks for one.

- Preserve standard navigation, selection, dismissal, menu, sheet, and gesture behavior.
- Use native Liquid Glass for the functional layer.
- Keep dense content on opaque surfaces or standard materials.
- Use semantic type, color, symbols, spacing, and control roles.
- Implement every state and accessibility response in the playbook.
- Keep the product theme visible in hierarchy, custom content, color, motion, imagery, data formatting, and copy.

If the requested direction conflicts with a `MUST`, explain the conflict and implement the nearest safe expression.

## Review a feature

Inspect the rendered result and interaction behavior when tools permit it. Review code alone only when runtime inspection is unavailable.

Report findings in this order:

1. Violated `MUST` statements.
2. Product-theme conflicts.
3. Weak `SHOULD` choices that materially reduce clarity or consistency.
4. Strong opportunities for product-distinct expression.

Do not report a `SHOULD` as a defect when the product has a clear reason to differ. Explain the effect and available trade-off.

## Finish

Use the Agent feature checklist in `references/DESIGN.md`.

Make sure that the result:

- Feels native before it feels branded.
- Makes the next important answer visually strongest.
- Uses color and motion for meaning.
- Keeps custom components useful rather than ornamental.
- Uses Liquid Glass only in the functional layer.
- Reflows for compact iPhone and resizable iPad layouts.
- Works with all required accessibility settings and input methods.

Report the applied product-theme choices and any deliberate playbook exceptions.
