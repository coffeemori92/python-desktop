import pyautogui

pyautogui.moveTo(100, 100) # 지정한 위치로 마우스를 이동
pyautogui.moveTo(100, 200)
pyautogui.moveTo(100, 300)
pyautogui.moveTo(100, 200, duration=0.25)

# 상대 좌표로 이동
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())
pyautogui.move(100, 100, duration=0.25)
print(pyautogui.position())

p = pyautogui.position()
print(p[0], p[1])
print(p.x, p.y)