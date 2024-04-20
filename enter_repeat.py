import pyautogui
import time

# 엔터키를 누르는 함수
def press_enter():
    pyautogui.press('enter')

# 1초 간격으로 엔터키를 누르는 함수 반복 실행
while True:
    press_enter()
    time.sleep(0.5)





