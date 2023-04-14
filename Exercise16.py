# Create a program that converts feet and inches to meters. 

import PySimpleGUI as sg
from functions16 import convert

flabel = sg.Text("Enter feet: ")
feet = sg.InputText(key="feet")

ilabel = sg.Text("Enter inches: ")
inches = sg.InputText(key="inches")

convert_button = sg.Button("Convert")
result_label = sg.Text("", key="output")

window = sg.Window('Converter', 
                   layout=[[flabel, feet], 
                           [ilabel, inches], 
                           [convert_button, result_label]])


while True: 
    event, values = window.read()
    feet = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet, inches)
    window["output"].update(value=f"{result} m")




