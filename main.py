import pyautogui 

pyautogui.moveTo(1105, 447, 1)

for i in range(10000000):
    if(pyautogui.position(1105, 447)):
        pyautogui.moveTo(1200, 800, 1)
        
    if(pyautogui.position(1200, 800)):
        pyautogui.moveTo(1105, 800, 1)
