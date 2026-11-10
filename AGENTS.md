# LoopFlow R2X Repository Instructions

範圍：本 repo。另須遵守上一層 `E:\_GitHub\AGENTS.md`。

這是獨立的 Rhino 工具列外掛。按鈕只呼叫既有的 R2B、R2O、R2M 指令，本身不同步。

- 套件 id：`loopflow-R2X-Toolbar`
- 外掛顯示名稱：`LoopFlow R2X`（`.rhp` / `.rui` 同名，分頁才會自動出現）
- 工具列由 `tools/build_rui.py` 從三個產品的 `.rui` 複製按鈕、圖示與指令後產出 `toolbar/LoopFlow_R2X.rui`（含各產品的淺／深色 SVG）
- 已發布的 tag 不移動、不覆寫
- Rhino 9：相容測試進行中（2026-11-04 起）。Package Manager 安裝已通過。執行測試由使用者陸續做。通過前公開說明仍寫 Rhino 8；不發 `rh9_0` yak、不為 Rhino 9 改功能碼
