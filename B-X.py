from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(3)
print('[*] Start!')

def press_space():
    print('Space')
    keyboard.press(Key.space)
    keyboard.release(Key.space)

press_space()
print('[*] 3, 2, 1')
time.sleep(2.05)

for i in range(29):
    press_space()
    time.sleep(0.198888)