import pyautogui
import time
time.sleep(4)
count = 0
while count <= 100:
# The <= 100: is the total number of messages to be sent. Your can change the value to any number of your choice!
    pyautogui.typewrite("Place The Text You want To Send Here!")
    pyautogui.press("enter")
    
# Then run the code in the terminal and head over to your whatsapp Desktop or web
