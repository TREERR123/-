import time
import ctypes
import keyboard

# 鼠标侧键启动
"""
def main():
    while True:
        if ctypes.windll.user32.GetKeyState(0x05) < 0:
            ctypes.windll.user32.mouse_event(0x01, 800, 0, 0, 0)
        time.sleep(0.001)
"""

# 键盘‘1’启动
def main():
    while True:
        if keyboard.is_pressed('1'):
            ctypes.windll.user32.mouse_event(0x01, 800, 0, 0, 0)
        time.sleep(0.001)


if __name__ == "__main__":
    print('记得以管理员身份运行，否则无效')
    main()
