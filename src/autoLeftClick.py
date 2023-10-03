import pyautogui
import keyboard
import threading

def test():
    print("test is OK.")


cutLoop = False


def leftClick():
    while True:
        print('left click count 1')
        pyautogui.leftClick()
        if cutLoop:
            break


def startAutoClick(key):
    keyName=key.name
    global cutLoop
    if keyName=='1':
        cutLoop=True
    elif keyName=='2':
        cutLoop=False
        threading.Thread(target=leftClick).start()

def cutLeftClick():
    raise pyautogui.PyAutoGUIException


# class KeyboardHook(object):
#     def __init__(self):
#         # self.thread = PrintHi()
#         self.set_keyboard_hotkeys()
#         # self.thread.start()
#
#     def toggle_print(self):
#         print("Toggle Print")
#         # self.thread.active = not self.thread.active
#
#     def set_keyboard_hotkeys(self):
#         print("Setting hotkeys hooks")
#         keyboard.add_hotkey('ctrl+p', self.toggle_print)
#         #keyboard.wait()

if __name__ == '__main__':
    pyautogui.PAUSE = 0.1
    # keyboard.add_hotkey('alt+z', leftClick)
    # keyboard.add_hotkey('alt+x', cutLeftClick)
    keyboard.hook(startAutoClick)
    keyboard.wait('4')
