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
            [sg.Listbox(values=players, enable_events=True, key="player", size=(20, 20)), sg.Listbox(values=[], enable_events=True, key="char", size=(20, 20))],
            [sg.Button('Select'), sg.Button('Create'), sg.Button('Edit'), sg.Button('Remove'), sg.Button('Exit')]
        ]

        window = sg.Window("Character Selection", layout=layout, **self.screen_configs).Finalize()
        window.Element("char").Update(visible=False)
        window.Element("actual_player_name").Update(visible=False)
        window.Element("actual_char_name").Update(visible=False)
        window.Maximize()

        def func_screen(window):
            if player and character:
                window.Element("actual_char_name").Update(visible=True)
                window.Element("actual_char_name").Update(player.name)
                window.Element("actual_player_name").Update(visible=True)
                window.Element("actual_player_name").Update(character.name)
            event, values = window.Read()
            if event in (None, 'Exit'):
                return False, None
            elif event == "player" and len(values["player"]) > 0:
                window.Element("char").Update(values['player'][0].characters)
                window.Element("char").Update(visible=True)
            elif event == "Create":
                return False, {"option": event}
            elif event == 'Select':
                print(event, values)
                if len(values["player"]) > 0\
                        and len(values["char"]) > 0\
                        and self.__main_controller.is_valid_player(values["player"][0].name)\
                        and self.__main_controller.is_valid_char(values["player"][0].name, values["char"][0].name):
                    return False, {"option": event, "values": {key: value[0] for key, value in values.items()}}
        return self.execute_screen(func_screen, window)

    def create_character(self):
        self.print_centralized("Creating new character")
        name = self.get_variable_input("Player name", str)
        age = int(self.get_variable_input("Age", int))
        char_name = self.get_variable_input("Char name", str)
        return name, age, char_name

    def list_created(self, players: list):
        template = "{:<20}|{:<3}|{:<10}|{:>20}s"
        menu = [("Exit", lambda: 0)]
        lines = []
        lines.append(template.format("Player name", "Age", "Char name", "Char played time"))

        for player in players:
            lines.append(template.format(player.name, player.age, player.characters[0].name, player.characters[0].time_played))

            for char in player.characters[1:]:
                lines.append(template.format("↳", player.age, char.name, char.time_played))
        formated_top = self.format_centralized("Created players", "-")
        formated_template = "\n".join(lines)
        formated_bottom = self.format_centralized("", '-')
        formated_screen = "{}\n{}\n{}\n".format(formated_top, formated_template, formated_bottom)
        return self.print_wait_confimation(formated_screen)

    def create_select(self):
        name = self.get_variable_input("Player name", str)
        if self.__main_controller.is_valid_player(name):
            char_name = self.get_variable_input("Char name", str)
            if self.__main_controller.is_valid_char(player_name=name, char_name=char_name):
                return name, char_name

    def edit(self):
        name = self.get_variable_input("Player name", str)
        if self.__main_controller.is_valid_player(name):
            edit = lambda: "edit"
            exclude = lambda: "remove"
            menu = [("Edit player", edit), ("Remove player", exclude)]
            operation = self.get_menu_input("", menu)
            if operation == "edit":
                while True:
                    new_name = self.get_variable_input("New name", str)
                    if not self.__main_controller.is_valid_player(new_name):
                        new_age = self.get_variable_input("New age", int)
                        return self.__main_controller.update_player(name, new_name, new_age)
           
            elif operation == "remove":
                text = "Do you want to remove {}?".format(name)
                yes = lambda: "yes"
                no = lambda: "no"
                menu = [("Yes", yes), ("No", no)]
                if self.get_menu_input(text, menu) == "yes":
                    self.__main_controller.remove_player(name)
