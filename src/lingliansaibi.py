import pyautogui

def printPosAndPixel():
    print(pyautogui.position())
    x, y = pyautogui.position()
    print(pyautogui.pixel(x, y))
    pyautogui.sleep(1)


if __name__ == '__main__':
    print('start 领联赛币')
    pyautogui.PAUSE = 2
    pyautogui.FAILSAFE = True
    while True:
        pyautogui.click(1808, 715)
        pyautogui.sleep(2)
        pyautogui.click(1767, 764)
        pyautogui.sleep(600)
        # printPosAndPixel()

