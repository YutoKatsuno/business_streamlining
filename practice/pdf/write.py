import PyPDF2

with open("covid19.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    total_pages = reader.numPages

    for i in range(total_pages):
        with open(f"{i + 1}ページ目.pdf", "wb") as new_file:
            writer = PyPDF2.PdfFileWriter()
            # 書き込みたいページを受け取る
            writer.addPage(reader.getPage(i))
            # 指定したファイルに書き込む
            writer.write(new_file)
