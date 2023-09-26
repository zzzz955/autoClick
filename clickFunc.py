import time
import pyautogui


def click_start(interval):
    x, y = pyautogui.position()
    while 1:
        pyautogui.click(x, y)
        time.sleep(interval)

