import pyautogui
w = pyautogui.getWindowsWithTitle("제목 없음")[0]
w.activate()

# pyautogui.write("123456")
# pyautogui.write("sunchichi", interval=1)

# pyautogui.write("t","e","s","t","left","left","right","l","a","enter", interval=0.25)

#特殊文字
#shift + 4 = $

# pyautogui.keyDown("shift") #shiftキーを押した状態
# pyautogui.press("4") #数字４を押す
# pyautogui.keyUp("shift") #shiftキーを離す

#簡単切り替えキー
# pyautogui.hotkey("ctrl","art","shift","a")
#Ctrl押して＞Alt押して＞Shift押して＞A押して＞A離して＞Shift離して＞Alt離して＞Ctrl離す

import pyperclip
# pyperclip.copy("승치치") #"승치치"文字をクリップボードにＳave
# pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl","v")

my_write("승치치")

#自動化プログラム終了
# win : ctrl + alt + del
# mac : cmd + shift + option + q