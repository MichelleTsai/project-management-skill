# project-management-skill

## 使用說明（簡短）

這個 repository 包含一套 Domain Knowledge（DK）建立與維護的 skill，用來：
- 引導 Kickoff 訪談並產出 `logic_map/` 下的專案檔案
- 每週以 `log.md` 維護變更，並在週五更新 `report.md`

主要檔案與路徑：
- 問卷（會前或私訊使用）： `dk-system/kickoff_full_questionnaire.md`
- Kickoff / Report / Log 輸出： `logic_map/{project}_kickoff.md`, `logic_map/{project}_report.md`, `logic_map/{project}_log.md`
- Schema 驗證工具（通用）： `tools/validate_schema.py`（用來比對 sample 與預期 schema）

常用觸發指令（可直接說給 skill 或貼入對話）：
- 「我接了一個新專案」：回傳會前問卷（或啟動逐題引導），協助收集 Kickoff 資訊
- 「我剛 Kickoff 完 / 幫我建立邏輯地圖」：把 Kickoff 筆記整理成 `logic_map/{project}_kickoff.md` 並產出初版 `report.md`、`log.md`
- 「週五到了 / 幫我更新邏輯地圖」：把 `log.md` 的流水帳合入 `report.md`（變動標註為「本週更新」），並清空 `log.md`
- 「log: ...」 或 「新增流水帳：...」：把文字新增到指定專案的 `log.md` 當週條目
- 「存成 kickoff 檔名 XXX」：將目前內容儲存為 `logic_map/XXX_kickoff.md`（若允許，也可 commit/push）

重要流程與原則（摘要）：
- 在自動產出 report 前，先對 sample data 做 schema 驗證（使用 `tools/validate_schema.py`），若驗證失敗請標註為「待確認」。
- 每個 `report.md` 應定義採用（Adoption）指標與回退條件；若採用率低於門檻，應暫停自動化輸出並安排示範或修正。
- 文件內不會包含任何真實專案的私人或特定人名測試細節；所有檢查與指引皆為通用步驟。

有需要我可以把這些操作自動化為小工具或快捷命令（例如把問卷自動貼到會議說明、或在收到回覆後自動整理成 kickoff.md）。

## Skill 涵蓋情境清單（整合）
此處整合每個情境的描述與「如何使用」短指令（可直接貼給 skill），詳細步驟仍可參考： [dk-system/references/situations.md](dk-system/references/situations.md)

| 編號 | 情境 | 建議指令 | 預期輸出 / 行為 |
|---|---|---|---|
| #01 | 全新專案（你是第一個 TPM） | `我接了一個新專案` | 啟動 Kickoff 逐題引導或提供會前問卷，產出 `logic_map/{project}_kickoff.md` |
| #02 | 全新專案但 PM 答案模糊 | `逐題引導` 或 要 PM 填 `dk-system/kickoff_full_questionnaire.md` | skill 用具體化技巧追問並補齊 Kickoff 資訊 |
| #03 | 接手有舊記錄 | `整合舊記錄`（上傳或貼內容） | 解析舊檔、匯入 `log.md`，並在 `report.md` 新增舊記錄摘要與需補課假設 |
| #04 | 前任離職、無紀錄 | `重建 Kickoff` | 發送最小必答問卷、生成最小版 `kickoff.md` 並輸出 onboarding checklist |
| #05 | 正常 Refine | `Refine 記要` | 把要點轉為需求候選並更新 `report.md` |
| #06 | 發現假設未驗證 | `標註需驗證` | 產出驗證任務樣板並加入 `log.md` |
| #07 | PO 與工程師意見分歧 | `生成討論摘要`（貼會議摘錄） | 產出決策選項比較表與風險建議，並在 `log.md` 建立待決事項 |
| #08 | 技術內容聽不懂 | `解釋這段`（貼摘錄） | 產生非技術化摘要與 2–3 個追問範本 |
| #09 | 會議未決事項 | `標註待決事項` | 把未決項加入 `log.md`，並在下次週報置頂提醒 |
| #10 | 工程師說做不到 | `評估替代方案`（貼上理由） | 生成技術限制摘要與 2–3 個替代方案（含估時/風險） |
| #11 | 主管問你問題需快速回覆 | `快速回覆主管：<問題>` | 從 `report.md`/`log.md` 擷取要點並回傳 2–3 句短回覆 |
| #12 | 報告中標注為「待確認」 | `列出待確認項` | 列出所有待確認條目並建議責任人與期限 |
| #13 | 報告缺此資訊 | `補資料：<問題>` | 生成追問清單或問卷以取得缺失資訊 |
| #14 | 工程師一直給技術答案 | `轉成決策選項`（貼技術內容） | 轉為 PM 可決策的選項，並列出對時程/成本/品質的影響 |
| #15 | 假設驗證錯誤但 PM 抵抗 | `生成風險與回退計畫` | 產出量化風險表、回退門檻與可操作步驟 |
| #16 | 專案中途被要求大改方向 | `評估變更影響`（貼變更摘要） | 產出變更影響快照，並生成新的 Kickoff 草案 |
| #17 | 你不在時有人做決定 | `同步變更`（貼記錄或 email） | 把變更摘要加入 `report.md` 並標註「他人代決」 |
| #18 | 同時負責多個專案、記錄混亂 | `整理我的專案清單` 或 `抽出專案 {project}` | 依標籤抽出條目、重建各專案 `log.md`，並產出 `overview.md` |
| #19 | 一個 bug 影響多專案 | `cross-project bug: <描述>` | 生成影響矩陣、跨專案通知範本，並記錄優先順序 |
| #20 | 假設被推翻引發連鎖反應 | `追蹤影響鏈 <假設ID或內容>` | 向上/下追溯依賴，列出受影響項目並產出修正清單 |
| #21 | Kickoff 訪談後建立初版 | `建立初版`（貼訪談筆記） | 生成 `kickoff.md`、`report.md` 與空白 `log.md` |
| #22 | 週五更新邏輯地圖 | `週報更新` | 把 `log.md` 合入 `report.md`，標註「本週更新」並清空 `log.md` |
| #23 | 新 PM onboarding | `匯出導覽版 {project}` | 產出 onboarding 摘要、關鍵待確認項與 30 分鐘議程 |
| #24 | 邏輯地圖太大難維護 | `精簡邏輯地圖 {project}` | 建議分割策略，並標註可移到歷史記錄的段落 |
| #25 | 資料 schema 頻繁變動 | `驗證 schema` 或 `schema 檢查` | 先執行 schema 驗證，若失敗標註「待確認」 |
| #26 | PO/PM 回覆延遲或不完整 | `收集最小必答項` 或 `補資料：<問題>` | 先整理最小必答欄位，會後把缺項標註並追蹤 |
| #27 | 採用率低（工程師拒用或不習慣） | `檢查 adoption` 或 `生成回退計畫` | 產出採用率檢查與回退條件，並建議示範與 early-adopter 支援 |
| #28 | 遺留系統可重用性不確定 | `評估遺留系統` | 分析介面與資料格式，判斷可重用性並納入 PoC 或排除 |
