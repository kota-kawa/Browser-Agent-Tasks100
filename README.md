# Browser-Agent-Tasks100

ブラウザ操作を評価するためのタスクベンチマークです。

## 使い方（詳細）

### 1. 前提条件

- Python 3.8 以降がインストールされていること
- 本リポジトリをローカルに取得していること

### 2. セットアップ

このリポジトリは追加の依存関係がなく、標準の Python だけで動作します。

### 3. タスクの生成

以下のコマンドでタスク一覧を再生成できます。

```bash
python generate_tasks.py
```

実行すると、同階層にある `tasks.jsonl` が生成（または上書き）されます。

### 4. 出力ファイルの確認

`tasks.jsonl` は JSON Lines 形式（1行=1タスク）で保存されます。例えば先頭数行は以下のような形になります。

```bash
head -n 3 tasks.jsonl
```

```json
{"task_id": 1, "category": "...", "start_url": "...", "intent": "...", "difficulty": "easy", "success_criteria": ["..."]}
```

### 5. ベンチマークの使い方

1. `tasks.jsonl` から評価したいタスクを選びます。
2. `start_url` にアクセスし、`intent` を満たす操作をエージェントに実行させます。
3. 実行結果が `success_criteria` を満たしているかを確認します。
4. タスクごとの成否や所要時間など、評価指標を記録します。

上記の流れをタスク集合に対して繰り返すことで、ブラウザ操作エージェントの性能を比較できます。

## 補足: 再生成時の注意

- `tasks.jsonl` は毎回上書きされるため、編集した内容がある場合は事前にバックアップしてください。

## タスクフォーマット

各行が1タスクのJSONです。

- `task_id`: 連番ID
- `category`: カテゴリ名
- `start_url`: 開始URL
- `intent`: 実行してほしい指示文
- `difficulty`: 想定難易度 (`easy` / `medium` / `hard`)
- `success_criteria`: 成功条件のチェックポイント
