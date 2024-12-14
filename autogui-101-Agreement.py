from sys import exit
import pyautogui as pau
import pyperclip
import tkinter as tk
import tkinter.messagebox as messagebox
import time
import os

tk.Tk().withdraw()
TorF = messagebox.askokcancel('<Agreement>', 'This code will automatically download a picture, and set the picture as your wallpaper.\nDo you accept that?')
if TorF == False:
    exit()

DownloadCmd = 'powershell Invoke-WebRequest -Uri "https://www.python.jp/pages/python_logo2.png" -OutFile "~\Downloads\TheHopeOne.png"'
OpenCmd = 'C:/Users/%username%/Downloads/TheHopeOne.png'

#download a pic on DL-dir
pyperclip.copy(DownloadCmd)
pau.hotkey('win','r')
pau.hotkey('ctrl','v')
pau.press('enter')
time.sleep(1)
pau.press('enter')
time.sleep(2)

#open the pic
pyperclip.copy(OpenCmd)
pau.hotkey('win','r')
pau.hotkey('ctrl','v')
pau.press('enter')
time.sleep(1)

#set it as wallpaper
pau.hotkey('ctrl','b')
time.sleep(1)

#close the pic
pau.hotkey('alt','f4')

os.remove('Downloads/TheHopeOne.png')