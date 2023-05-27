import pyautogui
import time

# ファイルを作成する
pyautogui.moveTo(x=658, y=869)
pyautogui.click()
pyautogui.write("touch new.py")
pyautogui.press("enter")


# 3秒待機する
time.sleep(3)

# ファイルを削除する
pyautogui.write("rm new.py")
pyautogui.press("enter")
print(pyautogui.position())
