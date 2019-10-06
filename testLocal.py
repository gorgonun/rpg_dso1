from abc import ABC, abstractmethod
from flux import flux

class Place(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @property
    @abstractmethod
    def commands(self):
        return self.__commands.keys()

    @property
    @abstractmethod
    def full_path(self):
        pass

    @property
    def root(self):
        return self.as_list(self.full_path)[0]

    @property
    def top(self):
        return self.as_list(self.full_path)[-1]

    def as_list(self, string: str):
        incomplete_list = list(map(lambda x: [x, "places"], string.split(" ")))
        return [item for sublist in incomplete_list for item in sublist][:-1]


class Florest(Place):

    def __init__(self):
        self.__full_path = "stage1 florest"
        self.__commands = ["move north", "move south"]

    def move_north(self):
        return {"move": self.as_list(self.full_path + " stone"), "imediate_consequence": "You walk"}

    @property
    def full_path(self):
        return self.__full_path

    @property
    def commands(self):
        return self.__commands


class Stone(Place):

    def __init__(self):
        self.__full_path = "stage1 florest stone"
        self.__commands = "kill friend"

    def kill_friend(self):
        return {"carma": -1, "move": self.as_list(self.root + " village"), "key_decision": "1", "imediate_consequence": "You kill a friend"}

    @property
    def full_path(self):
        return self.__full_path

    @property
    def commands(self):
        return self.__commands


class Village(Place):

    def __init__(self):
        self.__full_path = "stage1 village"
        self.__commands = "1"

    def kill_friend(self):
        return {"carma": -1, "move": self.root + " village"}

    @property
    def full_path(self):
        return self.__full_path

    @property
    def commands(self):
        return self.__commands

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
        places = {"florest": Florest(), "stone": Stone(), "village": Village()}
        return places[place]


hc = PlaceControler()
input1 = "move_north"
input2 = "kill_friend"

hc.print_text()
hc.print_possible_actions()
hc.do_action(input1)
hc.print_text()
hc.print_possible_actions()
hc.do_action(input2)
