import pywhatkit as pwt
import keyboard



    elif"play" in info or "song" in info or "music" in info:
        name = info.replace("play"or"song"or"music","")
        pwt.playonyt(name)
        keyboard.press("spacebar")
    elif "Stop" in info or "close" in info or"exit" in info: 
        keyboard.press("spacebar")

