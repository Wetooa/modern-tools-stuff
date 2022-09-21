import time
import pyautogui
import pyscreenshot
import keyboard

while keyboard.is_pressed(']') == False:
    # this is for the pixel finding
    if keyboard.is_pressed('[') == True:
        print(pyautogui.position())
        time.sleep(1)
    if keyboard.is_pressed('ctrl') == True:
        pic = pyscreenshot.grab(bbox=(539, 233, 1760, 937))
        currTime = time.strftime("%Y%m%d-%H%M%S")
        pic.save("C:/Users/Wetooa/Documents/Educational/College/First Year/CS Modern Tools - 1/act 7/img6/" + currTime + ".png")
        time.sleep(1)
