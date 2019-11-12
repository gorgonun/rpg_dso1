from screens.startScreen import StartScreen
from screens.explorerScreen import ExplorerScreen
from screens.characterScreen import CharacterScreen
from screens.rankingScreen import RankingScreen
from screens.createCharacterScreen import CreateCharacterScreen

class ScreenController():

    def __init__(self, main_controller, log):
        self.__log = log
        self.__explorer_screen = ExplorerScreen(log)
        self.__start_screen = StartScreen(log)
        self.__character_creation_screen = CharacterScreen(self, log)
        self.__ranking_screen = RankingScreen(log)
        self.__create_character_screen = CreateCharacterScreen(log)
        self.__main_controller = main_controller
        self.__screen = ["main_character_screen"]

    @property
    def screen(self):
        if len(self.__screen) > 0:
            return self.__screen[0]
        return self.__screen

    @screen.setter
    def screen(self, next):
        if next not in self.__screen:
            self.__screen.append(next)

    def back(self):
        self.__screen = self.__screen[:-1]
        if not self.screen:
            return 0
        self.screen_manager()

    def screen_manager(self, **kwargs):
        if len(self.__screen) == 0:
            return 0
        elif self.screen == "main_character_screen":
            return self.main_character_screen(**kwargs)

    def show_text(self, text: str):
        self.__explorer_screen.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__explorer_screen.start(text, commands)

    def start_screen(self, text, menu):
        return self.__start_screen.start(text, menu)

    def main_character_screen(self, players: list, player, character):
        result = self.__character_creation_screen.start(players, player, character)
        if result in (None, "Exit") or not result["option"]:
            return self.back()
        elif result["option"] == "Create":
            return self.create_character()
        elif result["option"] == "Select":
            return self.__main_controller.select(result["values"]["player"], result["values"]["char"])
        elif result["option"] == "Edit":
            self.create_character(result["values"]["player"], result["values"]["char"], self.__main_controller.remove_char, result["values"]["player"], result["values"]["char"])
        elif result["option"] == "Remove player":
            self.__main_controller.remove_player(result["values"]["player"].name)
        elif result["option"] == "Remove character":
            self.__main_controller.remove_char(result["values"]["player"], result["values"]["char"])

    def create_character(self, player=None, char=None, before_creation=None, *args):
        char = self.__create_character_screen.start(player=player, char=char)
        if not char:
            return None
        elif before_creation:
            before_creation(*args)
        return self.__main_controller.create_character(**char)

    def create_select_screen(self):
        return self.__character_creation_screen.create_select()

    def is_valid_player(self, name):
        return self.__main_controller.is_valid_player(name)

    def is_valid_char(self, player_name: str, char_name: str):
        return self.__main_controller.is_valid_char(player_name=player_name, char_name=char_name)

    def update_player(self, old_name: str, new_name: str, new_age: int):
        return self.__main_controller.update_player(old_name, new_name, new_age)

    def remove_player(self, name):
        return self.__main_controller.remove_player(name)

    def edit(self):
        return self.__character_creation_screen.edit()

    def show_ranking(self, players_dict: dict):
        return self.__ranking_screen.show_ranking(players_dict)
