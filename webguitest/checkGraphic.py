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
    def checkGraphic(imagepath,delay=10,confidence=1):
        elemToCheck = None
        numTries = 1
        print("    (0): locating {} ...".format(imagepath))
        while (elemToCheck is None) and (numTries < delay):
            try:
                elemToCheck = pyautogui.locateOnScreen(imagepath,confidence)
            except Exception as exp:
                if isinstance(exp, pyautogui.pyscreeze.ImageNotFoundException):
                    print("    ({}): locating {} ...".format(numTries,imagepath))
                else:
                    print(exp)
                    break
            finally:
                numTries += 1
                time.sleep(1)
        if elemToCheck is None:
            print("    (x): could not locate image {}".format(imagepath))
            return False
        return True
else:
    def checkGraphic(imagepath,delay=10,confidence=1):
        print("ERROR: no module 'pyautogui' - 'clickGraphic()' is not available")
        print("       maybe you missed to also install the 'Xlib' library on which pyautogui depends on")
        return False
