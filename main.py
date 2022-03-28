import pyautogui
import time
import keyboard
time.sleep(7)
while True:
    pyautogui.write('Jeb sie :)')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(0.1)
    if keyboard.is_pressed('s'):
        break