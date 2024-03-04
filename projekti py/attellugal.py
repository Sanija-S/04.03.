import PySimpleGUI as sg
import os 
import io # ievada izvada operacijas, lau teksta straumi parverst pec baitu datiem- nostreamo
from PIL import image # mdulis kkas apstrada attelus
# pip install Pillow

buttons=[
    
   [sg.T("Izvēlies mapi ar attēliem:"), sg.input(key="Input", inable_events=True), sg.FolderBrowse()],
   [sg.image(key="Image", size=(400,400))],
   [sg.T("Attēls:"), sg.T("0 / 0", key="Index")],
   [sg.Button("Iziet"), sg.Button("Iepriekš"), sg.Button("Atpakaļ")]

]
logs=sg.Window("Attēlu galerija",buttons, resizable=True)
while True:
    event, values= logs.read
    if event==sg.WIN_CLOSED or event== "Iziet":
        break
logs.close() 