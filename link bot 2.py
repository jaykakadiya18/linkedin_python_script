import pyautogui
import webbrowser as wb
import time

wb.open("https://www.linkedin.com/uas/login")
print(pyautogui.position())
print(pyautogui.size())
pyautogui.Size(width=1366, height=768)
time.sleep(8)
# pyautogui.write("jay")
pyautogui.click(x=158, y=580, clicks=1, interval=2, button='left')
# print(pyautogui.position())
print(pyautogui.position())
print("Succes")

