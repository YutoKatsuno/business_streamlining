import pyautogui
import pyperclip

# キーボードの操作

# 入力したい文字列を渡す(日本語には対応してない)
pyautogui.click()
pyautogui.write("test")

# 日本語で入力したい場合
pyautogui.click()
pyperclip.copy("テスト")
pyautogui.hotkey("command", "v")

# １つのキーを指定
pyautogui.press("enter")
# 複数キーを指定
pyautogui.hotkey("command", "v")
