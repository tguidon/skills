# iOS Design Playbook

This playbook guides the design of native iOS and iPadOS apps for iOS 26 and later. It gives agents a strong starting point without prescribing one visual style.

Use this document with a `PRODUCT-THEME.md` file. The playbook supplies platform patterns. The product theme supplies product character.

## How to use this playbook

Read the rule words as follows:

- **MUST** protects accessibility, legibility, platform behavior, or user trust.
- **SHOULD** defines the preferred starting point. A product theme can replace it with a documented reason.
- **MAY** identifies a tool that fits some products or contexts.

Use this sequence for each feature:

1. Name the primary user task and the information that supports it.
2. Read the product theme and find the relevant character choices.
3. Choose the native navigation model and system components first.
4. Add custom expression in the content layer where it improves meaning.
5. Define every state, size, input method, and accessibility response.
6. Review the result with the checklist at the end of this document.

Do not treat a `SHOULD` as a veto. If another solution better serves the product, record that choice in the product theme.

When two directions conflict, use this priority:

1. Current Apple HIG and system component behavior.
2. Current Apple design guidance and resources.
3. The product theme.
4. The defaults in this playbook.
5. Third-party references and visual inspiration.

A current system component always outranks a static measurement in this file.

## Design character

Aim for this default balance:

- **70% platform-native:** familiar structure, behavior, controls, symbols, and accessibility.
- **20% calm precision:** clear hierarchy, deliberate spacing, and restrained visual noise.
- **10% expressive delight:** confident color, purposeful motion, and memorable domain-specific moments.

The percentages express priorities, not measurable screen area. A product theme can change the balance.

## Core principles

### Make content the protagonist

- **MUST** keep content visually dominant over navigation and controls.
- **MUST** make the current state, next likely action, and important change easy to find.
- **SHOULD** remove decoration before removing useful information.
- **SHOULD** place controls near the content that they affect.

### Keep behavior familiar and expression distinct

- **MUST** preserve expected iOS behavior for navigation, dismissal, selection, menus, sheets, and gestures.
- **SHOULD** use system components unless a custom component communicates the product domain better.
- **MAY** create a custom component when it improves glanceability, compresses a recurring relationship, or enables a necessary interaction.
- **MUST** give each custom component the states and accessibility behavior of an equivalent system component.

### Build hierarchy before decoration

- **MUST** establish hierarchy with order, grouping, alignment, size, and spacing before color or effects.
- **SHOULD** give each screen one clear visual entry point.
- **SHOULD** limit each region to three visible emphasis levels.
- **SHOULD** move secondary actions into menus or later disclosure when primary controls become crowded.

### Concentrate expression

- **SHOULD** spend strong color and custom motion on high-value information or actions.
- **SHOULD** keep routine states visually quiet so important changes feel important.
- **MAY** create one signature visual or interaction for a core product concept.
- **MUST** keep that signature useful without color, motion, or transparency.

### Design the whole state model

- **MUST** design loading, empty, populated, partial, stale, predicted, confirmed, disrupted, recovered, offline, error, disabled, and permission-denied states.
- **MUST** distinguish a temporary state from a final state.
- **SHOULD** preserve context during refresh, retry, and recovery.
- **SHOULD** explain what changed and what the person can do next.
- **MUST** show the age, source, or confidence of information when it affects a decision.

### Design for the next important question

- **MUST** make the strongest element answer the question that matters in the current phase.
- **SHOULD** let hierarchy change when the task moves from planning to action, monitoring, disruption, or reflection.
- **SHOULD** keep identifiers and provenance available but quieter than the next useful answer.
- **MUST** make positive states explicit when silence can create uncertainty.

## Interface layers and Liquid Glass

Treat the interface as two persistent layers and one temporary relationship.

| Layer | Contains | Material direction |
|---|---|---|
| Content layer | Information, media, lists, cards, charts, app backgrounds | Opaque surfaces or standard materials |
| Functional layer | Navigation, toolbars, tab bars, sidebars, floating controls | System Liquid Glass |
| Temporary relationship | Menus, sheets, inspectors, and controls that emerge from a source | System presentation tied to its source |

### Liquid Glass rules

- **MUST** use Liquid Glass as a functional layer above content.
- **MUST NOT** use Liquid Glass as the surface of content cards, lists, tables, or app backgrounds.
- **MUST NOT** stack Liquid Glass on Liquid Glass.
- **MUST** use system components for glass navigation and controls when a suitable component exists.
- **MUST NOT** recreate Liquid Glass with fixed blur, opacity, border, highlight, or shadow values.
- **SHOULD** apply custom glass only to important, top-level controls that float above content.
- **SHOULD** use the Regular variant. It adapts across backgrounds and accessibility settings.
- **MAY** use the Clear variant only when all three conditions are true:
  - The control floats above media-rich content.
  - A dimming layer will not damage the content.
  - The foreground uses bold, bright content that remains legible.
