from screens.startScreen import StartScreen
from screens.explorerScreen import ExplorerScreen
from screens.characterCreationScreen import CharacterCreationScreen
from screens.rankingScreen import RankingScreen

class ScreenController():

    def __init__(self, main_controller, log):
        self.__log = log
        self.__explorer_screen = ExplorerScreen(log)
        self.__start_screen = StartScreen(log)
        self.__character_creation_screen = CharacterCreationScreen(self, log)
        self.__ranking_screen = RankingScreen(log)
        self.__main_controller = main_controller

    def show_text(self, text: str):
        self.__explorer_screen.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__explorer_screen.get_action(text, commands)

    def start_screen(self, text, menu):
        return self.__start_screen.start(text, menu)

    def create_character(self):
        return self.__character_creation_screen.create_character()

    def list_created(self, players):
        return self.__character_creation_screen.list_created(players)

    def create_select_screen(self):
        return self.__character_creation_screen.create_select()

    def check_if_exists_player(self, name):
        return self.__main_controller.check_if_exists_player(name)

    def check_if_exists_char(self, player_name: str, char_name: str):
        return self.__main_controller.check_if_exists_char(player_name=player_name, char_name=char_name)

    # def select(self, player_name: str, char_name: str):
        # return player_name, char_name
        # return self.__main_controller.select(player_name=player_name, char_name=char_name)

    def update_player(self, old_name: str, new_name: str, new_age: int):
        return self.__main_controller.update_player(old_name, new_name, new_age)

    def remove_player(self, name):
        return self.__main_controller.remove_player(name)

    def edit(self):
        return self.__character_creation_screen.edit()

    def show_ranking(self, players_dict: dict):
        return self.__ranking_screen.show_ranking(players_dict)
