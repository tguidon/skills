#!/usr/bin/env python3
"""Check the structure and source assets of an Icon Composer package."""

from __future__ import annotations

import argparse
import json
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


ALLOWED_EXTENSIONS = {".svg", ".png", ".pdf", ".jpg", ".jpeg"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check an Apple Icon Composer .icon package."
    )
    parser.add_argument("icon_package", type=Path)
    return parser.parse_args()


def png_size_and_alpha(path: Path) -> tuple[int, int, bool]:
    with path.open("rb") as file:
        signature = file.read(8)
        if signature != b"\x89PNG\r\n\x1a\n":
            raise ValueError("invalid PNG signature")
        length = struct.unpack(">I", file.read(4))[0]
        chunk = file.read(4)
        if chunk != b"IHDR" or length != 13:
            raise ValueError("missing PNG IHDR chunk")
        width, height, _depth, color_type, _compression, _filter, _interlace = (
            struct.unpack(">IIBBBBB", file.read(13))
        )
    return width, height, color_type in {4, 6}


def svg_canvas(path: Path) -> tuple[int, int]:
    root = ET.parse(path).getroot()
    width = root.attrib.get("width", "").removesuffix("px")
    height = root.attrib.get("height", "").removesuffix("px")
    view_box = root.attrib.get("viewBox", "").split()
    if width and height:
        return int(float(width)), int(float(height))
    if len(view_box) == 4:
        return int(float(view_box[2])), int(float(view_box[3]))
    raise ValueError("missing SVG width, height, or viewBox")


def collect_layers(groups: list[object], errors: list[str]) -> list[dict[str, object]]:
    layers: list[dict[str, object]] = []
    for group_index, group in enumerate(groups, start=1):
        if not isinstance(group, dict):
            errors.append(f"group {group_index} is not an object")
            continue
        group_layers = group.get("layers")
        if not isinstance(group_layers, list) or not group_layers:
            errors.append(f"group {group_index} has no layers")
            continue
        for layer_index, layer in enumerate(group_layers, start=1):
            if not isinstance(layer, dict):
                errors.append(
                    f"group {group_index}, layer {layer_index} is not an object"
                )
                continue
            layers.append(layer)
    return layers


def main() -> int:
    args = parse_args()
    package = args.icon_package.expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if package.suffix != ".icon" or not package.is_dir():
        print(f"ERROR: {package} is not an .icon package directory")
        return 1

    metadata_path = package / "icon.json"
    assets_path = package / "Assets"
    if not metadata_path.is_file():
        errors.append("icon.json is missing")
    if not assets_path.is_dir():
        errors.append("Assets directory is missing")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: cannot read icon.json: {error}")
        return 1

    groups = metadata.get("groups")
    if not isinstance(groups, list) or not groups:
        errors.append("icon.json must contain at least one group")
        groups = []
    elif len(groups) > 4:
        errors.append(f"icon.json contains {len(groups)} groups; the maximum is 4")

    supported_platforms = metadata.get("supported-platforms")
    if not isinstance(supported_platforms, dict) or not supported_platforms:
        errors.append("supported-platforms is missing or empty")

    layers = collect_layers(groups, errors)
    canvases: set[tuple[int, int]] = set()
    referenced_assets: set[str] = set()

    for index, layer in enumerate(layers, start=1):
        image_name = layer.get("image-name")
        if not isinstance(image_name, str) or not image_name:
            errors.append(f"layer {index} has no image-name")
            continue
        referenced_assets.add(image_name)
        asset = assets_path / image_name
        if asset.suffix.lower() not in ALLOWED_EXTENSIONS:
            errors.append(f"{image_name} uses an unsupported file extension")
            continue
        if not asset.is_file():
            errors.append(f"referenced asset is missing: {image_name}")
            continue

        try:
            if asset.suffix.lower() == ".svg":
                canvases.add(svg_canvas(asset))
            elif asset.suffix.lower() == ".png":
                width, height, has_alpha = png_size_and_alpha(asset)
                canvases.add((width, height))
                if not has_alpha:
                    warnings.append(
                        f"{image_name} has no alpha channel; use it only as a background"
                    )
        except (OSError, ValueError, ET.ParseError) as error:
            errors.append(f"cannot inspect {image_name}: {error}")

    if len(canvases) > 1:
        errors.append(f"source assets use different canvas sizes: {sorted(canvases)}")
    elif canvases:
        canvas = next(iter(canvases))
        if canvas not in {(1024, 1024), (1088, 1088)}:
            warnings.append(
                f"source canvas is {canvas[0]} × {canvas[1]}; expected 1024 or 1088"
            )

    for asset in assets_path.iterdir():
        if asset.is_file() and asset.name not in referenced_assets:
            warnings.append(f"unreferenced asset: {asset.name}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(
        f"OK: {len(groups)} group(s), {len(layers)} layer(s), "
        f"{len(referenced_assets)} referenced asset(s)"
    )
    if canvases:
        width, height = next(iter(canvases))
        print(f"Canvas: {width} × {height}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
