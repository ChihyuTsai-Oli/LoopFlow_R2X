"""確認共用工具列的按鈕順序、分隔條與圖示原文。"""
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUI = ROOT / "toolbar" / "LoopFlow_R2X.rui"

LEFT = [
    "! _RBOpen",
    "! _RBModels",
    "! _RBCamera",
    "! _RBLight",
    "! _ROOpen",
    "! _ROModels",
    "! _ROCamera",
    "! _ROPoint",
    "! _RMOpen",
    "! _RMStorey",
    "! _RMModels",
    "! _RMInbound",
]
RIGHT = {
    1: "! _RBObjects",
    2: "! _RBCameraPush",
    3: "! _RBLightPush",
    5: "! _ROObjects",
    6: "! _ROCameraPush",
}


class ToolbarTests(unittest.TestCase):
    def setUp(self):
        self.root = ET.parse(RUI).getroot()
        self.macros = {}
        for macro in self.root.find("macros"):
            self.macros[macro.get("guid")] = (macro.findtext("script") or "").strip()

    def test_tab_name(self):
        texts = [node.text for node in self.root.iter("locale_1033")]
        self.assertGreaterEqual(texts.count("LoopFlow R2X"), 3)

    def test_buttons_and_separators(self):
        items = list(self.root.find("tool_bars/tool_bar"))
        kinds = []
        for item in items:
            if item.tag != "tool_bar_item":
                continue
            if item.get("button_style") == "spacer":
                kinds.append("sep")
            else:
                kinds.append("btn")
        self.assertEqual(kinds, ["btn"] * 4 + ["sep"] + ["btn"] * 4 + ["sep"] + ["btn"] * 4)

    def test_commands(self):
        buttons = [
            item
            for item in self.root.find("tool_bars/tool_bar")
            if item.tag == "tool_bar_item" and item.get("button_style") != "spacer"
        ]
        self.assertEqual(len(buttons), 12)
        for index, item in enumerate(buttons):
            left = (item.findtext("left_macro_id") or "").strip()
            self.assertEqual(self.macros[left], LEFT[index])
            right = (item.findtext("right_macro_id") or "").strip()
            if index in RIGHT:
                self.assertEqual(self.macros[right], RIGHT[index])
            else:
                self.assertEqual(right, "")

    def test_icons_kept_as_svg(self):
        raw = RUI.read_text(encoding="utf-8")
        self.assertNotIn("ns0:", raw)
        self.assertIn('xmlns="http://www.w3.org/2000/svg"', raw)
        self.assertGreaterEqual(raw.count("<icon "), 13)
        self.assertNotIn("c40c3a2a", raw)
        self.assertNotIn("653f328d", raw)
        self.assertNotIn('button_type="Separator"', raw)
        self.assertEqual(raw.count('button_style="spacer"'), 2)


if __name__ == "__main__":
    unittest.main()
