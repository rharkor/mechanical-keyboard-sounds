# Python mechanical keyboard simulation

**Don't forget to authorize the files in windows security (Cause it delete them automatically thinking it's a keylogger)**

**Clone this project in C:\Program Files (x86)\keyboardSim otherwise you can't start script**
## Startup

Windows :

```
.\venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

To desactivate the venv

```
deactivate
```

## Usage

List of keyboards and personal rates :
0: alpaca (7/10)
1: blackpink (6/10)
2: bluealps (4/10)
3: boxnavy (5/10)
4: buckling (4/10)
5: cream (9/10)
6: holypanda (6/10)
7: mxblack (7/10)
8: mxblue (6/10)
9: mxbrown (7/10)
10: redink (8/10)
11: topre (5/10)
12: turquoise (6/10)

Choose your favorite keyboard (main.py : line 7)

```
keyboard_num = HERE_KEYBOARD_NUM
```

## Usefull commands

`CTRL + SHIFT + C`

> Stop the program

`CTRL + SHIFT + [LEFT_ARROW/RIGHT_ARROW]`

> Change keyboard

## Run on startup

Create a .exe from the main.py
**_notifications of changing keyboard doesnt work so put them in comment (line 64-69 in main.py)_**

```py

        notification.notify(
            title='Son de clavier mis à jour',
            message='Votre clavier est maintenant ' + keyboard,
            app_icon=None,  # e.g. 'C:\\icon_32x32.ico'
            timeout=1,  # seconds
        )
```

```cmd
pyinstaller 'main.py' --onefile --noconsole
```

Put the script .exe to  (`C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`)
