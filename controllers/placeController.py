from places import florest, noBearFlorest, northFlorest, village
from flux import flux
from place import Place
from screens import explorerScreen

class PlaceNotFoundException(Exception):
    pass


class PlaceController():

    def __init__(self, history_controller):
        self.__flux = flux
        self.__hc = history_controller

        self.__path = self.__flux[self.__hc.stage]["places"][self.__hc.placename]
        self.__place = self.get_instance(self.__hc.placename)
        self.__text = self.__path["text"]
        self.__commands = self.__place.commands

    def do_action(self, action: list):
        consequences = getattr(self.__place, action)
        if consequences:
            for command, consequence in consequences().items():
                if command == "move":
                    self.__path = self.map_keys(self.__flux, consequence)
                    self.__hc.placename = self.__path["placename"]
                    self.__place = self.get_instance(self.__hc.placename)
                elif command == "carma":
                    self.__hc.carma += consequence
                elif command == "key_deicision":
                    self.__hc.key_decisions += consequence
                elif command == "imediate_consequence":
                    self.__hc.show_text(consequence)
        self.__commands = self.__place.commands
        self.__text = self.__path["text"]

    def explore(self):
        action = self.__hc.get_action(self.__text, self.__commands).replace(" ", "_")
        self.do_action(action)

    def map_keys(self, original_dict: dict, list_map: list):
        place = original_dict
        for key in list_map:
            next = place.get(key)
            if not next:
                raise PlaceNotFoundException
            place = next
        return place
    
    def get_instance(self, place):
        places = {
            "florest": florest.Florest,
            "nobear": noBearFlorest.NoBearFlorest,
            "north": northFlorest.NorthFlorest,
            "village": village.Village}
        return places[place]()
