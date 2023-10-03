import pyautogui

def printPosAndPixel():
    print(pyautogui.position())
    x, y = pyautogui.position()
    print(pyautogui.pixel(x, y))
    pyautogui.sleep(1)


if __name__ == '__main__':
    print('start duihuan')
    pyautogui.PAUSE = 0.2
    pyautogui.FAILSAFE = True
    while True:
        pyautogui.click(580, 1173)
        pyautogui.click(1380, 864)
        printPosAndPixel()

