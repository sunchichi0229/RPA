import pyautogui
# pyautogui.FAILSAFE = FALSE #あんまり使用しない方がいい　強制終了を防ぐ機能
# pyautogui.PUASE = 1 #すべての動作に１秒ずつsleepを適用
# pyautogui.mouseInfo() #マウスの情報を見る機能

for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)