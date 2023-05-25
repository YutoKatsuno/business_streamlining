import PyPDF2
# 特定のパターンにマッチするファイルを取得するモジュール
from glob import glob
# 自然順アルゴリズムでソートするモジュール
# 組み込みのsort()を使うと数字順に並ばない
import natsort

# 複数のPDFファイルを合体させる
merger = PyPDF2.PdfFileMerger()

files = glob("*ページ目.pdf")
files = natsort.natsorted(files)

for i in files:
    merger.append(i)

with open("merge.pdf", "wb") as merge_file:
    merger.write(merge_file)


