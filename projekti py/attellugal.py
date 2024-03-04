import PySimpleGUI as sg
import os 
import io # ievada izvada operacijas, lau teksta straumi parverst pec baitu datiem- nostreamo
from PIL import Image # moulis kkas apstrada attelus
# pip install Pillow
# python.exe -m pip install --upgrade pip

# Funkcijas, kas ieuto atte;u o failu saraksta no noraditas mapes direktorijas
def get_image_files(directory):
    image_files=[f for f in os.listdir(directory) if f.lower().endswith((".png",".jpeg",".jpg", ".gif"))]
# Funkcija. lai paraditu attelus
def show_gallery(image_files, selected_index, window):
    if selected_index<len(image_files):
       filename=os.path.join(directory, image_files(selected_index)) #* - directory fix
       image=Image.open(filename)
       image.thumbnail((400,400))
       bio=io.BytesIO()
       image.save(bio, format="PNG")
       window["Image"].update(data=bio.getvalue())
       window["Image"].update(f"{selected_index+1} / {len(image_files)}")
    else:
         window["Image"].update(filename="", size=(400,400))
         window["Image"].update("0 / 0")
       



menu_def=[["File",["Close"]], ["HELP",["About"]]] # izvēļņu josla

buttons=[
   [sg.Menu(menu_def)],
   [sg.T("Izvēlies mapi ar attēliem:"), sg.Input(key="Input", enable_events=True), sg.FolderBrowse()],
   [sg.Image(key="Image", size=(400,400))],
   [sg.T("Attēls:"), sg.T("0 / 0", key="Index")],
   [sg.Button("Iziet"), sg.Button("Iepriekš"), sg.Button("Atpakaļ")]
]
logs=sg.Window("Attēlu galerija", buttons, finalize=True) # finalizepabeigts nekavejoties pec to izveles, tiek izdaritis visas darbibas pirms fails atverts- izmanto kad darbibas veicamas pirms lodu parada
directory= "" # lai noverstu kludu inda ar simbolu"*"
while True:
    event, values= logs.read()
    if event in (sg.WIN_CLOSED , "Iziet", "Close"): # more complex solution
        break
    if event=="About":
        sg.popup("Darba autore: Sanija Sokirka")
        if event=="Input":
            directory=values["Input"]
            image_files=get_image_files(directory)
            selecte_index=0
            show_galery(image_files, selecte_index, logs)
        if event=="Input":
        if event=="Input":


logs.close() 











#Power Mode
