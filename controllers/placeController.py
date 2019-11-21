from places import forest, village
from flux import flux
from logging import Logger

class PlaceNotFoundException(Exception):
    pass


class PlaceController():

    def __init__(self, main_controller, log: Logger):
        self.__flux = flux
        self.__log = log
        self.__main_controller = main_controller
        self.__path = self.__flux[self.__main_controller.placename]
        self.__place = self.get_instance(self.__main_controller.placename)()

    @property
    def text(self):
        return self.__path["data"]["introduction"]
    
    def reset(self):
        self.__path = self.__flux[self.__main_controller.placename]
        self.__place = self.get_instance(self.__main_controller.placename)()

    def do_action(self, action: str):
        if not action:
            return
        consequences = getattr(self.__place, action)()
        char_update = self.__path["data"][action]

        self.__log.info("Start doing action %s", action)

        self.__main_controller.update_game(death=char_update["dead"], carma=char_update["carma"], new_place=consequences["place_instance"], key_decision=char_update["key_decision"])

        self.__path = self.map_keys(self.__flux, consequences["next_place"])
        place_instance = consequences.get("place_instance")

        if place_instance:
            self.__log.info("New place instance: %s", self.__main_controller.placename)
            self.__place = self.get_instance(self.__main_controller.placename)()

    def explore(self):
        action = self.__main_controller.get_action(self.text, {key: self.__path["data"][key.replace(" ", "_")] for key in self.__place.commands.keys()})
        self.__log.info("Got action %s", action)
        if action:
            return self.do_action(action)

    def map_keys(self, original_dict: dict, list_map: list):
        place = original_dict
        for key in list_map:
            next = place.get(key)
            if not next:
                raise PlaceNotFoundException("Key {} not found in flux".format(key))
            place = next
        return place
    
    def get_instance(self, place: str):
        places = {
            "forest": forest.Forest,
            "village": village.Village}
        return places[place]
