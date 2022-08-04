# -*- coding: utf-8 -*-

import pandas as pd

import PySimpleGUI as sg
from random import choice
data = pd.read_csv("animes.csv")
shows = data["title"]
print = sg.Print

layout = [
    [sg.Text("Press the button for a random show!")],
    [sg.Button("ok")]
    
]



#create the window
window = sg.Window("CHOOSE FOR ME", layout, size=(300,200))


# create an even loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "ok": 
         print("Yay! let's Watch " + (choice(shows) +"!"))


    while True:

        event, values = window.read()
        if event in sg.WIN_CLOSED:
            break
        
    window.close()
         



        

   
           
       
   

    





