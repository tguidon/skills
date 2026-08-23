# iOS Design Evidence Guide

Use this guide to infer a product theme from an implemented app.

## Contents

- Evidence order
- Repository search map
- Runtime sample
- Intent and confidence
- Theme topology
- Reconciliation rules
- Capture checklist

## Evidence order

Use several evidence types. No single file proves a product theme.

| Strength | Evidence | What it proves |
|---|---|---|
| Highest | Current rendered flows | The actual visual and interaction result |
| High | Central semantic themes, tokens, and assets | Intended shared roles and supported variants |
| High | Reusable components and styles with many call sites | Stable component anatomy and repeated behavior |
| Medium | Repeated screen-level choices | An implicit convention that can lack central ownership |
| Medium | Previews, snapshot tests, widgets, and extensions | Expected states and system-surface consistency |
| Low | One-off constants, unused code, experiments, and old previews | A possible choice that needs corroboration |

Use product documents for purpose and terminology. Use implementation evidence for current visual behavior.

An existing `PRODUCT-THEME.md` outranks inferred intent. The implementation can reveal drift, incomplete adoption, or undocumented scoped themes.

## Repository search map

Start with project structure. Find app targets, extensions, feature modules, shared UI modules, and asset catalogs.

### Theme and token definitions

Search for names and types that describe:

- Theme, palette, appearance, style, design, token, metric, spacing, radius, shadow, and typography.
- SwiftUI environment keys and custom environment values.
- `ShapeStyle`, `ButtonStyle`, `ToggleStyle`, `LabelStyle`, `ViewModifier`, and custom modifiers.
- UIKit `UIAppearance`, tint, configuration objects, and shared factories.
- Asset-catalog color sets and appearance variants.
- Font registration and dynamic type scaling.

Read definitions and call sites. A token name without use does not prove current direction.

### Color

Map literal colors and named assets to semantic jobs:

- Product accent and primary action.
- Content background, grouped surface, elevated surface, and separator.
- Primary, secondary, tertiary, and disabled text.
- Positive, warning, critical, informational, selection, focus, and progress.
- Feature-specific or content-supplied roles.

Find light, dark, and increased-contrast variants. Note when a role exists without all appearances.

Do not treat every asset color as active. Find its uses and supported states.

### Typography

Record semantic text styles, custom typefaces, weights, number styles, and recurring relationships.

Look for:

- Display type that appears only in high-value content.
- Monospaced digits or domain-specific data formatting.
- Repeated label-value, title-summary, and metadata relationships.
- Manual sizes that bypass Dynamic Type.
- Feature-specific typography that can indicate a scoped theme.

### Shape, spacing, and surfaces

Find shared metrics before isolated values.

Record:

- Content margins and spacing rhythm.
- Repeated radii and concentric nesting.
- Capsules, badges, cards, grouped lists, separators, and edge treatments.
- Material, blur, opacity, shadow, stroke, and depth behavior.
- Liquid Glass use in navigation and controls.

Classify the visual result by semantic job. Do not turn every numeric value into a product rule.

### Components and hierarchy

Find components that appear across features or encode domain meaning.

Record:

- Stable anatomy and variation points.
- Summary, evidence, detail, and action order.
- States and accessibility behavior.
- Ownership by the core app or one feature.
- Whether the component clarifies meaning or adds decoration.

A repeated custom component can be more important than a formal token file.

### Motion, haptics, imagery, and sound

Find animation helpers, transitions, matched geometry, haptic generators, sound assets, illustrations, and image treatments.

Record the event and purpose for each repeated effect. Do not document a duration without its interaction meaning.

Find reduced-motion behavior and non-audio alternatives.

### Navigation and adaptation

Map the top-level navigation model and presentation rules.

Inspect:

- Tabs, sidebars, split views, navigation stacks, sheets, inspectors, menus, and popovers.
- Compact and regular width compositions.
- Window resizing, selection preservation, pointer behavior, and keyboard commands.
- Widgets, notifications, Live Activities, App Intents, and other system surfaces.

