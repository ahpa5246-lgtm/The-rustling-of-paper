#!/usr/bin/env python3
"""Validate 700-pixel storyboard image files, panel roster, and approval gates.

Usage: python3 scripts/validate_storyboard.py path/to/scene-001
No external dependencies. Visual/narrative quality still requires human inspection.
"""
import argparse
import json
import re
import struct
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def dimensions(path: Path):
    if path.suffix.lower() == ".png":
        with path.open("rb") as f:
            header = f.read(24)
        if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
            raise ValueError(f"{path}: invalid PNG signature or IHDR")
        return struct.unpack(">II", header[16:24])
    if path.suffix.lower() == ".svg":
        root = ET.parse(path).getroot()
        if not root.tag.endswith("svg"):
            raise ValueError(f"{path}: SVG root missing")
        w = root.attrib.get("width", "")
        if not re.fullmatch(r"700(?:\.0+)?(?:px)?", w):
            raise ValueError(f"{path}: width must explicitly be 700px, got {w!r}")
        vb = root.attrib.get("viewBox", "").replace(",", " ").split()
        if len(vb) != 4 or float(vb[2]) <= 0 or float(vb[3]) <= 0:
            raise ValueError(f"{path}: valid numeric viewBox required")
        return 700, int(round(float(vb[3])))
    raise ValueError(f"{path}: expected PNG or SVG")


def validate(scene: Path):
    errors = []
    scene = scene.resolve()
    try:
        state = json.loads((scene / "scene-state.json").read_text(encoding="utf-8"))
        for k in ("editorial", "visual"):
            if state[k]["status"] != "approved":
                errors.append(f"{k} approval missing")
        approved_visual = state["visual"].get("approved_revision")
        current_visual = state["visual"].get("revision")
        if approved_visual != current_visual:
            errors.append("approved visual revision differs from current revision")
    except (OSError, ValueError, KeyError, TypeError) as e:
        return [f"scene-state.json: {e}"]
    try:
        raw = json.loads((scene / "storyboard" / "panels.json").read_text(encoding="utf-8"))
        panels = raw["panels"] if isinstance(raw, dict) else raw
        ids = [p["id"] for p in panels]
        if len(ids) != len(set(ids)):
            errors.append("duplicate panel IDs")
        if state.get("panel_ids") and state["panel_ids"] != ids:
            errors.append("panel IDs/order differ from approved scene-state roster")
        if not ids:
            errors.append("no storyboard panels")
    except (OSError, ValueError, KeyError, TypeError) as e:
        return errors + [f"panels.json: {e}"]
    referenced_parts = []
    for p in panels:
        name = str(p.get("part", ""))
        if not re.fullmatch(r"storyboard-part-\d{2,3}\.(?:png|svg)", name):
            errors.append(f"{p.get('id')}: invalid segment name {name!r}")
            continue
        if name not in referenced_parts:
            referenced_parts.append(name)
        if "top" in p and "bottom" in p and p["top"] >= p["bottom"]:
            errors.append(f"{p.get('id')}: invalid y coordinates")

    asset_dir = scene / "storyboard"
    dimensions_by_part = {}
    for name in referenced_parts:
        path = asset_dir / name
        try:
            width, height = dimensions(path)
            if width != 700:
                errors.append(f"{name}: width {width} != 700")
            if height < 1:
                errors.append(f"{name}: invalid height")
            dimensions_by_part[name] = height
        except (OSError, ValueError, struct.error, ET.ParseError) as e:
            errors.append(f"{name}: {e}")
    for p in panels:
        height = dimensions_by_part.get(p.get("part", ""))
        if height is not None and ("top" in p or "bottom" in p):
            if not (0 <= p.get("top", -1) < p.get("bottom", height + 1) <= height):
                errors.append(f"{p.get('id')}: y-range outside image height")
    if referenced_parts:
        numbers = [int(re.search(r"part-(\d+)", x).group(1)) for x in referenced_parts]
        if numbers != list(range(1, len(numbers) + 1)):
            errors.append("segment order must be consecutive from part-01")
    for path in asset_dir.glob("storyboard-full.*"):
        if path.suffix.lower() in (".png", ".svg"):
            try:
                if dimensions(path)[0] != 700:
                    errors.append(f"{path.name}: master width != 700")
            except (OSError, ValueError, ET.ParseError) as e:
                errors.append(f"{path.name}: {e}")
    return errors


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("scene", type=Path)
    args = parser.parse_args()
    errors = validate(args.scene)
    if errors:
        print("FAIL:\n" + "\n".join("- " + x for x in errors))
        return 1
    print("PASS: approvals, ordered roster and all delivered image widths are valid")
    print("Manual check remains required: plot fidelity, continuity, legibility and sketch-only style")
    return 0


if __name__ == "__main__":
    sys.exit(main())
