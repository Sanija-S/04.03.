import PySimpleGUI as sg
import os 
import io # ievada izvada operacijas, lau teksta straumi parverst pec baitu datiem- nostreamo
from PIL import image # moulis kkas apstrada attelus
# pip install Pillow
# python.exe -m pip install --upgrade pip
buttons=[

   [sg.T("Izvēlies mapi ar attēliem:"), sg.input(key="Input", inable_events=True), sg.FolderBrowse()],
   [sg.image(key="Image", size=(400,400))],
   [sg.T("Attēls:"), sg.T("0 / 0", key="Index")],
   [sg.Button("Iziet"), sg.Button("Iepriekš"), sg.Button("Atpakaļ")]

]
logs=sg.Window("Attēlu galerija", buttons, finalize=True) # finalizepabeigts nekavejoties pec to izveles, tiek izdaritis visas darbibas pirms fails atverts- izmanto kad darbibas veicamas pirms lodu parada
while True:
    event, values= logs.read()
    if event in (sg.WIN_CLOSED , "Iziet", "Close"): # more complex solution
        break
logs.close() 