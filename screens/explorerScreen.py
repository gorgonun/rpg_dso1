from screen import Screen
import PySimpleGUI as sg
import math

class ExplorerScreen(Screen):
    
    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self, text, commands):
        layout = [
            [sg.Text(text, size=(self.rows, math.floor((self.columns/6 * 3))), key="top")],
            [sg.Text("", size=(self.rows, math.floor(self.columns/6 * 2)), key="commands")],
            [sg.Input(enable_events=True, size=(self.rows, math.floor(self.columns/6 * 1)), key="command")]
        ]

        window = sg.Window("Explorer screen", layout=layout, **self.screen_configs).Finalize()
        window.Element("command").SetFocus()
        window.Maximize()

        def func_screen(window):
            event, values = window.Read()
            if values["command"] in commands:
                return False, values["command"]
            elif values["command"] == "?":
                window.Element("commands").Update(" | ".join(commands))

        return self.execute_screen(func_screen, window)

    def show_text(self, text):
        self.print_wait_confimation(text)

    # def get_action(self, text:str, commands: list):
    #     output_dict = {
    #         key: {
    #             "f": lambda key: key,
    #             "args": [key]
    #         }
    #          for key in commands
    #          }
    #     return self.get_adventure_input(text, output_dict)
