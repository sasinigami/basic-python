import pyautogui
import time

x = 250
y = 150
num_seconds = 3
xOffset = 500
yOffset = 500
moveToX = 500
moveToY = 500
pyautogui.PAUSE = 0.5 #A pause between each pyautogui action

pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position

# pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
# pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position

# pyautogui.click(x=10, y=10, clicks=2, interval=0.25, button='left')

# pyautogui.rightClick(x=moveToX, y=moveToY)
# pyautogui.middleClick(x=moveToX, y=moveToY)
# pyautogui.doubleClick(x=moveToX, y=moveToY)
# pyautogui.tripleClick(x=moveToX, y=moveToY)

time.sleep(3)
# pyautogui.scroll(-100)
#pyautogui.scroll(-100, x=moveToX, y=moveToY)