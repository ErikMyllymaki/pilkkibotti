import pyautogui

def pull():
    pyautogui.PAUSE = 0.01
    redrod = pyautogui.locateOnScreen('./images/redrod.png', confidence=0.99999)
    if redrod:
        print('punainen vapa, nostetaan kala')
        pyautogui.click(redrod)