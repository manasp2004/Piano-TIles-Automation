# Game URL: https://www.agame.com/game/magic-piano-tiles

# X Position of Tiles:
# Tile 1: 520
# Tile 2: 629
# Tile 3: 706
# Tile 4: 805

# Y Position of all Tiles: 300

# ------------------------------------------------------------------------- #

import pyautogui
import time
import keyboard
import win32api, win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(0.009)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

pyautogui.FAILSAFE = False

time.sleep(1)

while True:
    if keyboard.is_pressed('q') == False:
        if pyautogui.pixel(520, 300)[0] == 0:
            click(520, 305)

        elif pyautogui.pixel(629, 300)[0] == 0:
            click(629, 305)

        elif pyautogui.pixel(706, 300)[0] == 0:
            click(706, 305)

        elif pyautogui.pixel(805, 300)[0] == 0:
            click(805, 305)
    else:
        print("Script Aborted!")
        break