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
    write(text)

def open_vim(filename):
    pgui.write("vim " + filename, 0.05)
    pgui.press("enter")
    time.sleep(2)
    pgui.press("a")

def write(text):
    strs = text.split("<")
    for i, s in enumerate(strs):
        pgui.write(s, 0.05)
        if i != len(strs) - 1:
            pgui.keyDown("shift")
            pgui.keyDown(",")
            pgui.keyUp("shift")
            pgui.keyUp(",")

open_terminal()
time.sleep(2)
open_vim("main.rs")
time.sleep(2)
syntax_on()
coding("/home/lucky/workspace/nats/src/main.rs")
