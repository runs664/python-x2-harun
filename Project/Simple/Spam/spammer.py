import pyautogui, time
time.sleep(7)
f = open("Project/Simple/Spam/text.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")