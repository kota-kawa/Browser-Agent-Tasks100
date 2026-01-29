import json
import random

categories = {
    "shopping": [
        {"url": "https://www.amazon.co.jp", "templates": [
            "{item}を検索して、一番安いものをカートに入れてください。",
            "{item}のレビューが星4以上の商品を探して、そのURLを教えてください。",
            "{budget}円以下で{item}を探してください。"
        ]},
        {"url": "https://www.rakuten.co.jp", "templates": [
            "{item}を検索し、ランキング1位の商品詳細ページを開いてください。",
            "{item}の送料無料の商品を探してください。"
        ]}
    ],
    "information": [
        {"url": "https://www.google.co.jp", "templates": [
            "{query}について調べて、結果を要約してください。",
            "{person}の生年月日を調べてください。",
            "{city}の明日の天気を調べてください。",
            "{company}の株価を調べてください。"
        ]},
        {"url": "https://ja.wikipedia.org", "templates": [
            "{topic}のページを開き、概要の最初の段落を読んでください。",
            "{history_event}について書かれているセクションを探してください。"
        ]}
    ],
    "travel": [
        {"url": "https://www.booking.com", "templates": [
            "{city}のホテルを{date}から1泊で検索してください。",
            "{city}にある評価が8以上のホテルを探してください。"
        ]},
        {"url": "https://www.jalan.net", "templates": [
            "{onsen}温泉の宿を検索してください。"
        ]}
    ],
    "productivity": [
        {"url": "https://translate.google.co.jp", "templates": [
            "「{phrase}」を英語に翻訳してください。",
            "「{phrase}」をフランス語に翻訳してください。"
        ]},
        {"url": "https://www.youtube.com", "templates": [
            "{video_topic}の動画を検索して、一番上の動画を再生してください。",
            "{youtuber}のチャンネルを開いてください。"
        ]}
    ]
}

items = ["ワイヤレスイヤホン", "ゲーミングマウス", "USB-Cケーブル", "スマートフォンケース", "コーヒーメーカー", "ランニングシューズ", "バックパック", "4Kモニター", "メカニカルキーボード", "空気清浄機"]
budgets = ["1000", "3000", "5000", "10000", "50000"]
queries = ["最新のAIニュース", "東京のおすすめラーメン", "Pythonの学習方法", "近くのジム", "円安の影響"]
people = ["大谷翔平", "イーロン・マスク", "岸田文雄", "テイラー・スウィフト", "宮崎駿"]
cities = ["東京", "大阪", "京都", "札幌", "福岡", "那覇", "ニューヨーク", "パリ"]
dates = ["来週の土曜日", "12月25日", "ゴールデンウィーク", "明日"]
onsens = ["草津", "箱根", "別府", "有馬", "下呂"]
topics = ["量子コンピュータ", "ルネサンス", "ブラックホール", "光合成", "第二次世界大戦"]
history_events = ["明治維新", "フランス革命", "アポロ11号", "ベルリンの壁崩壊"]
companies = ["トヨタ自動車", "ソニー", "任天堂", "Apple", "Google"]
phrases = ["こんにちは、元気ですか？", "この電車は新宿に行きますか？", "お会計をお願いします。", "駅はどこですか？"]
video_topics = ["猫 おもしろ", "料理 レシピ", "ヨガ 初心者", "マインクラフト 実況", "テックニュース"]
youtubers = ["HIKAKIN", "はじめしゃちょー", "東海オンエア"]

def generate_task(task_id):
    category_name = random.choice(list(categories.keys()))
    site = random.choice(categories[category_name])
    template = random.choice(site["templates"])

    # Fill template
    intent = template
    if "{item}" in intent: intent = intent.replace("{item}", random.choice(items))
    if "{budget}" in intent: intent = intent.replace("{budget}", random.choice(budgets))
    if "{query}" in intent: intent = intent.replace("{query}", random.choice(queries))
    if "{person}" in intent: intent = intent.replace("{person}", random.choice(people))
    if "{city}" in intent: intent = intent.replace("{city}", random.choice(cities))
    if "{company}" in intent: intent = intent.replace("{company}", random.choice(companies))
    if "{date}" in intent: intent = intent.replace("{date}", random.choice(dates))
    if "{topic}" in intent: intent = intent.replace("{topic}", random.choice(topics))
    if "{history_event}" in intent: intent = intent.replace("{history_event}", random.choice(history_events))
    if "{onsen}" in intent: intent = intent.replace("{onsen}", random.choice(onsens))
    if "{phrase}" in intent: intent = intent.replace("{phrase}", random.choice(phrases))
    if "{video_topic}" in intent: intent = intent.replace("{video_topic}", random.choice(video_topics))
    if "{youtuber}" in intent: intent = intent.replace("{youtuber}", random.choice(youtubers))

    return {
        "task_id": task_id,
        "category": category_name,
        "start_url": site["url"],
        "intent": intent
    }

tasks = []
for i in range(100):
    tasks.append(generate_task(i))

with open("tasks.jsonl", "w", encoding="utf-8") as f:
    for task in tasks:
        f.write(json.dumps(task, ensure_ascii=False) + "\n")

print("Generated 100 tasks in tasks.jsonl")
