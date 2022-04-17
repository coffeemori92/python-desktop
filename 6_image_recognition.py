import pyautogui
import time
import sys

# file_menu = pyautogui.locateOnScreen('file_menu.png')
# print(file_menu)

# pyautogui.click(file_menu)

terminal_menu = pyautogui.locateOnScreen('terminal_menu.png')
pyautogui.click(terminal_menu)

pyautogui.sleep(0.25)

# trash_icon = pyautogui.locateOnScreen('trash_icon.png')
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen('trash_icon.png', grayscale=True)
# pyautogui.moveTo(trash_icon)

# 2. 범위지정
trash_icon = pyautogui.locateOnScreen(
  'trash_icon.png', region=(1648, 726, 1903 - 1648, 841))
pyautogui.moveTo(trash_icon)

# 3. 정확도 조정
run_button = pyautogui.locateOnScreen('run_button.png', confidence=0.7)
pyautogui.moveTo(run_button)

# 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
# file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
# while file_menu_notepad is None:
#   file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
# pyautogui.moveTo(file_menu_notepad)

# 2. 일정 시간동안 기다리기 (TimeOut)
# timeout = 10
# start = time.time()
# file_menu_notepad = None
# while file_menu_notepad is None:
#   file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
#   end = time.time()
#   if (end - start > timeout):
#     print('timeout')
#     sys.exit()

def find_target(img_file, timeout=30):
  start = time.time()
  taregt = None
  while taregt is None:
    taregt = pyautogui.locateOnScreen(img_file)
    end = time.time()
    if (end - start > timeout):
      break
  return taregt

def my_move(img_file, timeout=30):
  target = find_target(img_file, timeout)
  if target:
    pyautogui.moveTo(target)
  else:
    print(f'[Timeout {timeout}s] Target not found ({img_file})')
    print('Terminate program')
    sys.exit()

my_move('file_menu_notepad.png', 10)
