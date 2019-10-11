from places import forest, village
from flux import flux
from place import Place
from screens import explorerScreen

class PlaceNotFoundException(Exception):
    pass


class PlaceController():

    def __init__(self, main_controller, log):
        self.__flux = flux
        self.__log = log
        self.__hc = main_controller
        self.__path = self.__flux[self.__hc.stage]["places"][self.__hc.placename]
        self.__place = self.get_instance(self.__hc.placename)()
        self.__text = self.__path["data"]["introduction"]
        self.__commands = self.__place.commands

    def do_action(self, action: list):
        consequences = getattr(self.__place, action)()
        char_update = self.__path["data"][action]

        self.__log.info("Start doing action %s", action)

        if self.__path["data"][action]["dead"]:
            self.__log.info("Character dead")
            return self.__hc.death()

        self.__hc.carma += char_update["carma"]
        self.__hc.show_text(self.__path["data"][action]["consequence"])

        self.__path = self.map_keys(self.__flux, consequences["next_place"])
        self.__hc.placename = self.__path["placename"]
        place_instance = consequences.get("place_instance")

        if place_instance:
            self.__log.info("New place instance: %s", self.__hc.placename)
            self.__place = self.get_instance(self.__hc.placename)()

        self.__commands = self.__place.commands
        self.__text = self.__path["data"]["introduction"]

    def explore(self):
        action = self.__hc.get_action(self.__text, self.__commands).replace(" ", "_")
        self.__log.info("Got action %s", action)
        return self.do_action(action)

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
            "forest": forest.forest,
            "village": village.Village}
        return places[place]
