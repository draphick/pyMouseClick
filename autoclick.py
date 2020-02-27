import pyautogui, sys
import time

# ctrl+c to stop/exit script
print("press ctrl+c to stop/exit autoclicker")
try:
    while True:
        # sleep 1 second
        time.sleep(.5)
        # clicking mouse
        pyautogui.click()
except:
    pass