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

root=tk.Tk()
frame=tk.Frame(root)
frame.pack()

button=tk.Button(frame,text="Take ScreenShot",command=screen_app)
button.pack(side=tk.LEFT)

close=tk.Button(frame,text="quit",command=quit)
close.pack(side=tk.LEFT)

root.mainloop()