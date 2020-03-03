import pyautogui
import time

# print(pyautogui.position())
# print(pyautogui.size())
# print(pyautogui.locateCenterOnScreen('IEIcon.png'))
# print(pyautogui.locateOnScreen('IEIcon.png'))
# pyautogui.screenshot('Outputs/output.png')
# time.sleep(2)
pyautogui.screenshot('Outputs/output_specific.png', region=(pyautogui.locateOnScreen('PostManIcon.png', confidence=0.7)))