# WebGuiTest
A web user interface test module for Python 3 combining Selenium and pyautogui into one interface

## Requirements

Ideally you have both, Selenium and the pyautogui module installed. Both are freely available.
Selenium is used for base interaction with the FireFox web browser and to interact with HTML elements when they need to be selected by their ''id'', ''name'' or ''CSS path''.
Pyautogui is used when a portion of the screen needs to be identified by a screenshot. This is helpful, if you need to find a button that has a random ID.

### Selenium

Selenium is a web testing framework used to auto-perform interactions with websites by selecting elements in the DOM of the HTML. It can be used to control many different browsers. WebGuiTest is using only the FireFox browser.

You need to install the selenium driver for python

    pip install selenium

and download the so-called ''geckodriver'' for Selenium to let it interact with an existing installation of the FireFox browser. You can find the current version of the ''geckodriver'' here: https://github.com/mozilla/geckodriver/releases
You have to unpack it and copy the file to a location where your python installation can find the file (e.g. somewhere in your systems $PATH).

### pyautogui

The pyautogui library is simply installed by

    pip install pyautogui

On Linux you additionally need to install the Xlib libary with

    pip install xlib

and the scrot program for taking screenshots:

    apt install scrot

## Changelog

### 0.0.15

  * use pyautogui.moveTo instead of manually combining methods to simulate drag-and-drop

### 0.0.14

  * added a delay of one second to moveGraphic

### 0.0.13

  * also retry when selenium element is not yet loaded

### 0.0.12

  * added "debug" option to methods to allow for surpression of console-output by the testing methods

### 0.0.11

  * introduced paremeter "waitbetweentries" to let user specify the time to wait between retries when dealing with graphical methods

### 0.0.9 / 0.0.10

  * added "moveGraphic" method to drag-and-drop

### 0.0.7 / 0.0.8

  * added "getTextFromName" method to get text content of a named HTML element

### 0.0.6

  * increased time to wait between tries from 1 seconds to 2 seconds when searching for graphical elements

### 0.0.5

  * corrected error

### 0.0.4

  * Added "checkGraphic" function

### 0.0.3

  * Added "enterValueToGraphic" function

### 0.0.2

  * Added "enterValue" function

### 0.0.1

  * First release
