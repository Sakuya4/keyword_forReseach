import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

# 讀取 Excel 檔案
data = pd.read_excel('D:/輔大RA/第二階段/完成/文字雲/result.xlsx')

# 確保資料中包含必要的欄位
if {'row', 'column', 'value'}.issubset(data.columns):
    print("Data contains required columns.")
else:
    raise ValueError("Input data must contain 'row', 'column', and 'value' columns.")

# 清理資料：移除 NaN 和空字串
data['row'] = data['row'].fillna('').astype(str).str.strip()
data['column'] = data['column'].fillna('').astype(str).str.strip()
data['value'] = pd.to_numeric(data['value'], errors='coerce').fillna(0)

# 篩選條件：row 和 column 不為空，且 value > 3
filtered_data = data[(data['row'] != '') & (data['column'] != '') & (data['value'] > 3)]

# 計算關鍵字組合頻率，考慮特殊情況
keyword_pairs = Counter()
for _, row in filtered_data.iterrows():
    if row['row'] == row['column']:
        # 若 row 和 column 相同，直接用 row 作為關鍵字
        keyword = row['row']
        keyword_pairs[keyword] += row['value']
        print(f"Single keyword added: {keyword}, Value: {row['value']}")
    else:
        # 一般情況，生成 "row - column" 組合
        pair = f"{row['row']} - {row['column']}"
        keyword_pairs[pair] += row['value']
        print(f"Pair added: {pair}, Value: {row['value']}")

# 檢查是否有符合條件的關鍵字組合
if not keyword_pairs:
    print("No keyword pairs found with value > 3. Exiting.")
else:
    # 生成文字雲
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        colormap='viridis'
    ).generate_from_frequencies(keyword_pairs)

    # 顯示文字雲
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Keyword Co-occurrence Word Cloud (Value > 3)", fontsize=15)
    plt.show()

    # 保存文字雲圖片
    output_file = 'wordcloud_with_single_keywords.png'
    wordcloud.to_file(output_file)
    print(f"Word cloud saved to {output_file}")
