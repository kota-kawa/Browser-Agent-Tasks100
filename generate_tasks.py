import json
import random

categories = {
    "shopping": [
        {
            "url": "https://www.amazon.co.jp",
            "templates": [
                {
                    "text": "{item}を検索し、価格が{budget}円以下かつレビュー評価が星{rating}以上の商品を1つ選び、商品名と価格を答えてください。",
                    "difficulty": "hard",
                    "success_criteria": "条件(価格{budget}円以下、評価星{rating}以上)を満たす商品名と価格が提示されている。",
                },
                {
                    "text": "{item}を検索して、配送予定日が最短の商品の商品ページを開き、配送予定日を報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "配送予定日が最短の商品ページを開き、配送予定日を提示している。",
                },
                {
                    "text": "{item}を検索し、色が{color}のバリエーションを選択して価格を確認してください。",
                    "difficulty": "medium",
                    "success_criteria": "{color}のバリエーションを選択した状態で価格が示されている。",
                },
            ],
        },
        {
            "url": "https://www.rakuten.co.jp",
            "templates": [
                {
                    "text": "{item}を検索し、ランキング上位3件のうち最安の商品ページを開いて価格を教えてください。",
                    "difficulty": "hard",
                    "success_criteria": "ランキング上位3件の比較が行われ、最安の価格が示されている。",
                },
                {
                    "text": "{item}の送料無料かつレビュー件数が{review_count}件以上の商品を1つ見つけ、商品名とURLを教えてください。",
                    "difficulty": "hard",
                    "success_criteria": "送料無料かつレビュー件数{review_count}件以上の商品名とURLが示されている。",
                },
            ],
        },
    ],
    "information": [
        {
            "url": "https://www.google.co.jp",
            "templates": [
                {
                    "text": "{query}について調べ、信頼できる情報源を2つ以上見つけて要点を3つにまとめてください。",
                    "difficulty": "hard",
                    "success_criteria": "2つ以上の情報源に言及し、要点が3つに整理されている。",
                },
                {
                    "text": "{person}の生年月日を調べ、情報元のサイト名もあわせて報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "生年月日と参照したサイト名が示されている。",
                },
                {
                    "text": "{city}の明日の天気を調べ、降水確率と最高気温を報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "降水確率と最高気温が示されている。",
                },
                {
                    "text": "{company}の株価(現在値)を調べ、前日比もあわせて報告してください。",
                    "difficulty": "hard",
                    "success_criteria": "現在値と前日比が提示されている。",
                },
            ],
        },
        {
            "url": "https://ja.wikipedia.org",
            "templates": [
                {
                    "text": "{topic}のページを開き、概要の最初の段落を要約してください。",
                    "difficulty": "medium",
                    "success_criteria": "概要の最初の段落が要約されている。",
                },
                {
                    "text": "{history_event}について書かれているセクションを探し、その見出しと要点を2つ挙げてください。",
                    "difficulty": "hard",
                    "success_criteria": "該当セクションの見出しと2つの要点が示されている。",
                },
            ],
        },
    ],
    "travel": [
        {
            "url": "https://www.booking.com",
            "templates": [
                {
                    "text": "{city}のホテルを{date}から1泊で検索し、評価が{rating}以上で最安のホテル名と価格を教えてください。",
                    "difficulty": "hard",
                    "success_criteria": "評価{rating}以上の中で最安のホテル名と価格が示されている。",
                },
                {
                    "text": "{city}で朝食付きプランのホテルを探し、最初に表示されたホテルの名前を報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "朝食付きの条件で検索し、最初に表示されたホテル名が示されている。",
                },
            ],
        },
        {
            "url": "https://www.jalan.net",
            "templates": [
                {
                    "text": "{onsen}温泉の宿を検索し、評価が{rating}以上の宿を1つ選び、その宿名と評価を報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "評価{rating}以上の宿名と評価が示されている。",
                },
                {
                    "text": "{onsen}温泉の宿で、{budget}円以下のプランを探してプラン名を報告してください。",
                    "difficulty": "hard",
                    "success_criteria": "{budget}円以下のプラン名が示されている。",
                },
            ],
        },
    ],
    "productivity": [
        {
            "url": "https://translate.google.co.jp",
            "templates": [
                {
                    "text": "「{phrase}」を{language}語に翻訳し、翻訳結果を報告してください。",
                    "difficulty": "easy",
                    "success_criteria": "{language}語への翻訳結果が示されている。",
                },
                {
                    "text": "「{phrase}」を英語に翻訳したうえで、丁寧表現になっているか確認してください。",
                    "difficulty": "medium",
                    "success_criteria": "英語翻訳結果が示され、丁寧表現かどうかの判断がある。",
                },
            ],
        },
        {
            "url": "https://www.youtube.com",
            "templates": [
                {
                    "text": "{video_topic}の動画を検索し、再生回数が最も多い動画のタイトルと再生回数を報告してください。",
                    "difficulty": "hard",
                    "success_criteria": "検索結果から再生回数が最大の動画を特定し、タイトルと再生回数が示されている。",
                },
                {
                    "text": "{youtuber}のチャンネルを開き、最新動画のタイトルを報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "チャンネルの最新動画タイトルが示されている。",
                },
            ],
        },
    ],
    "maps": [
        {
            "url": "https://www.google.com/maps",
            "templates": [
                {
                    "text": "{city}駅周辺で評価が{rating}以上の{place_type}を検索し、最初に表示された店舗名と評価を報告してください。",
                    "difficulty": "hard",
                    "success_criteria": "評価{rating}以上の{place_type}を検索し、最初の店舗名と評価が示されている。",
                },
                {
                    "text": "{city}から{near_city}までの公共交通機関のルートを調べ、所要時間を報告してください。",
                    "difficulty": "medium",
                    "success_criteria": "公共交通機関ルートの所要時間が示されている。",
                },
            ],
        }
    ],
}

