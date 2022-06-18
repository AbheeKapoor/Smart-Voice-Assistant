from os import startfile
from pyautogui import click
from keyboard import press
from keyboard import write
from time import sleep
import webbrowser as web

def whatsappMsg(name,message):
    startfile("C:\\Users\\home\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15) 
    click(x=221,y=134)
    sleep(2)
    write(name)
    sleep(2)
    click(x=231,y=307)
    sleep(2)
    click(x=1567,y=984)
    sleep(2)
    
    write('hello')
    press('enter')

#whatsappMsg('sahil','hello')
def whatsappCall(name):
    startfile("C:\\Users\\home\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15) 
    click(x=221,y=134)
    sleep(2)
    write(name)
    sleep(2)
    click(x=231,y=307)
    sleep(2)
    click(x=1567,y=984)
    sleep(2)
    click(x=1650,y=80)
#whatsappCall('sahil')

def whatsappChat(name):
    startfile("C:\\Users\\home\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    sleep(15) 
    click(x=221,y=134)
    sleep(2)
    write(name)
    sleep(2)
    click(x=231,y=307)
    sleep(2)
    click(x=1567,y=984)
    sleep(2)

#whatsappChat('sahil')

def classScience(subject):
        web.open("https://meet.google.com/gcz-okov-aem")
        sleep(15)
        click(x=626,y=768)
        sleep(2)
        click(x=698,y=781)
        sleep(2)
        click(x=1337,y=564)
        sleep(2)
        click(x=1740,y=1024)
        sleep(2)
        click(x=1563,y=932)
        sleep(2)
        write('Joined class sir')
        press('enter')


def classMaths(subject):
        web.open("https://meet.google.com/gcz-okov-aem")
        sleep(15)
        click(x=626,y=768)
        sleep(2)
        click(x=698,y=781)
        sleep(2)
        click(x=1337,y=564)
        sleep(2)
        click(x=1740,y=1024)
        sleep(2)
        click(x=1563,y=932)
        sleep(2)
        write('Joined class sir')
        press('enter')

def classEnglish(subject):
        web.open("https://meet.google.com/gcz-okov-aem")
        sleep(15)
        click(x=626,y=768)
        sleep(2)
        click(x=698,y=781)
        sleep(2)
        click(x=1337,y=564)
        sleep(2)
        click(x=1740,y=1024)
        sleep(2)
        click(x=1563,y=932)
        sleep(2)
        write('Joined class sir')
        press('enter')


