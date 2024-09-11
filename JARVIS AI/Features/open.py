import os
import keyboard
import pyautogui
import webbrowser
from time import sleep


 
def OpenExe(query):
    Query  = str(query).lower()
    
    
    if "visit" in query:
        Nameofweb = Query.replace("visit ","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "open" in query:
        Nameofapp = query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameofapp)
        keyboard.press('enter')
        sleep(0.5)
        return True
        
    
    elif "start" in query:
        Nameofapp = query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameofapp)
        keyboard.press('enter')
        sleep(0.5)
        return True
    