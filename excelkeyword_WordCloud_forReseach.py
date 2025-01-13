import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter

data = pd.read_excel('(路徑名)/result.xlsx')

# 必要欄位設定為這三欄，
# 原以z*z矩陣為主，但檔案會變很大，所以轉用另一種資料儲存方式。
if{'row', 'column', 'value'}.issubset(data.columns):
    print("Data contains required columns.")
else:
    raise ValueError("Input data must contain 'row', 'column', and 'value' columns.")
    
data['row'] = data['row'].fillna('').astype(str).str.strip()
data['column'] = data['column'].fillna('').astype(str).str.strip()
data['value'] = pd.to_numeric(data['value'], errors='coerce').fillna(0)

# 篩選條件：row 和 column 不為空，
# 條件限制：數值大於3才++
filtered_data = data[(data['row'] != '') & (data['column'] != '') & (data['value'] > 3)]

# 計數器
keyword_pairs = Counter()
for _, row in filtered_data.iterrows():
    if row['row'] == row['column']:     # if row和column相同，以"row"為主，只能這樣搞。
        keyword = row['row']
        keyword_pairs[keyword] += row['value']
        print(f"Single keyword added: {keyword}, Value: {row['value']}")
    else:
        # 一般情況，生成 "row - column" 組合
        pair = f"{row['row']} - {row['column']}"
        keyword_pairs[pair] += row['value']
        print(f"Pair added: {pair}, Value: {row['value']}")

# 檢查是否有符合條件的關鍵字組合，否則生成文字雲
if not keyword_pairs:
    print("No keyword > 3, Exiting.")
else:
    wordcloud = WordCloud(
        width=800, height=400,
        background_color='white',
        colormap='viridis'
    ).generate_from_frequencies(keyword_pairs)

    # 文字雲的設定
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Keyword Word Cloud", fontsize=15)
    plt.show()
    output_file = 'wordcloud.png'
    wordcloud.to_file(output_file)
    print(f"save as {output_file}")
