import pyautogui

# pyautogui.moveTo(200, 200) #決めた場所にマウスが移動

# pyautogui.moveTo(300, 400, duration=3) #3秒の間。300,400の位置に移動。
# pyautogui.moveTo(600, 800, duration=3) 
# pyautogui.moveTo(1000, 500, duration=3) 


# 基準位置からマウスの移動(現在位置が基準になり、移動)
pyautogui.moveTo(100, 100, duration=2)
print(pyautogui.position()) # Point(x, y)
pyautogui.move(200, 300, duration=2) # 100, 100を基準に　+200 , +300
print(pyautogui.position())
pyautogui.move(700, 400, duration=2)
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1]) # x, y
print(p.x, p.y) # x, y