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

a = 0.19222
for i in range(23):
    press_space()
    time.sleep(a)

for i in range(3):
    press_space()
    time.sleep(a/2)

for i in range(5):
    press_space()
    time.sleep(a)

for i in range(2):
    press_space()
    time.sleep(a*2)