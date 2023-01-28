import pyautogui
# from pull import *
# from drop import *


pyautogui.PAUSE = 0.01

# if redrod2:
# while True:
#     redrod2 = pyautogui.locateOnScreen('./images/redrod2.png', confidence=0.99999)
#     if redrod2:
#         print('punainen vapa, nostetaan kala')
#         # pyautogui.click(redrod)
#         pyautogui.click(redrod2)

while True:
    fishing = True
    pyautogui.PAUSE = 0.01

    while not fishing:
        print('ei kalasteta')
        smallsurvari = pyautogui.locateOnScreen('./images/smallsurvari.png', confidence=0.9)
        emptyhook = pyautogui.locateOnScreen('./images/emptyhook.png', confidence=0.9)
        ritsa = pyautogui.locateOnScreen('./images/ritsa.png', confidence=0.6)
        survi = pyautogui.locateOnScreen('./images/survi.png', confidence=0.6)
        rod = pyautogui.locateOnScreen('./images/rod.png', confidence=0.6)
        out = pyautogui.locateOnScreen('./images/out.png', confidence=0.6)

        def drop():
            if survi or smallsurvari:
                print('mato paikallaan, pilkitään')
                pyautogui.click(rod)
            elif (not survi and not smallsurvari) and emptyhook:
                print('tyhjä koukku, mato vaihdetaan')
                pyautogui.click(emptyhook)
        def pull():
            if ritsa:
                fishing=True
                print('ritsa pilkkivalmiina, poistutaan pilkkinäkymästä')
                pyautogui.click(out)
        drop()
        pull()
        break

    while fishing:
        print('kalastetaan')
        def pull():
            redrod = pyautogui.locateOnScreen('./images/redrod.png', confidence=0.99999)
            if redrod:
                print('punainen vapa, nostetaan kala')
                pyautogui.click(redrod)
                fishing=False

        pull()
 

# while True:

#     pull()
#     drop()
    
    # emptyhook = pyautogui.locateOnScreen('./images/emptyhook.png', confidence=0.9)
    # smallsurvari = pyautogui.locateOnScreen('./images/smallsurvari.png', confidence=0.9)
    # survi = pyautogui.locateOnScreen('./images/survi.png', confidence=0.6)
    # rod = pyautogui.locateOnScreen('./images/rod.png', confidence=0.6)
    # out = pyautogui.locateOnScreen('./images/out.png', confidence=0.6)
    # ritsa = pyautogui.locateOnScreen('./images/ritsa.png', confidence=0.6)

    # # def pull():
    # #     if ritsa:
    # #         print('ritsa pilkkivalmiina, poistutaan pilkkinäkymästä')
    # #         pyautogui.click(out)
    # def drop():
    #     if survi or smallsurvari:
    #         print('mato paikallaan, pilkitään')
    #         pyautogui.click(rod)
    #     elif (not survi and not smallsurvari) and emptyhook:
    #         print('tyhjä koukku, mato vaihdetaan')
    #         pyautogui.click(emptyhook)

    # drop()
    # # pull()


