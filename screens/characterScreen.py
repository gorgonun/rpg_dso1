from screen import Screen
from logging import Logger
import PySimpleGUI as sg


class CharacterScreen(Screen):

    def __init__(self, main_controller, log: Logger):
        self.__main_controller = main_controller
        self.__log = log

    @property
    def log(self):
        return self.__log

    def start(self, players: list, player, character):
        layout = [
            [sg.Text("Player: ", key="actual_player_name"), sg.Text("Character: ", key="actual_char_name")],
            [sg.Text("Players")],
            [sg.Listbox(values=players, enable_events=True, key="player", size=(20, 20)), sg.Listbox(values=[], enable_events=True, size=(20, 20), key="char")],
            [sg.Button('Select'), sg.Button('Create'), sg.Button('Edit'), sg.Button('Remove'), sg.Button('Exit')]
        ]

        window = sg.Window("Character Selection", layout=layout, **self.screen_configs).Finalize()
        window.Element("char").Update(visible=False)
        window.Element("actual_player_name").Update(visible=False)
        window.Element("actual_char_name").Update(visible=False)
        window.Maximize()

        def func_screen(window):
            def check_selection(values, opt_char):
                return (len(values["player"]) > 0 and
                        (len(values["char"]) > 0 or opt_char) and
                        self.__main_controller.is_valid_player(values["player"][0].name) and
                        self.__main_controller.is_valid_char(values["player"][0].name, values["char"][0].name))
            if player and character:
                window.Element("actual_char_name").Update(visible=True)
                window.Element("actual_char_name").Update(player.name)
                window.Element("actual_player_name").Update(visible=True)
                window.Element("actual_player_name").Update(character.name)
            event, values = window.Read()
            if event == "player" and len(values["player"]) > 0:
                window.Element("char").Update(values['player'][0].characters)
                window.Element("char").Update(visible=True)
            elif event == "Create":
                return False, {"option": event}
            elif event in ('Select', 'Edit', 'Remove'):
                opt_char = event == "Remove"
                if check_selection(values, opt_char):
                    if opt_char:
                        event = self.remove(values, opt_char)
                    return False, {"option": event, "values": {key: value[0] for key, value in values.items()}}
            elif event == "Exit":
                return False, None
        return self.execute_screen(func_screen, window)

    def remove(self, values, has_char):
        simplePopupLayout = [
            [sg.Button("Remove player"), sg.Button("Remove character")]
        ]

        if has_char:
            event, _ = self.popup("Remove", simplePopupLayout)
        else:
            event = "Remove player"

        target_name = values['player'][0].name if event == "Remove player" else values['char'][0].name
        confirmation = sg.popup_yes_no("Do you really want to remove {}?".format(target_name))
        if confirmation == "Yes":
            return event

    def popup(self, title, layout):
        window = sg.Window(title, layout=layout)

        def func_screen(window):
            event, values = window.Read()
            return False, (event, values)

        return self.execute_screen(func_screen, window)
