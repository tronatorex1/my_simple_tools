# These scripts help in creating sort of a MACRO (Excel) that is a script with actions related to mouse, keyboard and print screen operations
#   It comes with pop up windows and more. Use it as a Non-TKInter pop up solution (faster and lighter)
# https://pyautogui.readthedocs.io/en/latest/quickstart.html

import pyautogui

# General Functions
pyautogui.position()  # current mouse x and y
pyautogui.size()  # current screen resolution width and height
pyautogui.onScreen(55, 55)  # True if x & y are within the screen.

# Fail-Safes: Set up a 2.5 second pause after each PyAutoGUI call:
pyautogui.PAUSE = 2.5
#   When fail-safe mode is True, moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can abort your program
pyautogui.FAILSAFE = True

# Mouse Movements
pyautogui.moveTo(111, 222, duration=2)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
pyautogui.dragTo(111, 222, duration=4)
pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)
pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
pyautogui.drag(30, 0, 2, button='right')      # drag the mouse left 30 pixels over 2 seconds while holding down the right mouse button
pyautogui.click(x=111, y=222, clicks=3, interval=2, button='right')
pyautogui.rightClick(x=moveToX, y=moveToY)
pyautogui.middleClick(x=moveToX, y=moveToY)
pyautogui.doubleClick(x=moveToX, y=moveToY)
pyautogui.tripleClick(x=moveToX, y=moveToY)
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')
pyautogui.moveTo(100, 200)   # moves mouse to X of 100, Y of 200.
pyautogui.moveTo(None, 500)  # moves mouse to X of 100, Y of 500.
pyautogui.moveTo(600, None)  # moves mouse to X of 600, Y of 500.
pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds

#    Move by Tweening
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)     # start slow, end fast
pyautogui.moveTo(100, 100, 2, pyautogui.easeOutQuad)    # start fast, end slow
pyautogui.moveTo(100, 100, 2, pyautogui.easeInOutQuad)  # start and end fast, slow in middle
pyautogui.moveTo(100, 100, 2, pyautogui.easeInBounce)   # bounce at the end
pyautogui.moveTo(100, 100, 2, pyautogui.easeInElastic)  # rubber band at the end

# Keyboard Functions
pyautogui.typewrite('Hello world!\n', interval=2)
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=1)
pyautogui.KEYBOARD_KEYS # list of all possible keys to use
pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
pyautogui.hotkey('ctrl', 'shift', 'esc')
pyautogui.keyDown('volumedown')
pyautogui.keyUp('A')

# Message Box Functions: use them to show a pop-up window and allow user-input actions
pyautogui.alert('This displays some text with an OK button.')
pyautogui.confirm('This displays text and has an OK and Cancel button.')
x = pyautogui.prompt('This lets the user type in a string and press OK.') # this allows to ener data and is caught in var x
pyautogui.alert(text='', title='', button='OK')
y = pyautogui.password(text='Enter your password:', title='Password', default='', mask='░')

# Screenshot Functions
pyautogui.screenshot()  # returns a Pillow/PIL Image object
pyautogui.screenshot('foo.png')  # returns a Pillow/PIL Image object, and saves it to a file
for i in pyautogui.locateAllOnScreen('looksLikeThis.png'):
    print(i)
list(pyautogui.locateAllOnScreen('looksLikeThis.png'))
pyautogui.locateCenterOnScreen('looksLikeThis.png')
pyautogui.screenshot(region=(0,0, 300, 400))
"""
Note: You can visually locate something on the screen if you have an image file of it.
The calculator can appear in a slightly different place each time it is launched, causing you to re-find the coordinates each time. 
However, if you have an image of the button (a pic in a png file), such as the image of the "7" button
you can call the locateOnScreen('calc7key.png') function to get the screen coordinates
The return value is a 4-integer tuple: (left, top, width, height)
"""
pyautogui.locateOnScreen('looksLikeThis.png') # tries to locate the png file on the screen and returns (left, top, width, height) of first place it is found


# Mouse clicks
pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click(x=100, y=200)    # move to 100, 200, then click the left mouse button.
pyautogui.click('button.png')    # Find where button.png appears on the screen and click it.
pyautogui.click(button='right')  # right-click the mouse
pyautogui.click(clicks=2)        # double-click the left mouse button
pyautogui.click(clicks=2, interval=0.25)  # double-click the left mouse button, but with a quarter second pause in between clicks
pyautogui.click(button='right', clicks=3, interval=0.25)  ## triple-click the right mouse button with a quarter second pause in between clicks
pyautogui.doubleClick()  # perform a left-button double click
pyautogui.tripleClick()
pyautogui.scroll(10)     # scroll up 10 "clicks"
pyautogui.scroll(-10)    # scroll down 10 "clicks"
pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"
pyautogui.hscroll(10)    # scroll right 10 "clicks"
pyautogui.hscroll(-10)   # scroll left 10 "clicks"

# Others
screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
pyautogui.moveTo(600, 750) # Move the mouse to XY coordinates.
pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick()     # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
    pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times. Shift key is released automatically
pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.


# Samples:

# 1
import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')