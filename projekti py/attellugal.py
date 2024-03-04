import PySimpleGUI as sg
import os 
import io # ievada izvada operacijas, lau teksta straumi parverst pec baitu datiem- nostreamo
from PIL import image # mdulis kkas apstrada attelus
# pip install Pillow

buttons=[

]
logs=sg.Window("Attēlu galerija",buttons, resizable=True)
while True:
    event, values= logs.read
    if event==sg.WIN_CLOSED or event== "Iziet":
        break
logs.close() 