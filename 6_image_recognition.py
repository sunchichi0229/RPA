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
# run_btn = pyautogui.locateOnScreen("run_button.png", confidence=0.9)
# pyautogui.moveTo(run_btn)

# 1. 待ち続ける
# file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
# if file_menu_notepad:
#     pyautogui.click(file_menu_notepad)
# else:
#     print("発見失敗")

# 2. 一定の時間の間、待ち続ける(TimeOut)
import time
import sys

# timeout = 10 #10秒待機
# start = time.time() #start時間設定
# file_menu_notepad = None
# while file_menu_notepad is None:
#     file_menu_notepad = pyautogui.locateOnScreen("file_menu_notepad.png")
#     end = time.time()
#     if end - start > timeout: #指定した１０秒を過ぎたら
#         print("タイムオーバー")
#         sys.exit()

# pyautogui.click(file_menu_notepad)

def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout:
            break
    return target

def my_click(img_file, timeout = 30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program.")
        sys.exit()

my_click("file_menu_notepad.png, 10")