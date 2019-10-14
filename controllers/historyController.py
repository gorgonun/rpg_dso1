from controllers.placeController import PlaceController
from controllers.screenController import ScreenController
from controllers.playerController import PlayerController

class HistoryController():

    def __init__(self, log):
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
    def placename(self, placename):
        if placename is not None:
            self.__placename = placename

    def create_character(self, player_name: str, player_age: int, char_name: str):
        player = self.__player_controller.create_character(player_name=player_name, player_age=player_age, char_name=char_name)
        if not player:
            return
        self.__character = player.character(char_name)
        self.__player = player
        return player

    def check_if_exists_player(self, name):
        return self.__player_controller.exists_player(name)

    def check_if_exists_char(self, player_name: str, char_name:str):
        return self.__player_controller.exists_character(player_name=player_name, char_name=char_name)
    
    def select(self, player_name: str, char_name: str):
        return self.__player_controller.select(player_name=player_name, char_name=char_name)

    def create_character_screen(self):
        self.__screen_controller.create_character_screen()

    def create_select_screen(self):
        result = self.__screen_controller.create_select_screen()
        if not result:
            self.__log.info("Got no result while searching for char")
            return self.create_character_screen()
        self.__player = result[0]
        self.__character = result[1]

    def start_adventure(self):
        self.__log.info("Starting game")
        if not self.__player or self.__character.dead:
            self.__log.info("No player detected for this game. Redirecting to player creation/selection screen.")
            self.create_select_screen()

        self.__character.reset()
        self.__place_controller.reset()
        while not self.__character.dead:
            self.__place_controller.explore()

    def show_text(self, text):
        self.__screen_controller.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__screen_controller.get_action(text, commands)

    def start_game(self):
        text = "Start menu"
        start = lambda: "start_game"
        create = lambda: "create_character"
        list_created = lambda: "list_created"
        ranking = lambda: self.show_ranking(); self.start_game
        edit = lambda: self.edit(); self.start_game
        exit_f = lambda: self.__log.info("exiting"); exit
        menu = [("Start game", start), ("Create character", create)]
        
        if self.__player_controller.has_players:
            menu.append(("List players created", list_created))
            menu.append(("Edit players", edit))
            menu.append(("Show ranking", ranking))

        menu.append(("Exit", exit))
        menu_option = self.__screen_controller.start_screen(text, menu)
        
        if menu_option == "start_game":
            return self.start_adventure()
        
        elif menu_option == "create_character":
            self.create_character_screen()
            return self.start_game()
        
        elif menu_option == "list_created":
            self.list_created()
            return self.start_game()

    def show_ranking(self):
        players = self.__player_controller.complete_players
        player_dict = {key: value["characters"] for key, value in players.items()}
        self.__screen_controller.show_ranking(player_dict)

    def list_created(self):
        players = self.__player_controller.players
        self.__screen_controller.list_created(players)

    def test_mode(self):
        self.__player_controller.populate()

    def death(self):
        self.__log.info("End game")
        self.reset_adventure()
        return self.start_game()

    def update_game(self, death: bool, carma: int, transition_text: str, new_place: str, key_decision: str):
        self.show_text(transition_text)
        self.placename = new_place
        self.__character.carma = carma
        self.__character.dead = death
        if key_decision:
            self.__character.key_decisions = key_decision

    def update_player(self, old_name, new_name, new_age):
        self.__player_controller.update_player(old_name, new_name, new_age)

    def remove_player(self, name):
        self.__player_controller.remove_player(name)
        if self.__player and self.__player.name == name:
            self.__player = None
            self.__character = None

    def edit(self):
        return self.__screen_controller.edit()

    def reset_adventure(self):
        self.__log.info("Reseting adventure")
        self.placename = "forest"
        #TODO: do it in character
        self.carma = 0
        self.key_decisions = []
        self.__place_controller = PlaceController(self, self.__log)
        self.__screen_controller = ScreenController(self, self.__log)
        self.__log.info("Reset complete")