Platform structure belongs to the shared playbook. Product-specific emphasis belongs in the product theme.

## Runtime sample

Select a small sample that spans the product language:

1. The primary repeated flow.
2. The main navigation destinations.
3. A dense or high-stakes screen.
4. Empty, loading, error, and success states.
5. A modal or transient interaction.
6. Each suspected scoped theme.
7. An iPad layout or wide window when supported.

Inspect light and dark appearances. Add large Dynamic Type and reduced-motion or increased-contrast appearances when tools permit.

Do not infer the whole product from onboarding, marketing screenshots, or one polished hero screen.

## Intent and confidence

Classify each candidate rule.

### Intent

- **Deliberate:** Centralized, repeated, named semantically, or reinforced by runtime behavior.
- **Inherited:** Supplied by iOS or a shared dependency without product-specific modification.
- **Experimental:** Isolated behind a feature flag, preview, prototype, or unfinished path.
- **Legacy:** Superseded, unused, or limited to an older architecture.
- **Accidental:** A local difference without a semantic reason or stable scope.

### Confidence

- **High:** Several strong evidence types agree.
- **Medium:** Repeated evidence exists, but ownership or intent remains unclear.
- **Low:** The inference relies on one source or conflicting evidence.

Write high-confidence rules directly. Confirm medium-confidence rules when they affect future direction.

Do not write a low-confidence choice as a rule. Ask the owner or omit it.

## Theme topology

Use the smallest topology that explains the product.

### Core product theme

Every app has one core theme. It defines shared hierarchy, interaction character, semantic roles, component conventions, and product voice.

### Feature theme

Use a feature theme when one feature has stable local rules across several elements or states.

A feature theme inherits navigation behavior, accessibility, type semantics, and core component anatomy unless evidence proves a bounded replacement.

### Content theme

Use a content theme when content supplies a visual language. Examples include flash-card decks, notebooks, teams, destinations, or game worlds.

Separate user-selected appearance from semantic status. A red deck theme cannot replace the critical-error role.

### Context mode

Use a context mode for a temporary task phase, such as focus, creation, celebration, urgency, or immersion.

A context mode needs clear entry and exit behavior. It does not become a second app-wide theme.

### Promotion test

Promote a local treatment into a scoped theme only when all conditions are true:

1. The scope or trigger is clear.
2. The treatment repeats across components or states.
3. The changed roles form a coherent visual purpose.
4. The treatment preserves named core-theme invariants.
5. A future feature can apply the rules without copying one screen.

## Reconciliation rules

Use coherent capture unless the user selects another mode.

- Keep a pattern when it is repeated, meaningful, accessible, and current.
- Consolidate literal variants that perform the same semantic job.
- Preserve local variation when it has a clear theme boundary.
- Exclude accidental inconsistency from future direction.
- Report current violations of playbook `MUST` statements as gaps.
- Never redefine a violation as brand character.
- Preserve owner-authored direction when code has not adopted it completely.
- Report drift when documentation and the current app disagree.

The result describes what future work must continue. It is not a census of every value in the repository.

## Capture checklist

- [ ] Read product documents and existing theme guidance.
- [ ] Map targets, features, shared UI, and asset catalogs.
- [ ] Find central definitions and their call sites.
- [ ] Inspect representative runtime flows when possible.
- [ ] Map color, type, spacing, shape, surface, imagery, motion, and sound roles.
- [ ] Identify signature components and state behavior.
- [ ] Separate core, feature, content, and context themes.
- [ ] Classify intent and confidence.
- [ ] Exclude accidental, legacy, and inaccessible choices from direction.
- [ ] Confirm unresolved product truth with the owner.
- [ ] Write one concise `PRODUCT-THEME.md`.
- [ ] Make sure that each scoped theme inherits more than it replaces.
