#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# set up needed modules and flag them if they are missing,
# so specific functionalities are deactivated
# ----------------------------------------------------------------------
"""
import time

pyautoguiAvailable = False
seleniumAvailable = False

try:
    import pyautogui
    pyautoguiAvailable = True
except ModuleNotFoundError:
    pass

try:
    from selenium import webdriver
    seleniumAvailable = True
except ModuleNotFoundError:
    pass

if not (pyautoguiAvailable and seleniumAvailable):
    # neither one of the two modules is available, so quit with a message
    print("ERROR: You need at least 'selenium' or the 'pyautogui' module to be installed.")
    quit()
elif not pyautogui:
    # only pyautogui is missing
    print("INFO: 'pyautogui' is missing. Features based on screen recognition are deactivated.")
    print("      If you want to use these, try installing by 'pip install pyautogui'.")
elif not seleniumAvailable:
    # only selenium is missing
    print("INFO: 'selenium' is missing. Features based on HTML selection are deactivated.")
    print("      If you want to use these, try installing by 'pip install selenium' and setting up a selenium webdriver.")
else:
    # everything is there
    print("INFO: 'pyautogui' and 'selenium' found.")
"""

import webguitest


if __name__ == "__main__":
    print("Running tests ...")
    
    firefox = webguitest.openBrowser("http://www.bev.gv.at",1200,600)
    #webguitest.getValueFromName(firefox,"asdf",2)
    webguitest.clickName(firefox,"V")
    webguitest.clickTextElement(firefox,"Shops & Services")
    #webguitest.clickGraphic("shop.png",2)
    #webguitest.clickGraphic("bevshop.png",2)
    webguitest.clickTextElement(firefox,"\nBEV Shop")
    webguitest.enterValueToName(firefox,"katastralgemeinde","45313",False)
    webguitest.enterValueToName(firefox,"grundstuecksnummer","100",False)
    webguitest.clickName(firefox,"anzeigenBtn")
    webguitest.setValueOfName(firefox,"hierarchies","Orthophotos A4")
    webguitest.clickName(firefox,"suchenBtn")
    
    #firefox.close()