- **MUST NOT** mix Regular and Clear variants in one interface.
- **SHOULD** use tint only for a primary action or a distinct functional purpose.
- **MUST NOT** tint every glass control.
- **MUST** avoid stable intersections between important content and glass controls.
- **MUST** respond to Reduce Transparency, Increase Contrast, and Reduce Motion.

Use standard materials inside the content layer when a surface needs separation. Choose a material for its semantic role, not its apparent color.

### Glass decision test

Ask these questions in order:

1. Is this element app content? If yes, do not use Liquid Glass.
2. Is this element navigation or a top-level floating control? If yes, prefer the system glass component.
3. Is this a transient interactive part of content, such as an active slider? If yes, use its system behavior.
4. Does custom glass improve hierarchy or only add style? If it only adds style, do not use it.
5. Can every label and symbol remain legible over all underlying content? If no, change the placement or material.

## Layout and spatial rhythm

### Adaptive structure

- **MUST** respect safe areas, system margins, Dynamic Type, localization, orientation, and window resizing.
- **MUST** design for the smallest supported iPhone width and a freely resized iPad window.
- **MUST** preserve the same information relationships when the layout changes.
- **SHOULD** change composition at useful content breakpoints. Do not scale an iPhone screen uniformly for iPad.
- **SHOULD** keep related content together when the number of columns changes.
- **MAY** let immersive media or color extend behind a sidebar when foreground content stays undistorted.

### Spacing toolbox

Use system spacing for system components. For custom content, this 4 pt scale is an optional starting point:

| Space | Default use |
|---|---|
| 4 pt | Tight internal relationships |
| 8 pt | Icon-label pairs and compact groups |
| 12 pt | Dense component padding |
| 16 pt | Standard padding and section gaps |
| 24 pt | Major group separation |
| 32 pt | Section separation |
| 48 pt or more | Deliberate dramatic separation |

- **MAY** use 16 pt as the initial compact-width content margin when no system container supplies one.
- **SHOULD** increase margins on wide layouts instead of stretching readable content without limit.
- **SHOULD** use spacing to show relationships. Related items sit closer than unrelated items.
- **MAY** break the scale for optical alignment or a deliberate expressive moment.

### Shape toolbox

- **MUST** preserve system shapes for system controls.
- **SHOULD** use capsules for prominent touch controls and compact status elements.
- **MAY** start with 12 pt for compact repeated content surfaces.
- **MAY** start with 16 pt for standard cards and grouped content.
- **MAY** use 20–24 pt for large hero surfaces with generous padding.
- **MUST** make nested shapes concentric. Start with `inner radius = outer radius - inset` and adjust only for optical balance.
- **SHOULD** use fewer radii. Repeated geometry creates more cohesion than many decorative shapes.

## Information hierarchy

Every primary screen must answer these questions without interaction:

1. Where am I?
2. What is true now?
3. What changed or needs attention?
4. What can I do next?

Use this reading order:

1. **Summary:** the most important state or outcome.
2. **Evidence:** the information that explains the summary.
3. **Detail:** data for deeper inspection.
4. **Action:** the next useful operation near its subject.

- **SHOULD** lead with the meaningful conclusion, not a generic screen title.
- **SHOULD** give numbers units, context, and a comparison when the comparison adds meaning.
- **SHOULD** combine labels and values into scan-friendly rows or groups.
- **MUST NOT** hide a critical state behind disclosure.
- **MUST NOT** turn every group into a card. Use whitespace, sections, and separators first.

## Typography

- **MUST** support Dynamic Type through all accessibility sizes.
- **SHOULD** use San Francisco and semantic text styles.
- **SHOULD** use Regular, Medium, Semibold, or Bold weights. Avoid light weights for interface text.
- **SHOULD** keep body text at the system body size. Custom body text uses 17 pt by default and never less than 11 pt.
- **SHOULD** use size and weight before custom color to establish hierarchy.
- **SHOULD** use bold, left-aligned text for important onboarding, alerts, and high-value summaries.
- **SHOULD** minimize typefaces and avoid manual letter spacing for system text.
- **MUST** let text wrap before it truncates when the full meaning matters.
- **MUST** scale meaningful symbols with adjacent text.

## Color

