# Icon Composer delivery

## Preferred workflow

1. Create flat and aligned source layers.
2. Open Icon Composer from `Xcode > Open Developer Tool > Icon Composer`.
3. Set the supported platforms in the document settings.
4. Set the canvas background.
5. Import the layers in their intended order.
6. Create no more than four depth groups.
7. Tune Default, Dark, and Mono.
8. Save the document as a `.icon` package.
9. Add the package to the Xcode target.
10. Build and inspect the installed icon.

The top group in the Icon Composer sidebar is the front group. Make sure that the sidebar order matches the intended depth order.

## Source asset contract

Use these source rules:

- Every source file uses the same canvas size.
- Every foreground PNG has a transparent canvas.
- Every raster background is full-bleed and opaque.
- Every source layer has crisp edges.
- Every filename has a number and a descriptive name.
- No source file contains the final platform mask.
- No source file contains static Liquid Glass effects.

## Direct package edits

A `.icon` file is a package directory. It contains `icon.json` and an `Assets` directory.

Apple does not publish `icon.json` as a stable API. Do not create a schema from memory.

If direct editing is necessary, use a package saved by the installed Icon Composer version.

Preserve fields that you do not understand. Run the package validator after each edit.

Some Icon Composer controls do not appear as explicit fields in every saved package. Do not add guessed fields for group mode or appearance settings. Set those controls in Icon Composer.

Then build the Xcode target. A successful JSON parse does not prove that `actool` accepts the package.

## Xcode integration

Add the `.icon` package as a normal target resource. Do not add it to `Assets.xcassets`.

Set `ASSETCATALOG_COMPILER_APPICON_NAME` to the package filename without `.icon`.

The `.icon` package replaces the primary app-icon asset catalog for the target.

Xcode can generate compatible renditions for older systems. Keep the asset catalog only when exact legacy artwork is required.

## Validation order

1. Run `scripts/validate_icon_package.py`.
2. Build the Xcode target.
3. Install the app on the target simulator.
4. Inspect the Home Screen at normal size.
5. Inspect Default, Dark, Mono, clear, and tinted previews in Icon Composer.
6. Reopen the `.icon` file when Icon Composer has cached old source assets.

If Icon Composer reports a file error, stop direct package edits. Create a new document with that Icon Composer version.
