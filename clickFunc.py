import time
import pyautogui
from PyQt5.QtCore import Qt


class click_Func:
    def __init__(self):
        self.roof = None

    def key_pressed(self, key):
        if key == Qt.Key_F3:
            self.roof = True
            self.click_start(1)
        if key == Qt.Key_F4:
            self.roof = False

    def click_start(self, interval):
        x, y = pyautogui.position()

        while self.roof:
            pyautogui.click(x, y)
            time.sleep(interval)