- **SHOULD** start with semantic system colors.
- **MAY** use custom colors to express the product theme and clarify domain information.
- **MUST** define light, dark, and increased-contrast variants for every custom color.
- **MUST** keep one meaning for each semantic color.
- **MUST NOT** use color as the only carrier of status, selection, or interactivity.
- **SHOULD** use one dominant accent family and a small set of semantic status colors.
- **SHOULD** place confident color in large meaningful fields or small high-value accents.
- **MUST NOT** decorate inactive text with the same color that marks interactive text.
- **MUST** meet a contrast ratio of 4.5:1 for normal text and 3:1 for large or bold text.

## Navigation and presentation

- **MUST** use a stable top-level navigation model.
- **MUST** keep persistent destinations separate from screen-specific actions.
- **SHOULD** use a tab bar for a small set of peer destinations on iPhone.
- **SHOULD** use a sidebar or split view when iPad space reveals useful relationships.
- **SHOULD** make Search a first-class destination when retrieval is central to the product.
- **MUST** preserve swipe-back and standard dismissal behavior.
- **SHOULD** present a sheet for a focused task that preserves the current context.
- **SHOULD** present a menu or popover from the control that caused it.
- **SHOULD** use a full-screen transition only for immersion or a task that needs full attention.
- **MUST** keep destructive actions explicit and recoverable when possible.

### Action placement

- **SHOULD** place the primary action near the content that it affects.
- **SHOULD** separate the primary action from related secondary controls.
- **SHOULD** group bar items by function and frequency.
- **MUST NOT** make separate text and symbol controls look like one combined control.
- **SHOULD** use a text label when no symbol has a clear, familiar meaning.
- **MUST** give gesture-only actions another discoverable path.

## Components and data display

Custom components are product tools, not decoration. A custom component earns its place when it does at least one of these jobs:

- Shows a recurring domain relationship at a glance.
- Compresses complex data without hiding important context.
- Makes status, progress, or change easier to understand.
- Supports an interaction that no suitable system component provides.

For a new signature pattern, explore at least three meaningfully different information structures before selecting one. Do not standardize the first acceptable arrangement.

Useful component families include:

- **Status summary:** a clear state, supporting reason, and next action.
- **Metric group:** a primary value with unit, trend, and comparison.
- **Timeline:** ordered events with current position and exceptions.
- **Progress view:** completed, current, upcoming, delayed, and blocked states.
- **Insight surface:** a conclusion with evidence and a path to detail.
- **Action cluster:** one primary action with related secondary actions.

- **MUST** label axes, units, time ranges, and exceptional values in data displays.
- **MUST** provide a nonvisual description of meaningful charts.
- **SHOULD** reveal detail through selection, expansion, or navigation without replacing the overview.
- **SHOULD** keep decorative marks quieter than the data.
- **MUST NOT** use a chart when a sentence or number communicates the result faster.

## Motion and feedback

Every animation must serve at least one purpose:

- Explain continuity between a source and its result.
- Confirm direct manipulation or an action.
- Reveal a state change or changed relationship.
- Add brief delight to a meaningful product moment.

- **SHOULD** use system transitions and motion first.
- **MUST** keep gesture-driven motion attached to the gesture and interruptible.
- **MAY** start near 150–250 ms for custom direct feedback and 250–450 ms for custom transitions.
- **SHOULD** tune custom timing to the distance, input method, interruption model, and product theme.
- **SHOULD** animate related properties as one coherent event.
- **SHOULD** let menus, sheets, and transient controls emerge from their source.
- **MAY** add one restrained celebratory motion to a high-value success moment.
- **MUST NOT** delay task completion for delight.
- **MUST** replace large movement, depth, elastic motion, and repeated motion when Reduce Motion is active.
- **MUST** avoid fast flashing and uncontrolled peripheral motion.

Use haptics to confirm meaning, not to decorate taps. Keep each haptic meaning consistent across the app.

## Interaction and reachability

- **MUST** give normal touch controls a hit area of at least 44×44 pt.
- **MAY** use a smaller target only in an exceptional dense context.
- **MUST** keep an exceptional target at least 28×28 pt, well separated, and available through an accessible alternative.
- **SHOULD** place frequent iPhone actions near the middle or bottom of the display.
- **MUST** support touch and VoiceOver.
- **MUST** support pointer and hardware-keyboard input for core iPad tasks.
- **SHOULD** add keyboard shortcuts for frequent and command-like iPad actions.
- **MUST** show hover, focus, pressed, selected, disabled, and progress states where those states apply.

## iPhone and iPad adaptation

### iPhone

- Focus each screen on one primary task.
- Keep frequent actions reachable.
- Use progressive disclosure for secondary detail.
- Preserve content during rotation when the product supports landscape.

