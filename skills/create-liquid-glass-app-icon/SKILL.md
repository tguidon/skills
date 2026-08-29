---
name: create-liquid-glass-app-icon
description: Create or revise layered Apple app icons that use Icon Composer and support Liquid Glass. Use when a user provides icon design direction, requests an iOS 26+ app icon, needs production SVG or PNG layers, or wants a `.icon` package wired into Xcode. Do not use for general interface review or unrelated product-design work.
---

# Create a Liquid Glass App Icon

Create the icon from the user's design direction. Deliver production artwork and a valid Icon Composer package.

## Use the design direction

Treat the user's visual direction as the primary source.

Extract these details when the user supplies them:

- The app name and primary metaphor.
- The desired mood, shape language, and palette.
- Required symbols, brand assets, or reference images.
- Elements to preserve or avoid.
- The target Apple platforms.

Do not review the complete product or codebase. Read only relevant brand assets, screenshots, `PRODUCT-THEME.md`, or existing icon files.

If a missing choice blocks the artwork, ask one short group of questions. Otherwise, make conservative assumptions and continue.

## Read the production guidance

Read [references/apple-icon-guidance.md](references/apple-icon-guidance.md) before you create artwork.

Read [references/icon-composer-delivery.md](references/icon-composer-delivery.md) before you create or edit the `.icon` package.

## Define the icon

Write a short production brief before you create assets. Include:

- The visual metaphor.
- The background treatment.
- The ordered depth groups.
- The palette for Default, Dark, and Mono.
- The smallest-size recognition test.
- The required source files.

Use one clear metaphor. Remove details that do not survive at Home Screen size.

Do not add text, initials, or a new brand element unless the user requests it.

## Create the source artwork

Use a 1024 × 1024 canvas for iPhone, iPad, and Mac. Use a 1088 × 1088 canvas for Apple Watch.

Keep every imported layer on the same full-size canvas. This rule preserves alignment in Icon Composer.

Prefer SVG for flat shapes. Use a transparent PNG for raster art or unsupported SVG features.

Use `$imagegen` when the request needs new raster art or useful concept exploration.

For a vector-friendly mark, use ImageGen for the concept. Then rebuild the selected design as crisp SVG layers.

Do not bake these effects into the source artwork:

- The final rounded-rectangle or circle mask.
- Glass, refraction, or specular highlights.
- Drop shadows, bevels, blur, glow, or edge lighting.
- Material translucency.

Give each layer a numbered, descriptive name. Keep colors separate when an appearance needs independent control.

## Compose the icon

Use Apple Icon Composer for the final composition. Use Computer Use only when app control is necessary and authorized.

If Icon Composer is unavailable, look for the copy bundled with Xcode. If no compatible copy or saved package exists, deliver the source layers and report the exact blocker. Do not invent a package or claim that delivery is complete.

Create a canvas color or gradient in Icon Composer. Do not use an opaque background inside a foreground layer.

Organize the artwork into no more than four depth groups. Put the front group at the top of the Icon Composer sidebar.

Use group mode intentionally:

- Use `Individual` when each shape needs a separate glass response.
- Use `Combined` when the group must behave as one object.

Start with automatic Liquid Glass properties. Then adjust blur, translucency, shadow, refraction, and specular alignment.

Keep high-contrast identity details opaque when glass treatment reduces recognition.

Tune Default, Dark, and Mono. Mono supplies the clear and tinted system appearances.

Inspect all appearances at the smallest preview size. Also inspect varied wallpapers and moving-light previews.

## Create the `.icon` package

Save the Icon Composer document as `<AppIconName>.icon`.

Do not invent `icon.json` fields. Apple does not publish this package schema as a stable API.

If you edit a package directly, start from a file saved by the installed Icon Composer version. Preserve unknown fields.

Run `scripts/validate_icon_package.py <path-to-icon>` after each direct package edit.

The script checks structure and source assets. An Xcode build remains the authoritative compatibility check.

## Add the icon to Xcode

If an Xcode project is in scope, add the `.icon` package as a target resource. Do not put it inside an asset catalog.

Set the App Icon build setting to the `.icon` filename without its extension.

Keep an old asset-catalog icon only when the user needs its exact rendering on older systems.

Use `$xcodebuildmcp-cli` to build and run the app. Inspect the installed Home Screen icon on the exact target simulator.

If the display name is part of the request, make sure that the Home Screen label uses the requested app name.

## Make final checks

Make sure that:

- The icon has a strong silhouette at small sizes.
- The platform mask does not clip the focal shape.
- The foreground edges are crisp.
- Default, Dark, Mono, clear, and tinted appearances remain recognizable.
- The layers use Liquid Glass without losing essential contrast.
- The `.icon` package passes the validation script.
- The Xcode target builds with the new icon.
- The installed icon and label are correct on the Home Screen.

Report the `.icon` path, source asset paths, design choices, appearance behavior, and validation results.
