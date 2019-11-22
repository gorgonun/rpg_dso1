from screen import Screen
import PySimpleGUI as sg


class ExplorerScreen(Screen):
    
    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self, text, commands):
        layout = [
            [sg.Text(text, **self.centralize(20), key="top", justification="center")],
            [sg.Text("", **self.centralize(5), key="commands")],
            [sg.Input(enable_events=True, size=(self.columns, 1), key="command")],
            [sg.Button("Continue", key="continue"), sg.Button("Return", key="return")]
        ]

        window = sg.Window("Explorer screen", layout=layout, **self.screen_configs).Finalize()
        window.Element("continue").Update(visible=False)
        window.Element("command").SetFocus()
        window.Maximize()

        def func_screen(window, commands):
            window.Element("return").Update(visible=True)
            event, values = window.Read()
            if event == "continue":
                return False, values["command"].replace(" ", "_")
            elif values["command"] in commands.keys():
                window.Element("command").Update(visible=False)
                window.Element("top").Update(commands[values["command"]]["consequence"])
                window.Element("continue").Update(visible=True)
                window.Element("return").Update(visible=False)
            elif values["command"] == "?":
                window.Element("commands").Update(" | ".join(commands.keys()))
            elif event == "return":
                return False, event

        return self.execute_screen(func_screen, window, commands)