placeholders = {
    "item": [
        "ワイヤレスイヤホン",
        "ゲーミングマウス",
        "USB-Cケーブル",
        "スマートフォンケース",
        "コーヒーメーカー",
        "ランニングシューズ",
        "バックパック",
        "4Kモニター",
        "メカニカルキーボード",
        "空気清浄機",
        "外付けSSD",
        "Bluetoothスピーカー",
    ],
    "budget": ["1000", "3000", "5000", "10000", "20000", "50000"],
    "rating": ["3.5", "4.0", "4.2", "4.5"],
    "color": ["黒", "白", "青", "赤"],
    "review_count": ["50", "100", "300", "500"],
    "query": [
        "最新のAIニュース",
        "東京のおすすめラーメン",
        "Pythonの学習方法",
        "近くのジム",
        "円安の影響",
        "生成AIの倫理的課題",
    ],
    "person": ["大谷翔平", "イーロン・マスク", "岸田文雄", "テイラー・スウィフト", "宮崎駿"],
    "city": ["東京", "大阪", "京都", "札幌", "福岡", "那覇", "ニューヨーク", "パリ"],
    "near_city": ["横浜", "神戸", "名古屋", "大宮", "千葉"],
    "date": ["来週の土曜日", "12月25日", "ゴールデンウィーク", "明日"],
    "onsen": ["草津", "箱根", "別府", "有馬", "下呂"],
    "topic": ["量子コンピュータ", "ルネサンス", "ブラックホール", "光合成", "第二次世界大戦"],
    "history_event": ["明治維新", "フランス革命", "アポロ11号", "ベルリンの壁崩壊"],
    "company": ["トヨタ自動車", "ソニー", "任天堂", "Apple", "Google"],
    "phrase": [
        "こんにちは、元気ですか？",
        "この電車は新宿に行きますか？",
        "お会計をお願いします。",
        "駅はどこですか？",
    ],
    "video_topic": ["猫 おもしろ", "料理 レシピ", "ヨガ 初心者", "マインクラフト 実況", "テックニュース"],
    "youtuber": ["HIKAKIN", "はじめしゃちょー", "東海オンエア"],
    "language": ["英", "フランス", "ドイツ", "スペイン"],
    "place_type": ["カフェ", "レストラン", "書店", "美術館"],
}


def build_replacements(*texts):
    combined_text = "".join(texts)
    replacements = {}
    for key, options in placeholders.items():
        token = "{" + key + "}"
        if token in combined_text:
            replacements[key] = random.choice(options)
    return replacements


def apply_replacements(text, replacements):
    for key, value in replacements.items():
        text = text.replace("{" + key + "}", value)
    return text


def generate_task(task_id):
    category_name = random.choice(list(categories.keys()))
    site = random.choice(categories[category_name])
    template = random.choice(site["templates"])

    replacements = build_replacements(template["text"], template["success_criteria"])
    intent = apply_replacements(template["text"], replacements)
    success_criteria = apply_replacements(template["success_criteria"], replacements)

    return {
        "task_id": task_id,
        "category": category_name,
        "start_url": site["url"],
        "intent": intent,
        "difficulty": template["difficulty"],
        "success_criteria": success_criteria,
    }


tasks = []
for i in range(100):
    tasks.append(generate_task(i))

with open("tasks.jsonl", "w", encoding="utf-8") as f:
    for task in tasks:
        f.write(json.dumps(task, ensure_ascii=False) + "\n")

print("Generated 100 tasks in tasks.jsonl")
