import pyautogui
#screenshot撮る
img = pyautogui.screenshot()
img.save("screenshot.png") #ファイルでsave

pixel = pyautogui.pixel(28, 18)
print(pixel)

print(pyautogui.pixelMatchesColor(28, 18, (34, 167, 242)))