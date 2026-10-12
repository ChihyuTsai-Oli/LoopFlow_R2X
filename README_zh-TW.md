[English Version](./README.md)

An open-source workflow automation tool developed by **蔡智聿 (Chihyu Tsai)**. [https://intro.chihyu-tsai.com](https://intro.chihyu-tsai.com)

---

# LoopFlow｜R2X Toolbar

選用的整併工具列。只呼叫既有的 Rhino to Blender、Octane、MEP Sync 指令，本身不負責同步，也不取代那三個產品。

[▶ Releases](https://github.com/ChihyuTsai-Oli/LoopFlow_R2X/releases)

## 它做什麼

分頁 **LoopFlow R2X** 有十二顆按鈕，分成三組，組與組之間有分隔條：

- Rhino to Blender Sync：Open、Models（右鍵 Objects）、Camera（右鍵 Camera Push）、Light（右鍵 Light Push）
- Rhino to Octane Sync：Open、Models（右鍵 Objects）、Camera（右鍵 Camera Push）、Point
- Rhino to MEP Sync：Open、Storey、Models、Inbound

三個產品裝完仍會各自開自己的分頁。想只留這一個分頁時，自己關掉那三個。R2X 不包含那些套件，執行時也不讀它們的檔案。該產品有安裝，按鈕才會作用。沒安裝時，Rhino 會回報找不到指令。

## 系統需求

- **Rhino 8**（Windows）

## 安裝

1. 開啟 Rhino 8，命令列執行 `PackageManager`
2. 搜尋 **`loopflow-R2X-Toolbar`** 並安裝
3. 或從 [Releases](https://github.com/ChihyuTsai-Oli/LoopFlow_R2X/releases) 下載 `loopflow-r2x-toolbar-1.0.2-rh8_0-win.yak`，在 Package Manager 選擇從檔案安裝
4. **完全關掉 Rhino 再開**
5. 使用分頁 **LoopFlow R2X**。若沒出現：到 **Tools → Options → Plug-ins**（工具 → 選項 → 外掛程式）勾選 **LoopFlow R2X**

Rhino to Blender Sync、Rhino to Octane Sync、Rhino to MEP Sync 要另外安裝。這個工具列不包含它們，那些套件也不需要先裝這個。

## 相關專案

- [LoopFlow｜Half-automatic 2D/3D Sync](https://github.com/ChihyuTsai-Oli/LoopFlow/blob/main/README_zh-TW.md)
- [LoopFlow｜Rhino to Blender Sync](https://github.com/ChihyuTsai-Oli/LoopFlow_Rhino-to-Blender-Sync/blob/main/README_zh-TW.md)
- [LoopFlow｜Rhino to Octane Sync](https://github.com/ChihyuTsai-Oli/LoopFlow_Rhino-to-Octane-Sync/blob/main/README_zh-TW.md)
- [LoopFlow｜Rhino to MEP Sync](https://github.com/ChihyuTsai-Oli/LoopFlow_Rhino-to-MEP-Sync/blob/main/README_zh-TW.md)

## 授權

本專案採用 [MIT License](./LICENSE) 發布。
