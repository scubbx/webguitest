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
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import Select
    seleniumAvailable = True
except ImportError:
    pass


if seleniumAvailable:
    def selectDropdownName(driver,elementName,textToSelect,delay=10,elementnumber=-1,debug=False):
        numTries = 1
        elemToClick = None
        if debug: print("    (0): locating {} ...".format(elementName))
        while (elemToClick is None) and (numTries < delay):
            try:
                if elementnumber >= 0:
                    elemToClick = driver.find_elements_by_name(elementName)[elementnumber]
                else:
                    elemToClick = driver.find_element_by_name(elementName)
            except Exception as exp:
                if isinstance(exp, selenium.common.exceptions.NoSuchElementException):
                    if debug: print("    ({}) locating {} ...".format(numTries,elementName))
                elif isinstance(exp, selenium.common.exceptions.ElementNotInteractableException):
                    if debug: print("    ({}) locating {} ...".format(numTries,elementName))
                else:
                    if debug: print(exp)
                    break
            finally:
                numTries += 1
                time.sleep(0.5)
        if elemToClick is None:
            if debug: print("    (x): could not locate name={}".format(elementName))
            return False
        Select(elemToClick).select_by_visible_text(textToSelect)
        if debug: print("    (✓): selected on {}".format(textToSelect))
        return True

else:
    def selectDropdownName(driver,elementName,textToSelect,delay=10,elementnumber=-1,debug=False):
        if debug: print("ERROR: no module 'selenium' - 'enterValueToName()' is not available")
        return False
