#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
pyautoguiAvailable = False
seleniumAvailable = False

try:
    import pyautogui
    pyautoguiAvailable = True
except ImportError:
    pass

try:
    import selenium
    seleniumAvailable = True
except ImportError:
    pass

if pyautoguiAvailable:
    def moveGraphic(imagepath,x=500,y=500,delay=10,confidence=1):
        elemToClick = None
        numTries = 1
        print("    (0): locating {} ...".format(imagepath))
        while (elemToClick is None) and (numTries < delay):
            try:
                elemToClick = pyautogui.locateOnScreen(imagepath,confidence)
            except Exception as exp:
                if isinstance(exp, pyautogui.pyscreeze.ImageNotFoundException):
                    print("    ({}): locating {} ...".format(numTries,imagepath))
                else:
                    print(exp)
                    break
            finally:
                numTries += 1
                time.sleep(2)
        if elemToClick is None:
            print("    (x): could not locate image {}".format(imagepath))
            return False
        time.sleep(1)
        pyautogui.mouseDown(pyautogui.center(elemToClick))
        pyautogui.mouseUp(x,y)
        print("    (✓): moved {}".format(elemToClick))
        time.sleep(1)
        return True
else:
    def moveGraphic(imagepath,delay=10,confidence=1):
        print("ERROR: no module 'pyautogui' - 'moveGraphic()' is not available")
        print("       maybe you missed to also install the 'Xlib' library on which pyautogui depends on")
        return False
