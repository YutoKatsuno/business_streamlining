# PyPDFでもテキスト抽出できるが、日本語には対応していない
from pdfminer.high_level import extract_text

# 指定したファイルのテキストデータを取得する
text = extract_text("3ページ目.pdf")
print(text)
# 特定の文字列の最初の文字のインデックスを返す
index = text.find("重症化した人の割合は ")
print(text[index:index+10])
