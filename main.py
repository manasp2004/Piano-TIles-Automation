# Game URL: https://www.agame.com/game/magic-piano-tiles

# X Position of Tiles:
# Tile 1: 536
# Tile 2: 629
# Tile 3: 706
# Tile 4: 797

# Y Position of all Tiles: 400

# ------------------------------------------------------------------------- #

import pyautogui
import time
import keyboard

pyautogui.FAILSAFE = False

while True:
    if keyboard.is_pressed('q') == False:
        if pyautogui.pixel(536, 400)[0] == 0:
            pyautogui.click(536, 400, button='right')

        elif pyautogui.pixel(629, 400)[0] == 0:
            pyautogui.click(629, 400, button='right')

        elif pyautogui.pixel(706, 400)[0] == 0:
            pyautogui.click(706, 400, button='right')

        elif pyautogui.pixel(797, 400)[0] == 0:
            pyautogui.click(797, 400, button='right')
    else:
        print("Script Aborted!")
        break