from pynput import keyboard as keyboard_handler
import pyglet
from plyer import notification

keyboards = ["alpaca", "blackink", "bluealps", "boxnavy", "buckling", "cream",
            "holypanda", "mxblack", "mxblue", "mxbrown", "redink", "topre", "turquoise"]
keyboard_num = 5
keyboard = keyboards[keyboard_num]


sounds = {}
keys = {
}

def main():
    load_sounds()
    with keyboard_handler.Listener(
            on_press=handle_key_press,
            on_release=handle_key_relase) as listener:
        listener.join()


def get_key_code(key):
    try:
        key_code = key.vk
    except AttributeError:
        key_code = key.value.vk
    return key_code


def handle_key_press(key):
    key_code = get_key_code(key)
    handle_sound(key_code)
    keys[key_code] = True
    print(key_code)
    handle_exit()
    handle_next_keyboard()


def handle_exit():
    # CTRL + SHIFT + C
    if 162 in keys and keys[162] and 160 in keys and keys[160] and 67 in keys and keys[67]:
        exit()


def handle_next_keyboard():
    global keyboard_num
    global keyboard
    global keyboards
    if 162 in keys and keys[162] and 160 in keys and keys[160] and (39 in keys and keys[39] or 37 in keys and keys[37]):
        if 37 in keys and keys[37]:
            keyboard_num -= 1
            if keyboard_num < 0:
                keyboard_num = len(keyboards) - 1
            keyboard = keyboards[keyboard_num]
        else:
            keyboard_num += 1
            if keyboard_num > len(keyboards) - 1:
                keyboard_num = 0
            keyboard = keyboards[keyboard_num]
        notification.notify(
            title='Son de clavier mis à jour',
            message='Votre clavier est maintenant ' + keyboard,
            app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
            timeout=1,  # seconds
        )


def handle_key_relase(key):
    key_code = get_key_code(key)
    keys[key_code] = False


def handle_sound(key_code):
    if key_code not in keys or not keys[key_code]:
        if key_code == 8 and 'BACKSPACE' in sounds[keyboard]:
            sounds[keyboard]['BACKSPACE'].play()
        elif key_code == 13 and 'ENTER' in sounds[keyboard]:
            sounds[keyboard]['ENTER'].play()

        elif key_code == 32 and 'SPACE' in sounds[keyboard]:
            sounds[keyboard]['SPACE'].play()
        else:
            sounds[keyboard]['GENERIC_R' + str(key_code % 5)].play()


def load_sounds():
    for keyboard in keyboards:
        sounds[keyboard] = {}
        for i in range(5):
            load_sound(keyboard, 'GENERIC_R' + str(i))
        load_sound(keyboard, 'BACKSPACE')
        load_sound(keyboard, 'ENTER')
        load_sound(keyboard, 'SPACE')
    
    print("Sounds loaded !")


def load_sound(keyboard, sound_name):
    try:
        sounds[keyboard][sound_name] = pyglet.resource.media(
            'assets/audio/' + keyboard + '/press/' + sound_name + '.mp3', streaming=False)
    except Exception:
        pass

if __name__ == "__main__":
    main()
