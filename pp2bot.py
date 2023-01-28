import pyautogui

pyautogui.PAUSE = 0.01

while True:
    fishing = False

    if not fishing:
        print('ei kalasteta')
        smallsurvari = pyautogui.locateOnScreen('./images/smallsurvari.png')
        emptyhook = pyautogui.locateOnScreen('./images/emptyhook.png',)
        ritsa = pyautogui.locateOnScreen('./images/ritsa.png')
        holmes = pyautogui.locateOnScreen('./images/holmes.png')
        survi = pyautogui.locateOnScreen('./images/survi.png')
        rod = pyautogui.locateOnScreen('./images/rod.png')
        out = pyautogui.locateOnScreen('./images/out.png')

        if survi or smallsurvari:
                print('mato paikallaan, pilkitään')
                pyautogui.click(rod)
        if emptyhook:
                print('tyhjä koukku, mato vaihdetaan')
                pyautogui.click(emptyhook)
        if ritsa:
                fishing=True
                print('ritsa pilkkivalmiina, poistutaan pilkkinäkymästä')
                pyautogui.click(out)

    if fishing:
        while fishing:
            print('kalastetaan')
            redrod = pyautogui.locateOnScreen('./images/redrod.png', confidence=0.99999)
            if redrod:
                print('punainen vapa, nostetaan kala')
                pyautogui.click(redrod)
                fishing=False


