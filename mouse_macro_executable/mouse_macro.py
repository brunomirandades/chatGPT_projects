import pyautogui
import keyboard
import time
import random

def move_mouse(x, y, step_x, step_y):
    for i in range(200):
        if keyboard.is_pressed(stop_key):
            exit()
        x += step_x
        y += step_y
        pyautogui.moveTo(x, y)
        time.sleep(0.01)

stop_key = 'ctrl+alt+end'
# keyboard.add_hotkey(stop_key, exit)

while True:
    x, y = pyautogui.position()
    rand_x = x + 200 * (2 * (0.5 - random.random()))
    rand_y = y + 200 * (2 * (0.5 - random.random()))
    step_x = (rand_x - x) / 200
    step_y = (rand_y - y) / 200
    move_mouse(x, y, step_x, step_y)
    time.sleep(5)
    move_mouse(rand_x, rand_y, -step_x, -step_y)
    time.sleep(5)