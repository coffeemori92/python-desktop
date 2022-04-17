import pyautogui
import pyperclip

w = pyautogui.getWindowsWithTitle('제목 없음')[0]
w.activate()
print(w)

# pyautogui.write('1 2 3 4 5 ')
# pyautogui.write('NadoCoding', interval=0.25)

pyautogui.write(['t', 'e', 's', 't', 'left', 'left', 'right'])

# pyperclip.copy('나도 코딩')
# pyautogui.hotkey('ctrl', 'v')

def my_write(text):
  pyperclip.copy(text)
  pyautogui.hotkey('ctrl', 'v')

my_write('코딩')
