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
    from selenium import webdriver
    seleniumAvailable = True
except ModuleNotFoundError:
    pass

if seleniumAvailable:
    def openBrowser(url,x,y):
        driver = webdriver.Firefox()
        driver.get(url)
        driver.set_window_size(x, y)
        driver.set_window_position(0, 0)
        return driver
elif pyautoguiAvailable:
    def openBrowser(url,x,y):
        print("pyautogui method to open Browser is yet to be implemented")
        return False
