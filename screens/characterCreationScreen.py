from screen import Screen
from logging import Logger

class CharacterCreationScreen(Screen):

    def __init__(self, main_controller, log: Logger):
        self.__main_controller = main_controller
        self.__log = log

    @property
    def log(self):
        return self.__log

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
        if self.__main_controller.check_if_exists_player(name):
            char_name = self.get_variable_input("Char name", str)
            if self.__main_controller.check_if_exists_char(player_name=name, char_name=char_name):
                return name, char_name
                # return self.__main_controller.select(player_name=name, char_name=char_name)

    def edit(self):
        name = self.get_variable_input("Player name", str)
        if self.__main_controller.check_if_exists_player(name):
            edit = lambda: "edit"
            exclude = lambda: "remove"
            menu = [("Edit player", edit), ("Remove player", exclude)]
            operation = self.get_menu_input("", menu)
            if operation == "edit":
                while True:
                    new_name = self.get_variable_input("New name", str)
                    if not self.__main_controller.check_if_exists_player(new_name):
                        new_age = self.get_variable_input("New age", int)
                        return self.__main_controller.update_player(name, new_name, new_age)
           
            elif operation == "remove":
                text = "Do you want to remove {}?".format(name)
                yes = lambda: "yes"
                no = lambda: "no"
                menu = [("Yes", yes), ("No", no)]
                if self.get_menu_input(text, menu) == "yes":
                    self.__main_controller.remove_player(name)
