import pyautogui

fw = pyautogui.getActiveWindow() #現在、活性化しているプログラム

# print(fw.title) #プログラムのタイトル情報
# print(fw.size) #プログラムのサイズ情報(width, height)
# print(fw.left, fw.top, fw.right, fw.bottom) #プログラムの位置情報
# pyautogui.click(fw.left + 30, fw.top + 20)

# for w in pyautogui.getAllWindows():
#         print(w)

w = pyautogui.getWindowsWithTitle("제목 없음")[0]
print(w)
if w.isActive == False: # 現在、活性化されてないなら、
    w.activate() # 活性化(一番前に持ってくる)

if w.isMaximized == False: # 現在、最大化されてないなら、
    w.maximize() #最大化

pyautogui.sleep(1)

# if w.isMinimized == False:　# 現在、最小化されてないなら
#     w.minimize()　# 最小化

w.restore() #画面を元に戻す。

w.close() # winodwsを消す