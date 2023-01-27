import pyautogui


while True:
    rod = pyautogui.locateOnScreen('./images/rod.png', confidence=0.99999)
    emptyhook = pyautogui.locateOnScreen('./images/emptyhook.png', confidence=0.99999)
    mutka = pyautogui.locateOnScreen('./images/mutka.png', confidence=0.4)
    if mutka:
        pyautogui.click(rod)
    if emptyhook:
        pyautogui.click(emptyhook)
    redrod = pyautogui.locateOnScreen('./images/redrod.png', confidence=0.99999)
    if redrod:
        print('red')
        pyautogui.click(redrod)



