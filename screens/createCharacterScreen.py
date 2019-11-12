from screen import Screen
from logging import Logger
import PySimpleGUI as sg


class CreateCharacterScreen(Screen):

    def __init__(self, log: Logger):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self, player=None, char=None):
        layout = [
            [sg.Text("Create a character")],
            [sg.Text("Name", size=(14, 1)), sg.Input(enable_events=True, key="player_name")],
            [sg.Text("Age", size=(14, 1)), sg.Input(enable_events=True, key="player_age")],
            [sg.Text("Character name", size=(14, 1)), sg.Input(enable_events=True, key="char_name")],
            [sg.Submit(), sg.Button("Cancel")]
        ]

        window = sg.Window("Character Creation", layout=layout, **self.screen_configs).Finalize()
        if player and char:
            window.Element("player_name").Update(player)
            window.Element("player_age").Update(player.age)
            window.Element("char_name").Update(char)
        window.Maximize()

        def func_screen(window):
            event, values = window.Read()
            if event == "Submit":
                if not self.validate_text(values["player_name"]):
                    window.Element("player_name").SetFocus()
                elif not self.validate_number(values["player_age"]):
                    window.Element("player_age").SetFocus()
                elif not self.validate_text(values["char_name"]):
                    window.Element("char_name").SetFocus()
                else:
                    return False, values
            elif event == "player_age":
                if len(values["player_age"]) > 0 and not self.validate_number(values["player_age"][-1]):
                    window.Element("player_age").Update(values["player_age"][:-1])
            elif event == "Cancel":
                return False, None
        
        return self.execute_screen(func_screen, window)

