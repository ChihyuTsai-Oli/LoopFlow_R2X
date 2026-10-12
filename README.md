[繁體中文版](./README_zh-TW.md)

An open-source workflow automation tool developed by **蔡智聿 (Chihyu Tsai)**. [https://intro.chihyu-tsai.com](https://intro.chihyu-tsai.com)

---

# LoopFlow｜R2X Toolbar

An optional combined toolbar. It calls the existing Rhino to Blender, Octane, and MEP Sync commands. It does not sync anything, and it does not replace those products.

[▶ Releases](https://github.com/ChihyuTsai-Oli/LoopFlow_R2X/releases)

## What it does

The **LoopFlow R2X** tab has twelve buttons in three groups, with a separator between groups:

- Rhino to Blender Sync: Open, Models (right-click Objects), Camera (right-click Camera Push), Light (right-click Light Push)
- Rhino to Octane Sync: Open, Models (right-click Objects), Camera (right-click Camera Push), Point
- Rhino to MEP Sync: Open, Storey, Models, Inbound

Those three products still open their own tabs after install. Close those tabs yourself if you want to keep only this one. R2X does not include them, and it does not read their files when it runs. A button only works after that product is installed. If it is not, Rhino reports that the command was not found.

## System requirements

- **Rhino 8** (Windows)

## Install

1. Open Rhino 8 and run `PackageManager`.
2. Search for **`loopflow-R2X-Toolbar`** and install.
3. Or download `loopflow-r2x-toolbar-1.0.2-rh8_0-win.yak` from [Releases](https://github.com/ChihyuTsai-Oli/LoopFlow_R2X/releases) and install from file.
4. **Quit Rhino completely and reopen it.**
5. Use the **LoopFlow R2X** tab. If it does not appear: **Tools → Options → Plug-ins**, enable **LoopFlow R2X**.

Install Rhino to Blender Sync, Rhino to Octane Sync, and Rhino to MEP Sync separately. This toolbar does not include them, and those packages do not require this one.

## Related projects

- [LoopFlow | Half-automatic 2D/3D Sync](https://github.com/ChihyuTsai-Oli/LoopFlow)
- [LoopFlow | Rhino to Blender Sync](https://github.com/ChihyuTsai-Oli/LoopFlow_Rhino-to-Blender-Sync)
- [LoopFlow | Rhino to Octane Sync](https://github.com/ChihyuTsai-Oli/LoopFlow_Rhino-to-Octane-Sync)
- [LoopFlow | Rhino to MEP Sync](https://github.com/ChihyuTsai-Oli/LoopFlow_Rhino-to-MEP-Sync)

## License

Released under the [MIT License](./LICENSE).
