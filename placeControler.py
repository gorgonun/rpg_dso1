from places import florest, noBearFlorest, northFlorest, village
from flux import flux
from place import Place

class PlaceNotFoundException(Exception):
    pass


class PlaceControler():

    def __init__(self):
        self.__flux = flux
        self.__carma = 0
        self.__stage = "stage1"
        self.__placename = "florest"
        self.__path = self.__flux[self.__stage]["places"][self.__placename]
        self.__place = self.get_instance(self.__placename)
        self.__text = self.__path["text"]
        self.__commands = self.__place.commands

    def do_action(self, action: list):
        consequences = getattr(self.__place, action)
        if consequences:
            for command, consequence in consequences().items():
                if command == "move":
                    self.__path = self.map_keys(self.__flux, consequence)
                    self.__placename = self.__path["placename"]
                    self.__place = self.get_instance(self.__placename)
                elif command == "carma":
                    self.__carma += consequence
                elif command == "key_deicision":
                    self.__key_decisions += consequence
                elif command == "imediate_consequence":
                    print(consequence)
        self.__commands = self.__place.commands
        self.__text = self.__path["text"]

    def print_possible_actions(self):
        print("commands", self.__place.commands)

    def print_text(self):
        print(self.__text)

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
            "florest": florest.Florest(),
            "nobear": noBearFlorest.NoBearFlorest(),
            "north": northFlorest.NorthFlorest(),
            "village": village.Village()}
        return places[place]

hc = PlaceControler()
input1 = "move_north"
input2 = "push_him_away"

hc.print_text()
hc.do_action(input1)
hc.print_text()
hc.do_action(input2)