import os
import pandas as pd
import openai
from time import sleep

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_prompt(description):
    prompt = f"""
請將以下食品描述歸類為以下飲食組別之一：
- 蛋豆魚肉類
- 全穀雜糧類
- 蔬菜類
- 水果類
- 乳品類
- 油脂與堅果種子類
- 飲料類
- 調味料與醬料類
- 加工食品類
- 零食類
- 餐廳/快餐類
- 其他

以下是除了基礎六大類的細部說明，盡可能讓每一筆資料都屬於一個類別，『其他類別』是逼不得已真的無法分類時再使用：
- 飲料類（含含糖飲料、果汁、茶、酒精飲料）
- 調味料與醬料類（沙拉醬、醬汁、醃製品）
- 加工食品類（甜點、糕點、餅乾、速食、冷凍餐點）
- 零食類（薯片、爆米花、糖果等零嘴）
- 餐廳/快餐類（餐廳供應的複合料理）

食品描述："{description}"

請直接回覆分類名稱，字詞必須完整且精確。
"""
    return prompt

def classify_food_group(description, max_retry=3):
    prompt = create_prompt(description)
    retries = 0
    while retries < max_retry:
        try:
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "你是一個專業的食品分類助理。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=20,
            )
            label = response.choices[0].message.content.strip()
            return label
        except Exception as e:
            print(f"錯誤: {e}，重試 {retries+1}/{max_retry} ...")
            retries += 1
            sleep(2)
    return "未知"

df = pd.read_csv("test.csv")

labels = []
total = len(df)
for idx, row in df.iterrows():
    print(f"處理第 {idx+1}/{total} 筆: {row['Descrip'][:30]}...")
    label = classify_food_group(row['Descrip'])
    print(f"分類結果: {label}")
    labels.append(label)
    sleep(1)  # API速率限制

df['Diet_Group'] = labels
df.to_csv("test_labeled.csv", index=False)
print("標註完成，結果已存檔為 test_labeled.csv")