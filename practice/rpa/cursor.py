import pyautogui

# カーソルの操作

# 指定した場所にマウスカーソルが移動する
pyautogui.moveTo(x=100, y=100, duration=10)


# ドラッグする方法
# 左クリックを長押し
pyautogui.mouseDown()
# 今のカーソルの場所からどこまで移動させるか
pyautogui.moveRel(100, 0, duration=1)
# 左クリックを止める
pyautogui.mouseUp()