### iPad

- Use the larger canvas to reveal context and relationships.
- Prefer sidebars, columns, inspectors, and popovers over repeated full-screen transitions.
- Keep useful content density. Do not enlarge every iPhone element.
- Support any window size, orientation, and multitasking arrangement.
- Preserve selection and work state when the window changes size.
- Support touch, pointer, keyboard, and Apple Pencil when the task benefits from them.
- Populate the menu bar with frequent commands and keyboard shortcuts.
- Disable unavailable menu commands in place instead of moving them unpredictably.

Use one shared component anatomy across both devices. The arrangement can change, but meaning and core behavior stay consistent.

## Accessibility and inclusion

Accessibility is part of the first design pass.

- **MUST** support VoiceOver with useful labels, values, traits, actions, and reading order.
- **MUST** support Dynamic Type without losing essential information or actions.
- **MUST** support Dark Mode, Increase Contrast, Reduce Transparency, and Reduce Motion.
- **MUST** support Differentiate Without Color, Button Shapes, Bold Text, Voice Control, Switch Control, and Full Keyboard Access where applicable.
- **MUST** preserve meaning without color, sound, motion, or transparency.
- **MUST** support left-to-right and right-to-left layouts.
- **MUST** allow text expansion for localization.
- **MUST** use locale-aware dates, times, numbers, units, names, and currencies.
- **MUST** provide captions, transcripts, or descriptions for meaningful media.
- **SHOULD** use plain, inclusive language and avoid culture-specific assumptions.
- **SHOULD** reduce cognitive load by making the next action clear and splitting long tasks into understandable stages.

Test the experience at the largest accessibility text size. Test it with VoiceOver, Reduce Motion, Reduce Transparency, Increase Contrast, Dark Mode, and a right-to-left locale.

## State patterns

| State | Direction |
|---|---|
| Loading | Preserve layout when known. State what is loading when the wait matters. |
| Empty | Explain the state and offer the most useful next action. |
| Error | Place the cause and recovery action near the affected content. Preserve entered data. |
| Offline | Distinguish unavailable network data from locally available data. |
| Stale | Show the last update time and the effect of stale information. |
| Predicted | Label the value as a prediction. Show confidence or range when it affects the decision. |
| Confirmed | Distinguish a verified fact from an earlier prediction without destroying useful history. |
| Recovered | Explain what returned to normal and preserve the earlier disruption when that history matters. |
| Permission denied | Explain the benefit before requesting access. Provide a path that does not require access when possible. |
| Disabled | Keep the control legible. Explain the unmet condition when it is not obvious. |
| Success | Confirm the result near its source. Preserve momentum toward the next task. |

## System surfaces

The best interface is not always the open app.

- **SHOULD** identify the smallest system surface that can answer the current question.
- **MAY** use Live Activities for changing, time-sensitive state.
- **MAY** use widgets for glanceable, stable, or periodically updated information.
- **MAY** use notifications for important changes that require awareness or action.
- **MAY** use App Shortcuts, Siri, Spotlight, controls, and shared links for direct access to frequent tasks.
- **MUST** keep meaning and terminology consistent across every surface.
- **MUST** make each surface useful within its interaction and privacy limits.

## Product theme boundary

The product theme can define:

- Product values and emotional tone.
- The platform-native, calm, and expressive balance.
- Accent and semantic color roles.
- Typography choices within accessibility limits.
- Content density and hierarchy preferences.
- Shape preferences for custom content.
- Signature components, data displays, motion, haptics, imagery, and sound.
- App-specific adaptation rules for iPhone and iPad.
- Deliberate exceptions to `SHOULD` statements.

The product theme cannot override a `MUST`. Update this playbook when a product exposes a valid new foundation rule.

## Agent feature checklist

Before implementation, make sure that the feature has:

- [ ] One named primary task.
- [ ] A clear summary, evidence, detail, and action hierarchy.
- [ ] A native navigation and presentation model.
- [ ] A justified boundary between system and custom components.
- [ ] Correct content, functional, and temporary layers.
- [ ] Every data and permission state.
- [ ] Compact iPhone and resizable iPad layouts.
- [ ] Touch, pointer, keyboard, and VoiceOver behavior where applicable.
- [ ] Dynamic Type and localization behavior.
- [ ] Dark Mode and increased-contrast colors.
- [ ] Reduce Motion and Reduce Transparency behavior.
- [ ] A useful experience without color or animation.

After implementation, review the feature at small and large sizes. Review the light, dark, high-contrast, reduced-transparency, and reduced-motion appearances.
