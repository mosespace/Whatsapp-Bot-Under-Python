import pyautogui
import time
time.sleep(4)
count = 0
while count <= 100:
    pyautogui.typewrite("Place The Text You want To Send Here!")
    pyautogui.press("enter")
    
