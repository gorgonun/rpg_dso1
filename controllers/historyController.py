from controllers.placeController import PlaceController
from controllers.screenController import ScreenController

class HistoryController():

    def __init__(self, log):
        self.__log = log
        self.placename = "forest"
        #TODO: do it in character
        self.carma = 0
        self.key_decisions = []
        self.__place_controller = PlaceController(self, self.__log)
        self.__screen_controller = ScreenController(self, self.__log)

    def start_adventure(self):
        self.__log.info("Starting game")
        dead = False
        while not dead:
            dead = self.__place_controller.explore()

    def show_text(self, text):
        self.__screen_controller.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__screen_controller.get_action(text, commands)

    def start_game(self):
        text = "Start menu"
        start = lambda: "start_game"
        create = lambda: "create_character"
        menu = [("Start game", start), ("Create character", create), ("Exit", exit)]
        menu_option = self.__screen_controller.start_screen(text, menu)
        if menu_option == "start_game":
            return self.start_adventure()

    def death(self):
        self.__log.info("End game")
        # final screen
        # save character
        self.reset_adventure()
        self.start_game()

    def update_game(self, death: bool, carma: int, transition_text: str, new_place: str):
        self.show_text(transition_text)
        self.placename = new_place

    def reset_adventure(self):
        self.__log.info("Reseting adventure")
        self.placename = "forest"
        #TODO: do it in character
        self.carma = 0
        self.key_decisions = []
        self.__place_controller = PlaceController(self, self.__log)
        self.__screen_controller = ScreenController(self, self.__log)
        self.__log.info("Reset complete")
