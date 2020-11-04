from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('pressed ', x, y)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(755, 628)[0] == 0:
        click(755, 628)
    if pyautogui.pixel(882, 628)[0] == 0:
        click(882, 628)
    if pyautogui.pixel(1035, 628)[0] == 0:
        click(1035, 628)
    if pyautogui.pixel(1153, 628)[0] == 0:
        click(1153, 628)
