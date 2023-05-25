# PyPDFでもテキスト抽出できるが、日本語には対応していない
from pdfminer.high_level import extract_text
import PyPDF2

# 指定したファイルのテキストデータを取得する
text = extract_text("3ページ目.pdf")
print(text)
# 特定の文字列の最初の文字のインデックスを返す
index = text.find("重症化した人の割合は ")
print(text[index:index+10])

# with open("covid19.pdf", "rb") as file:
#     reader = PyPDF2.PdfFileReader(file)
#
#     with open("3ページ目.pdf", "wb") as new_file:
#         writer = PyPDF2.PdfFileWriter()
#         writer.addPage(reader.getPage(2))
#         writer.write(new_file)
