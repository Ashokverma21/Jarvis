
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import keyboard
import pyautogui
def WhatsappMessage(name,message):
       
       
        pyautogui.press('win')
        sleep(1)
        keyboard.write('Whatsapp')
        keyboard.press('enter')
        sleep(1)
        return True
        sleep(10)
        click(x=156, y=137)
    
        sleep(1)
    
        write(name)
    
        sleep(1)
        click(x=250, y=231)
        sleep(1)
    
        click(x=821, y=1044)
        sleep(1)
        write(message)
        press("enter")
    
def WhatsappCall(name):
        pyautogui.press('win')
        sleep(1)
        keyboard.write('Whatsapp')
        keyboard.press('enter')
        sleep(1)
        return True
       
        sleep(10)
        click(x=223, y=138)
        
    
        sleep(1)
    
        write(name)
    
        sleep(1)
        click(x=250, y=231)
        sleep(1)
        
        click(x=1767, y=89)

def WhatsappVideoCall(name):
    pyautogui.press('win')
    sleep(1)
    keyboard.write('Whatsapp')
    keyboard.press('enter')
    sleep(1)
    return True
   
    sleep(10)
    click(x=223, y=138)
    

    sleep(1)

    write(name)

    sleep(1)
    click(x=250, y=231)
    sleep(1)
    click(x=1709, y=90)

def WhatsappChat(name):
    pyautogui.press('win')
    sleep(1)
    keyboard.write('Whatsapp')
    keyboard.press('enter')
    sleep(1)
    return True
   
    sleep(10)
    click(x=223, y=138)
    

    sleep(1)

    write(name)

    sleep(1)
    click(x=250, y=231)
    