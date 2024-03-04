import PySimpleGUI as sg
import os 
buttons=[

]
logs=sg.Window("Attēlu galerija",buttons, resizable=True)
while True:
    event, values= logs.read
    if event==sg.WIN_CLOSED or event== "Iziet":
        break
logs.close()