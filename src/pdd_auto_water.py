import pyautogui
import random


def getReady():
    # 点击确认选择职责
    jsBtn = pyautogui.locateCenterOnScreen('../save_picture/accept.jpg', confidence=0.7)
    if jsBtn is not None:
        pyautogui.moveTo(jsBtn)
        pyautogui.click()
        print('已点击接受职责选择')

        pyautogui.sleep(0.5)

        # 点击灵活职责
        if pyautogui.pixelMatchesColor(1587, 690, (255, 255, 255), tolerance=15):
            # 点击就绪
            jxBtn = pyautogui.locateCenterOnScreen('../save_picture/ready.jpg', confidence=0.7)
            if jsBtn is not None:
                pyautogui.moveTo(jxBtn)
                pyautogui.click()
                print('已点击就绪')

                return True
        else:
            print("灵活职责未选择，颜色： " + str(pyautogui.pixel(1587, 690)))
            lhBtn = pyautogui.locateCenterOnScreen('../save_picture/lh.jpg', confidence=0.7)
            if jsBtn is not None:
                pyautogui.moveTo(lhBtn)
                pyautogui.click()
                print('已点击灵活职责')

                pyautogui.sleep(0.3)

                # 点击就绪
                jxBtn = pyautogui.locateCenterOnScreen('../save_picture/ready.jpg', confidence=0.7)
                if jsBtn is not None:
                    pyautogui.moveTo(jxBtn)
                    pyautogui.click()
                    print('已点击就绪')

                    return True


def autoPlay():
    print("start autoPlay")
    lz = False
    while True:
        # jxBtn = pyautogui.locateCenterOnScreen('../save_picture/continue.jpg', confidence=0.6)
        # if jxBtn is not None:
        #     pyautogui.moveTo(jxBtn)
        #     pyautogui.click()
        #     print("已选择英雄")
        if not lz and pyautogui.pixelMatchesColor(2332, 1046, (28, 117, 188), tolerance=3):
            pyautogui.moveTo(1403, 1334)
            pyautogui.click()
            print("已选择英雄")
            lz = True

        if lz:
            print("开始乱走")
            pyautogui.keyDown('w')
            pyautogui.sleep(random.random())
            pyautogui.keyUp('w')

            rt = random.random()
            if rt > 0.5:
                rt -= 0.5
            if rt <= 0.3:
                pyautogui.keyDown('a')
                pyautogui.sleep(rt)
                pyautogui.keyUp('a')

            rt = random.random()
            if rt > 0.5:
                rt -= 0.5
            if rt <= 0.3:
                pyautogui.keyDown('d')
                pyautogui.sleep(rt)
                pyautogui.keyUp('d')

        pyautogui.sleep(1)
        jsBtn = pyautogui.locateCenterOnScreen('../save_picture/accept.jpg', confidence=0.7)
        if jsBtn is not None:
            print("exit autoPlay")
            return
    # if (pyautogui.pixelMatchesColor(1088, 1223, (255, 162, 0))):
    #     pyautogui.moveTo(1113, 1234)
    #     pyautogui.doubleClick()adwa
    #     print("选托比昂")
    #
    #     pyautogui.keyDown('w')
    #     pyautogui.sleep(5)
    #     pyautogui.keyUp('w')
    #
    #     pyautogui.keyDown('a')
    #     pyautogui.sleep(2)
    #     pyautogui.keyUp('a')
    #
    #     pyautogui.keyDown('d')
    #     pyautogui.sleep(2)
    #     pyautogui.keyUp('d')
    # elif (pyautogui.pixelMatchesColor(2044, 1193, (255, 162, 0))):
    #     pyautogui.moveTo(2044, 1193)
    #     pyautogui.doubleClick()
    #     print("选DJ")
    #
    #     pyautogui.keyDown('w')
    #     pyautogui.sleep(5)
    #     pyautogui.keyUp('w')
    #
    #     pyautogui.keyDown('a')
    #     pyautogui.sleep(2)
    #     pyautogui.keyUp('a')
    #
    #     pyautogui.keyDown('d')
    #     pyautogui.sleep(2)
    #     pyautogui.keyUp('d')


def printPosAndPixel():
    print(pyautogui.position())
    x, y = pyautogui.position()
    print(pyautogui.pixel(x, y))
    pyautogui.sleep(1)


if __name__ == '__main__':
    print('start')
    pyautogui.PAUSE = 0.3

    popUpCount = 0
    waterCount = 0
    while True:
        # if getReady():
        # autoPlay()
        # pyautogui.sleep(1)
        closeBtn = pyautogui.locateCenterOnScreen('../save_picture/closeBtn.jpg', confidence=0.8)
        if closeBtn is not None:
            pyautogui.moveTo(closeBtn)
            printPosAndPixel()
            pyautogui.click()
            popUpCount += 1
            print('closed pop-up notification: ' + str(popUpCount))

        # move to water btn
        water20Btn = pyautogui.locateCenterOnScreen('../save_picture/water20Btn.jpg', confidence=0.8)
        if water20Btn is not None:
            pyautogui.moveTo(water20Btn)
        else:
            pyautogui.moveTo(1131, 869)
        pyautogui.click()
        waterCount += 1
        print('water count: ' + str(waterCount))

        # 托比昂位置 1113, y=1234 (x=1091, y=1226) color (255, 162, 0)
        # dj Point(x=2044, y=1193) # (255, 162, 0)
        # 秩序之光位置 x=1619, y=1243
        # dj位置 x=2009, y=1239
        # 选择职位已经是白色 Point(x=1587, y=690) (255, 255, 255)
        # 选择角色 Point(x=1403, y=1334) (230, 162, 65)
        # 加入队伍语音 Point(x=2332, y=1046) (28, 117, 188)
