import pyautogui


def getReady():
    # 点击确认选择职责
    jsBtn = pyautogui.locateCenterOnScreen('save_picture/accept.jpg', confidence=0.7)
    if jsBtn is not None:
        pyautogui.moveTo(jsBtn)
        pyautogui.click()
        print('已点击接受职责选择')

        pyautogui.sleep(1)

        # 点击灵活职责
        lhBtn = pyautogui.locateCenterOnScreen('save_picture/lh.jpg', confidence=0.7)
        if jsBtn is not None:
            pyautogui.moveTo(lhBtn)
            pyautogui.click()
            print('已点击灵活职责')

            pyautogui.sleep(1)

            # 点击就绪
            jxBtn = pyautogui.locateCenterOnScreen('save_picture/ready.jpg', confidence=0.7)
            if jsBtn is not None:
                pyautogui.moveTo(jxBtn)
                pyautogui.click()
                print('已点击就绪')

                return True


def autoPlay():
    print("start autoPlay")

    if (pyautogui.pixelMatchesColor(1088, 1223, (255, 162, 0))):
        pyautogui.moveTo(1113, 1234)
        pyautogui.doubleClick()
        print("选托比昂")

        pyautogui.keyDown('w')
        pyautogui.sleep(5)
        pyautogui.keyUp('w')

        pyautogui.keyDown('a')
        pyautogui.sleep(2)
        pyautogui.keyUp('a')

        pyautogui.keyDown('d')
        pyautogui.sleep(2)
        pyautogui.keyUp('d')
    elif(pyautogui.pixelMatchesColor(2044, 1193, (255, 162, 0))):
        pyautogui.moveTo(2044, 1193)
        pyautogui.doubleClick()
        print("选DJ")

        pyautogui.keyDown('w')
        pyautogui.sleep(5)
        pyautogui.keyUp('w')

        pyautogui.keyDown('a')
        pyautogui.sleep(2)
        pyautogui.keyUp('a')

        pyautogui.keyDown('d')
        pyautogui.sleep(2)
        pyautogui.keyUp('d')

if __name__ == '__main__':
    print('start')
    pyautogui.PAUSE = 0.5

    while True:
        # if getReady():
        #     autoPlay()
        # pyautogui.sleep(1)
        # autoPlay()
        print(pyautogui.position())
        x, y = pyautogui.position()
        print(pyautogui.pixel(x, y))
        pyautogui.sleep(1)
        # 托比昂位置 1113, y=1234 (x=1091, y=1226) color (255, 162, 0)
        # dj Point(x=2044, y=1193) # (255, 162, 0)
        # 秩序之光位置 x=1619, y=1243
        # dj位置 x=2009, y=1239
