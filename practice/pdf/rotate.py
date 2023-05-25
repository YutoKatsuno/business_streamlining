import PyPDF2

with open("covid19.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)

    page = reader.getPage(0)
    # 回転させる
    rotate = page.rotateClockwise(90)

    with open("rotate.pdf", "wb") as rotate_page:
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(rotate)
        writer.write(rotate_page)