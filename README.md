# keyword_forReseach
研究助理時期使用Code
之前也有一些，但全刪了，為了知道自己做了什麼，所以要將Code做保存，
未來離職也會比較有個概念以前的工作。


## 1. 產生文字雲
  1. 事前工作，將z*z矩陣轉換成另一種方式表現。
  2. 引用Library: pandas, wordcloud, matplotlib.pyplot, collections.Counter.
  3. 讀檔案、檢查必要欄位('row', 'column', 'value')   // value for keyword 出現之次數
  4. 資料清理：row 和 column 欄位填補空值為空字串（''），移除多餘空白，確保值為字串格式。
     value 欄位：強制轉換為數字類型，若轉換失敗則設為 0。這一步確保資料格式正確，方便後續操作。
  5. 篩選資料並且計算：超過 >3才++。
  6. 設定並生成文字雲。
     

```
1. Import required libraries (pandas, wordcloud, matplotlib, collections).
2. Load data from the specified Excel file.
3. Check if the data contains necessary columns ('row', 'column', 'value').
4. Clean the data:
   a. Remove NaN and trim spaces in 'row' and 'column'.
   b. Convert 'value' to numeric, filling invalid values with 0.
5. Filter the data:
   a. Include only rows where 'row' and 'column' are non-empty and 'value' > 3.
6. Initialize a Counter to store keyword frequencies.
7. Loop through the filtered data:
   a. If 'row' equals 'column', count it as a single keyword.
   b. Otherwise, treat it as a keyword pair ('row - column').
8. If no keywords meet the conditions, exit the program.
9. Generate a word cloud from the keyword frequencies.
10. Display the word cloud using matplotlib.
11. Save the word cloud as a PNG file.

```
