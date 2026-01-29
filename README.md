# Browser-Agent-Tasks100

ブラウザ操作を評価するためのタスクベンチマークです。

## 生成方法

```bash
python generate_tasks.py
```

`tasks.jsonl` は上記スクリプトで再生成されます。

## タスクフォーマット

各行が1タスクのJSONです。

- `task_id`: 連番ID
- `category`: カテゴリ名
- `start_url`: 開始URL
- `intent`: 実行してほしい指示文
- `difficulty`: 想定難易度 (`easy` / `medium` / `hard`)
- `success_criteria`: 成功条件のチェックポイント
