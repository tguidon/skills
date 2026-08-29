# Apple app icon guidance

Use these rules for Liquid Glass app icons.

## Artwork model

- Use a background and one or more foreground layers.
- Use two to four depth groups for most icons.
- Keep the metaphor simple, bold, frontal, and recognizable.
- Use crisp foreground edges. Do not use feathered silhouettes.
- Use overlap and opacity only when they improve depth.
- Keep the primary mark optically centered.

Apple applies the final platform mask. Do not include an enclosure mask in the source artwork.

## Canvas and files

- Use 1024 × 1024 for iPhone, iPad, and Mac.
- Use 1088 × 1088 for Apple Watch.
- Export all layers on the same full-size canvas.
- Prefer SVG for flat and scalable artwork.
- Convert text to outlines when text is necessary.
- Use transparent PNG for raster art and unsupported SVG features.
- Use a full-bleed opaque image only for a custom raster background.

Create the background color or gradient in Icon Composer when possible.

## Dynamic effects

Icon Composer supplies the dynamic material. Do not bake these effects into source assets:

- Blur.
- Layer shadows.
- Specular highlights.
- Refraction.
- Bevels.
- Glow.
- Glass translucency.

Static effects can conflict with system lighting. The system effects also change with icon size and system version.

## Appearances

Use one layered design for Default, Dark, and Mono.

Mono supplies clear and tinted appearances. Use a wide grayscale range and keep one important element near white.

Do not depend on color alone for the core metaphor.

Inspect the icon with these previews:

- The current icon grid.
- The smallest icon size.
- Light and dark wallpapers.
- Light and dark system appearance.
- Clear and tinted appearance.
- Moving-light effects.
- Every platform mask in scope.

## Primary Apple sources

- [Human Interface Guidelines: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons)
- [Creating your app icon using Icon Composer](https://developer.apple.com/documentation/xcode/creating-your-app-icon-using-icon-composer)
- [Icon Composer](https://developer.apple.com/icon-composer/)
- [WWDC25: Create icons with Icon Composer](https://developer.apple.com/videos/play/wwdc2025/361/)
- [WWDC25: Say hello to the new look of app icons](https://developer.apple.com/videos/play/wwdc2025/220/)
