import pyautogui as pgui
import time

def open_terminal():
    pgui.hotkey("ctrl", "alt", "t")

def open_gedit():
    pgui.write("gedit main.rs", 0.05)
    pgui.press("enter")

def coding(fr):
    f = open(fr)
    text = f.read()
    pgui.write(text, interval=0.05)

def open_vim(filename):
    pgui.write("vim " + filename, 0.05)
    pgui.press("enter")
    time.sleep(2)
    pgui.press("a")

open_terminal()
time.sleep(2)
open_gedit()
time.sleep(2)
coding("/home/lucky/workspace/nats/src/main.rs")
