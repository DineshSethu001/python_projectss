#pillow and pyAutoGui required
from unicodedata import name
import pyautogui
import time
import tkinter as tk


def screen_app():
    time.sleep(5)
    name=time.time()
    name="F:/python/screenshotApplication/{}.png".format(name)
    img=pyautogui.screenshot()
    img.save(name)
    img.show()

screen_app()