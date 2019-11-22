from controllers.placeController import PlaceController
from controllers.screenController import ScreenController
from controllers.playerController import PlayerController
from logging import Logger
from exceptions import CannotStartGameError


class HistoryController:

    def __init__(self, log: Logger):
        self.__log = log
        self.__player = None
        self.__character = None
        self.__placename = "forest"
        self.__place_controller = PlaceController(self, self.__log)
        self.__screen_controller = ScreenController(self, self.__log)
        self.__player_controller = PlayerController(self, self.__log)

    @property
    def placename(self):
        return self.__placename
    
    @placename.setter
    def placename(self, placename: str):
        if placename is not None:
            self.__log.info("History place changed to %s", placename)
            self.__placename = placename

    def start_game(self):
        return self.__screen_controller.start_screen()

    def main_character_screen(self):
        players = self.__player_controller.players
        return players, self.__player, self.__character

    def select(self, player, char):
        self.__player = player
        self.__character = char

    def check_player_status(self):
        if not self.__player or self.__character.dead:
            raise CannotStartGameError

    def start_adventure(self):
        self.__log.info("Starting game")

        try:
            self.check_player_status()
        except CannotStartGameError:
            self.__log.info("No player detected for this game or character is dead. Redirecting to player creation/selection screen.")
            self.__screen_controller.main_character_screen()

        self.reset_adventure()
        self.__place_controller.reset()

        while not self.__character.dead and self.__screen_controller.screen == "exploration":
            self.__place_controller.explore()
        if self.__character.dead:
            self.__screen_controller.back()
            self.death()

    def create_character(self, player_name: str, player_age: str, char_name: str):
        player = self.__player_controller.create_character(player_name=player_name, player_age=int(player_age), char_name=char_name)

        if player:
            self.__character = player.character(char_name)
            self.__player = player
            return player, player.character(char_name)

    def show_ranking(self):
        self.__log.info("Showing ranking")
        players = self.__player_controller.complete_players
        player_dict = {key: value.characters for key, value in players.items()}
        self.__screen_controller.show_ranking(player_dict)

    def get_action(self, text: str, commands: list):
        return self.__screen_controller.get_action(text, commands)

    def update_game(self, death: bool, carma: int, new_place: str, key_decision: str):
        self.placename = new_place
        self.__character.carma = carma
        self.__character.dead = death
        if key_decision:
            self.__character.key_decisions = key_decision
        self.__player_controller.save()

    def is_valid_player(self, name: str):
        return self.__player_controller.exists_player(name)

    def is_valid_char(self, player_name: str, char_name:str):
        return self.__player_controller.exists_character(player_name=player_name, char_name=char_name)
    
    def update_player(self, old_name: str, new_name: str, new_age: str):
        self.__player_controller.update_player(old_name, new_name, new_age)

    def remove_player(self, name: str):
        self.__log.info("Removing player %s", name)
        self.__player_controller.remove_player(name)
        if self.__player and self.__player.name == name:
            self.__player = None
            self.__character = None

    def remove_char(self, player, char):
        self.__log.info("Removing char %s from player %s", player.name, char.name)
        self.__player_controller.remove_char(player, char)
        if self.__character and self.__character.name == char.name:
            self.__character = None
        if self.__player and not self.__player_controller.exists_player(player.name):
            self.__player = None

    def death(self):
        self.__log.info("End game")

    def reset_adventure(self):
        self.__log.info("Reseting adventure")
        self.placename = "forest"
        self.__place_controller = PlaceController(self, self.__log)
        self.__screen_controller = ScreenController(self, self.__log)
        self.__screen_controller.screen = "start"
        self.__screen_controller.screen = "exploration"
        self.__log.info("Reset complete")

    def test_mode(self):
        self.__log.info("Populating")
        self.__player_controller.populate()
