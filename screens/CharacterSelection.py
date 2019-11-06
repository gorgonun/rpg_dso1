import PySimpleGUI as sg
import tkinter as tk

root = tk.Tk()

def validate(number):
    try:
        int(number)
        return True
    except:
        return False

def validate_text(text):
    return True if len(text) > 0 else False

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

layout = [
    [sg.Text("Players")],
    [sg.Listbox(values=("Player1", "Player2", "Player3"), enable_events=True, key="player", size=(20, 20)), sg.Listbox(values=("frf"), enable_events=True, key="char")],
    [sg.Button('Select'), sg.Button('Create'), sg.Button('Edit'), sg.Button('Remove'), sg.Button('Exit')]
]

create_char_layout = [
    [sg.Text("Create a character")],
    [sg.Text("Name", size=(14, 1)), sg.Input(enable_events=True, key="name")],
    [sg.Text("Age", size=(14, 1)), sg.Input(enable_events=True, key="age")],
    [sg.Text("Character name", size=(14, 1)), sg.Input(enable_events=True, key="char_name")],
    [sg.Submit(), sg.Button("Cancel")]
]

window = sg.Window("Character Selection", layout=layout, no_titlebar=True, location=(0,0), size=(screen_width,screen_height)).Finalize()
window.Element("char").Update(visible=False)
window.Maximize()

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break
    elif event == "player":
        window.Element("char").Update(visible=True)
    elif event == "Create":
        creation_window = sg.Window("Create a character", layout=create_char_layout, no_titlebar=True, location=(0,0), size=(screen_width,screen_height)).Finalize()
        creation_window.Maximize()
        event, values = creation_window.Read()
        if event == "Submit":
            if not validate_text(values["name"]):
                creation_window.Element("name").SetFocus()
            elif not validate(values["age"]):
                creation_window.Element("age").SetFocus()
            elif not validate_text(values["char_name"]):
                creation_window.Element("char_name").SetFocus()
            else:
                print(values)
                creation_window.Close()
        else:
            print(event)
    elif event == 'Select':
        print(values)


window.Close()