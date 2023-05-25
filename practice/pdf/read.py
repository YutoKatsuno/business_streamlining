# PyPDF2-1.26.0
import PyPDF2

# モードbはテキストファイル以外の場合に指定する
with open("covid19.pdf", "rb") as file:

    # PyPDF2で使える形式でPDFファイルを読み込む
    reader = PyPDF2.PdfFileReader(file)

    # 読み込んだPDFファイルのページ数
    print(reader.numPages)
    # 指定したページを取得する
    print(reader.getPage(0))
