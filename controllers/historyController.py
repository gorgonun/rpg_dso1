from controllers.placeController import PlaceController
from controllers.screenController import ScreenController
from controllers.playerController import PlayerController
from logging import Logger

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
        self.__screen_controller.screen = "exploration"
        self.start_adventure()
        # self.__log.info("Starting menu")
        # text = "Start menu\n"
        # start = lambda: self.start_adventure()
        # create = lambda: self.create_character()
        # list_created = lambda: self.list_created()
        # ranking = lambda: self.show_ranking()
        # edit = lambda: self.edit()
        # exit_f = lambda: "exit"
        # menu = [("Start game", start), ("Create character", create)]
        
        # if self.__player_controller.has_players:
        #     menu.append(("List players created", list_created))
        #     menu.append(("Edit players", edit))
        #     menu.append(("Show ranking", ranking))

        # menu.append(("Exit", exit_f))
        # result = self.__screen_controller.start_screen(text, menu)

        # if result == "exit":
        #     return 0

    def main_character_screen(self):
        players = self.__player_controller.players
        return self.__screen_controller.screen_manager(players=players, player=self.__player, character=self.__character)

    def select(self, player, char):
        self.__player = player
        self.__character = char

    def create_select_screen(self):
        result = self.__screen_controller.create_select_screen()

        if not result:
            self.__log.info("Got no result while searching for char")
            return self.create_character()

        result = self.__player_controller.select(player_name=result[0], char_name=result[1])
        self.__player = result[0]
        self.__character = result[1]

    def start_adventure(self):
        self.__log.info("Starting game")
        
        if not self.__player or self.__character.dead:
            self.__log.info("No player detected for this game or character is dead. Redirecting to player creation/selection screen.")
            self.main_character_screen()

        self.reset_adventure()
        self.__character.reset()
        self.__place_controller.reset()
        
        while not self.__character.dead:
            self.__place_controller.explore()
        self.death()

    def create_character(self, player_name: str, player_age: int, char_name: str):
        player = self.__player_controller.create_character(player_name=player_name, player_age=player_age, char_name=char_name)

        if player:
            self.__character = player.character(char_name)
            self.__player = player
            return player, player.character(char_name)


    # def list_created(self):
    #     self.__log.info("Showing created characters")
    #     players = self.__player_controller.players
    #     self.__screen_controller.list_created(players)

    def edit(self):
        self.__log.info("At edit screen")
        self.__screen_controller.edit()

    def show_ranking(self):
        self.__log.info("Showing ranking")
        players = self.__player_controller.complete_players
        player_dict = {key: value["characters"] for key, value in players.items()}
        self.__screen_controller.show_ranking(player_dict)

    def show_text(self, text: str):
        self.__screen_controller.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__screen_controller.get_action(text, commands)

    def update_game(self, death: bool, carma: int, transition_text: str, new_place: str, key_decision: str):
        self.show_text(transition_text)
        self.placename = new_place
        self.__character.carma = carma
        self.__character.dead = death
        if key_decision:
            self.__character.key_decisions = key_decision

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
        self.__log.info("Reset complete")

    def test_mode(self):
        self.__log.info("Populating")
        self.__player_controller.populate()
