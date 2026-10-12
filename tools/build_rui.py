"""從三個產品的工具列複製 4 顆按鈕，組成 LoopFlow R2X。

圖示整段原文複製，避免 XML 解析器改寫 SVG。
"""
from __future__ import annotations

import base64
import re
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    Path(r"E:\_GitHub\LoopFlow_Rhino-to-Blender-Sync\wip\docs\toolbar\LoopFlow_R2B.rui"),
    Path(r"E:\_GitHub\LoopFlow_Rhino-to-Octane-Sync\wip\docs\toolbar\LoopFlow_R2O.rui"),
    Path(r"E:\_GitHub\LoopFlow_Rhino-to-MEP-Sync\wip\docs\toolbar\LoopFlow_R2M.rui"),
]
OUT = ROOT / "toolbar" / "LoopFlow_R2X.rui"
TOOLBAR_PNG = ROOT / "packaging" / "toolbar.png"

ITEM_RE = re.compile(r"<tool_bar_item\b.*?</tool_bar_item>", re.DOTALL)
MACRO_RE = re.compile(r"<macro_item\b.*?</macro_item>", re.DOTALL)
ICON_RE = re.compile(r"<icon\b.*?</icon>", re.DOTALL)
GUID_ATTR = re.compile(r'\bguid="([^"]+)"')
SIDE_RE = {
    "left_macro_id": re.compile(r"<left_macro_id>([^<]+)</left_macro_id>"),
    "right_macro_id": re.compile(r"<right_macro_id>([^<]+)</right_macro_id>"),
}
BITMAP_RE = re.compile(r'\bbitmap_id="([^"]+)"')


def gid() -> str:
    return str(uuid.uuid4())


def blocks(pattern, text):
    found = {}
    for match in pattern.finditer(text):
        block = match.group(0)
        key = GUID_ATTR.search(block)
        if key:
            found[key.group(1)] = block
    return found


def take_group(path: Path):
    text = path.read_text(encoding="utf-8")
    macros = blocks(MACRO_RE, text)
    icons = blocks(ICON_RE, text)
    toolbar = re.search(r"<tool_bar\b.*?</tool_bar>", text, re.DOTALL)
    if toolbar is None:
        raise SystemExit("no toolbar in " + str(path))
    items = []
    out_macros = []
    out_icons = []
    macro_map = {}
    icon_map = {}
    for raw_item in ITEM_RE.findall(toolbar.group(0)):
        item = raw_item
        kept = False
        for side, pattern in SIDE_RE.items():
            found = pattern.search(item)
            if found is None:
                continue
            old = found.group(1).strip()
            if old not in macros:
                item = pattern.sub("", item)
                continue
            if old not in macro_map:
                cloned = macros[old]
                new_macro = gid()
                cloned = GUID_ATTR.sub('guid="' + new_macro + '"', cloned, count=1)
                bitmap = BITMAP_RE.search(cloned)
                if bitmap and bitmap.group(1) in icons:
                    old_icon = bitmap.group(1)
                    if old_icon not in icon_map:
                        icon = icons[old_icon]
                        new_icon = gid()
                        icon = GUID_ATTR.sub('guid="' + new_icon + '"', icon, count=1)
                        icon_map[old_icon] = new_icon
                        out_icons.append(icon)
                    cloned = BITMAP_RE.sub(
                        'bitmap_id="' + icon_map[old_icon] + '"', cloned, count=1
                    )
                macro_map[old] = new_macro
                out_macros.append(cloned)
            item = item.replace(old, macro_map[old], 1)
            kept = True
        if kept:
            lines = ['      <tool_bar_item guid="' + gid() + '">']
            for side, pattern in SIDE_RE.items():
                found = pattern.search(item)
                if found:
                    lines.append("        <" + side + ">" + found.group(1).strip() + "</" + side + ">")
            lines.append("      </tool_bar_item>")
            items.append("\n".join(lines))
    return items, out_macros, out_icons


def toolbar_icon():
    raw = base64.b64encode(TOOLBAR_PNG.read_bytes()).decode("ascii")
    icon_guid = gid()
    icon = (
        f'<icon guid="{icon_guid}" name="LoopFlow_R2X.svg">\n'
        "      <light><svg width=\"48\" height=\"48\" version=\"1.1\" "
        'xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">'
        f'<image href="data:image/png;base64,{raw}" width="48" height="48"/>'
        "</svg></light>\n"
        "    </icon>"
    )
    return icon_guid, icon


def main():
    groups = [take_group(path) for path in SOURCES]
    counts = [len(group[0]) for group in groups]
    if counts != [4, 4, 4]:
        raise SystemExit("expected 4 buttons in each source toolbar, got " + str(counts))
    tab = gid()
    icon_guid, icon = toolbar_icon()
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        f'<RhinoUI major_ver="5" minor_ver="0" guid="{gid()}">',
        "  <tool_bar_groups>",
        f'    <tool_bar_group guid="{gid()}" dock="top" visable="true" '
        f'active_tool_bar="{tab}" hide_single_tab="False">',
        "      <text>",
        "        <locale_1033>LoopFlow R2X</locale_1033>",
        "      </text>",
        f'      <tool_bar_group_item guid="{tab}" major_version="1" minor_version="1">',
        "        <text>",
        "        <locale_1033>LoopFlow R2X</locale_1033>",
        "        </text>",
        f"        <tool_bar_id>{tab}</tool_bar_id>",
        "      </tool_bar_group_item>",
        "    </tool_bar_group>",
        "  </tool_bar_groups>",
        "  <tool_bars>",
        f'    <tool_bar guid="{tab}" bitmap_id="{icon_guid}">',
        "      <text>",
        "        <locale_1033>LoopFlow R2X</locale_1033>",
        "      </text>",
    ]
    macros = []
    icons = [icon]
    for index, (buttons, group_macros, group_icons) in enumerate(groups):
        if index:
            parts.append(
                f'      <tool_bar_item guid="{gid()}" button_type="Separator" />'
            )
        parts.extend(buttons)
        macros.extend(group_macros)
        icons.extend(group_icons)
    parts.extend(
        [
            "    </tool_bar>",
            "  </tool_bars>",
            "  <macros>",
        ]
    )
    for macro in macros:
        parts.append("    " + macro.replace("\n", "\n    "))
    parts.append("  </macros>")
    parts.append("  <icons>")
    for icon_block in icons:
        parts.append("    " + icon_block.replace("\n", "\n    "))
    parts.extend(["  </icons>", "</RhinoUI>", ""])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text_out = "\n".join(parts)
    OUT.write_text(text_out, encoding="utf-8", newline="\n")
    print("buttons", text_out.count("<tool_bar_item "))
    print("separators", text_out.count('button_type="Separator"'))
    for token in (
        "! _RBOpen",
        "! _RBModels",
        "! _RBObjects",
        "! _RBCamera",
        "! _RBCameraPush",
        "! _RBLight",
        "! _RBLightPush",
        "! _ROOpen",
        "! _ROModels",
        "! _ROObjects",
        "! _ROCamera",
        "! _ROCameraPush",
        "! _ROPoint",
        "! _RMOpen",
        "! _RMStorey",
        "! _RMModels",
        "! _RMInbound",
    ):
        if token not in text_out:
            raise SystemExit("missing " + token)
    if "c40c3a2a" in text_out or "653f328d" in text_out:
        raise SystemExit("dangling right-click macro was copied")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
