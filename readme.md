
- 主程式架構：
    - ETL：
        - extract.py：從 Elasticsearch 開發機取得團資料，並將其儲存為 JSON 檔案
        - transform.py：從 JSON 檔案中讀取團資料，將部分欄位轉換為向量，並將資料儲存到 Elasticsearch
        - settings.py：Elasticsearch 的 index mapping 設定

    - API：
        - controller → group_ctrl.py ：主要的判斷邏輯
        - route.py：API的URI
        - model.py：API傳入參數
        - settings.py：存放LLM prompts

    - Front end：
        - html template

- 模型：
    - embedding：infgrad/stella-mrl-large-zh-v3.5-1792d
    - LLM：ollama API (gemma2:27b)


- 流程細節：
  ```txt
    ES資料庫 → 獲取資訊 → enbedding → 向量儲存(dense vector) → 混和搜尋(hybrid search) → Elasticsearch → result
                            ↓
                           LLM
                            ↓
                      萃取、過濾關鍵字
  ```
  
