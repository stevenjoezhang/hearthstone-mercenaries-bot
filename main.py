import pyautogui
import time
import sys
import random
time.sleep(3)


def auto1():
    while (True):
        try:
            pyautogui.click(573, 732)
            print("a")
            time.sleep(1)
            pyautogui.click(1415, 817)
            print("b")
            time.sleep(3)
            pyautogui.click(529, 394)
            time.sleep(1)
            pyautogui.click(1315, 817)
            time.sleep(2)
            pyautogui.click(869, 626)
            print("c")
            time.sleep(9)
            pyautogui.click(1415, 817)
            print("d")
            while (not pyautogui.pixelMatchesColor(1467, 527, (146, 151, 0), tolerance=15)):
                time.sleep(2)
            time.sleep(1)
            pyautogui.click(1468, 517)
            time.sleep(25)
            print("e")
            t = 0
            # not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15)):
            while(pyautogui.pixelMatchesColor(1467, 527, (146, 151, 0), tolerance=15) and t < 5):
                pyautogui.click(1120, 513)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(1.5)
                pyautogui.click(806, 520)
                time.sleep(3)
                pyautogui.click(1468, 517)
                time.sleep(20)
                t = t+1
            print("f")
            pyautogui.click(1468, 517)
            t = 0
            while ((not pyautogui.pixelMatchesColor(1025, 506, (63, 68, 129), tolerance=15)) and t < 10):
                time.sleep(2)
                t = t+1
            time.sleep(1)
            pyautogui.click(865, 567)
            time.sleep(1.5)
            pyautogui.click(1111, 822)
            time.sleep(5)
            print("h")
            pyautogui.click(813, 941)
            time.sleep(1)
            pyautogui.click(1062, 764)
            time.sleep(1)
            pyautogui.click(866, 618)
            time.sleep(5)
            pyautogui.click(866, 618)
            time.sleep(5)
        except:
            time.sleep(1)
            print("error")


def auto2():
    try:
        while(True):
            pyautogui.click(a, b)
            time.sleep(10+random.random())
    except KeyboardInterrupt:
        sys.exit(0)


auto1()
