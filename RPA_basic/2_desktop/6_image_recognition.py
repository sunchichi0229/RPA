import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu, duration = 1)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):
#     print(i)
#     pyautogui.click(i, duration=0.25)

#速度改善
# 1. GrayScale
# file_menu = pyautogui.locateOnScreen("file_menu.png", grayscale=True)
# pyautogui.moveTo(file_menu)

# 2. 範囲指定
# file_menu = pyautogui.locateOnScreen("file_menu.png", region=x, y, width, height)
# pyautogui.moveTo(file_menu)

# 3.正確度測定
run_btn = pyautogui.locateOnScreen("run_button.png", confidence=0.9)
pyautogui.moveTo(run_btn)