from controllers.placeController import PlaceController
from screens.explorerScreen import ExplorerScreen

class HistoryController():

    def __init__(self):
        self.stage = "stage1"
        self.placename = "florest"
        #TODO: do it in character
        self.carma = 0
        self.key_decisions = []
        self.__explorer_screen = ExplorerScreen()
        self.__place_controller = PlaceController(self)
    
    def explore(self):
        while True:
            self.__place_controller.explore()

    def show_text(self, text):
        self.__explorer_screen.show_text(text)
    
    def get_action(self, text: str, commands: list):
        return self.__explorer_screen.get_action(text, commands)

HistoryController().explore()