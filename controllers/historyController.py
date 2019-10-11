from controllers.placeController import PlaceController
from controllers.screenController import ScreenController
import logging

class HistoryController():

    def __init__(self):
        self.__log = logging.getLogger("log")
        self.__log.addHandler(logging.FileHandler("log.log", "a"))
        self.__log.setLevel(logging.DEBUG)
        self.stage = "stage1"
        self.placename = "forest"
        #TODO: do it in character
        self.carma = 0
        self.key_decisions = []
        self.__place_controller = PlaceController(self, self.__log)
        self.__screen_controller = ScreenController(self, self.__log)

    def start_game(self):
        self.__log.info("Starting game")
        while True:
            self.__place_controller.explore()

    def show_text(self, text):
        self.__screen_controller.show_text(text)

    def get_action(self, text: str, commands: list):
        return self.__screen_controller.get_action(text, commands)

    def start_screen(self):
        self.__screen_controller.start_screen()
