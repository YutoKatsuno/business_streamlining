import pyautogui
import pyperclip
import time

# 全画面表示を終了
pyautogui.moveTo(x=42, y=8)
pyautogui.moveTo(x=54, y=39)
pyautogui.click()
time.sleep(2)

# エクセルを開く
pyautogui.moveTo(x=80, y=168)
pyautogui.rightClick()
pyautogui.moveTo(x=172, y=178)
pyautogui.click()
time.sleep(2)

# 入力
pyautogui.moveTo(x=153, y=243)
pyautogui.click()
pyperclip.copy("テスト")
pyautogui.hotkey("command", "v")

# 保存
pyautogui.hotkey("command", "s")

# 削除
pyautogui.moveTo(x=29, y=40)
pyautogui.click()
