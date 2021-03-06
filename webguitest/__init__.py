#!/usr/bin/python3
# -*- coding: utf-8 -*-

name = "webguitest"

"""
----------------------------------------------------------------------
This is the WebGuiTest module.

The functions available are:

  openBrowser():
    Returns a selenium FireFox web-driver object to control the browser.


  clickGraphic(imagepath,delay=10,confidence=1,waitbetweentries=1,doubleclick=False,grayscale=False,debug=False):
    Returns True if successfull, False if not.

    imagepath: The path to the image file with contents to be searched on the screen.
    delay: How many tries to find the graphic should be performed.
    confidence: A value between 0 and 1. This allows the image to deviate slightly from the
                image on the screen. Good for fuzzy matching.
    waitbetweentries: The time to wait between retries in seconds.
    doubleclick: If True, a double click will be performed instead of a single click.
    grayscale: True or False to perform a faster grayscale match
    debug: Default is False. If set to True, there will be more detailed console output.

  
  clickName():
  
  clickId():

  getValueFromName():

  getTextFromName():
  
  enterValueToName():
  
  setValueOfName():
  
  clickTextElement():

  enterValueToGraphic():
  
  enterValue():

  checkGraphic():

  moveGraphic():

  selectDropdownName():

  
----------------------------------------------------------------------
"""


from webguitest.openBrowser import *
from webguitest.clickGraphic import *
from webguitest.clickName import *
from webguitest.getValueFromName import *
from webguitest.getTextFromName import *
from webguitest.enterValueToName import *
from webguitest.setValueOfName import *
from webguitest.clickTextElement import *
from webguitest.enterValueToGraphic import *
from webguitest.enterValue import *
from webguitest.checkGraphic import *
from webguitest.moveGraphic import *
from webguitest.selectDropdownName import *
from webguitest.clickId import *
from webguitest.clickInputValue import *
from webguitest.enterPathToFileName import *