from screen import Screen
from logging import Logger
from datetime import datetime
import PySimpleGUI as sg

class RankingScreen(Screen):

    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log
    
    def start(self, player_dict):

        string=""
        for key in player_dict.keys():
            
            string += key
            string += " "
            for character in player_dict[key]:
                key_decision = "" if not character.key_decisions else character.key_decisions[0]
                string += character.name
                string += " "
                string += str(character.time_played)
                string += " "
                string += str(key_decision)
                string += "\n"
            string += "\n"

        layout = [
            [sg.Multiline(default_text=string, size=(35, 10))],
            [sg.Button('Return')]
        ]

        window = sg.Window('Ranking', **self.screen_configs).Layout(layout).Finalize()
        window.Maximize()

        def func_screen(window):
                event, values = window.Read()
                if event in (None, 'Return'):
                    return False, None
                else:
                    return False, event
            
        return self.execute_screen(func_screen, window)

