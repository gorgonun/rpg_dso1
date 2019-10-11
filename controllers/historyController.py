from controllers.placeController import PlaceController
from controllers.screenController import ScreenController

class HistoryController():

    def __init__(self, log):
        self.__log = log
        self.stage = "stage1"
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
        return dead

    def show_text(self, text):
        self.__screen_controller.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__screen_controller.get_action(text, commands)

    def start_game(self):
        menu_option = self.__screen_controller.start_screen()
        if menu_option == "start_game":
            return self.start_adventure()

    def death(self):
        self.__log.info("End game")
        # final screen
        return 0
