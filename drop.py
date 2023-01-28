import pyautogui

def drop():
    pyautogui.PAUSE = 0.01
    rod = pyautogui.locateOnScreen('./images/rod.png', confidence=0.6)
    emptyhook = pyautogui.locateOnScreen('./images/emptyhook.png', confidence=0.9)
    smallsurvari = pyautogui.locateOnScreen('./images/smallsurvari.png', confidence=0.9)
    survi = pyautogui.locateOnScreen('./images/survi.png', confidence=0.6)
    if survi or smallsurvari:
        print('mato paikallaan, pilkitään')
        pyautogui.click(rod)
    elif (not survi and not smallsurvari) and emptyhook:
        print('tyhjä koukku, mato vaihdetaan')
        pyautogui.click(emptyhook)