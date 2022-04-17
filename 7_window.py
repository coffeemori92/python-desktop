import pyautogui

fw = pyautogui.getActiveWindow() # 현재 활성화된 창
print(fw.title) # 창의 제목
print(fw.size)

# for w in pyautogui.getAllWindows():
#   print(w)

w = pyautogui.getWindowsWithTitle('제목 없음')[0]
print(w)
if w.isActive == False:
  w.activate()

if w.isMaximized == False:
  w.maximize()

pyautogui.sleep(3)

w.restore()
w.close()
