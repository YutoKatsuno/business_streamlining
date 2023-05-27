import pyautogui


# 指定した画像と一致する場所の座標を取得
# confidenceを指定すると、100%一致ではなくても結果が返ってくる
x, y = pyautogui.locateCenterOnScreen("icon.png", confidence=0.9)
print(x, y)
x, y = pyautogui.position()
print(x*2, y*2)