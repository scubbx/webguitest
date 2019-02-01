#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
pyautoguiAvailable = False
seleniumAvailable = False

try:
    import pyautogui
    pyautoguiAvailable = True
except ModuleNotFoundError:
    pass

try:
    import selenium
    seleniumAvailable = True
except ModuleNotFoundError:
    pass

if pyautoguiAvailable:
    def clickGraphic(imagepath,delay=10,confidence=1):
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
                time.sleep(1)
        if elemToClick is None:
            print("    (x): could not locate image {}".format(elemToClick))
            return False
        time.sleep(1)
        pyautogui.click(pyautogui.center(elemToClick))
        print("    (✓): clicked {}".format(elemToClick))
        time.sleep(1)
        return True
else:
    def clickGraphic(imagepath,delay=10,confidence=1):
        print("ERROR: no module 'pyautogui' - 'clickElement()' is not available")
        return False
