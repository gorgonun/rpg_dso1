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
        self.__main_controller = main_controller
        self.__path = self.__flux[self.__main_controller.placename]
        self.__place = self.get_instance(self.__main_controller.placename)()

    @property
    def text(self):
        return self.__path["data"]["introduction"]

    def do_action(self, action: str):
        consequences = getattr(self.__place, action)()
        char_update = self.__path["data"][action]

        self.__log.info("Start doing action %s", action)

        self.__main_controller.update_game(death=char_update["dead"], carma=char_update["carma"], new_place=self.__path["placename"], transiction_text=char_update["consequence"])

        self.__path = self.map_keys(self.__flux, consequences["next_place"])
        place_instance = consequences.get("place_instance")

        if place_instance:
            self.__log.info("New place instance: %s", self.__main_controller.placename)
            self.__place = self.get_instance(self.__main_controller.placename)()

    def explore(self):
        action = self.__main_controller.get_action(self.text, self.__place.commands).replace(" ", "_")
        self.__log.info("Got action %s", action)
        return self.do_action(action)

    def map_keys(self, original_dict: dict, list_map: list):
        place = original_dict
        for key in list_map:
            print(key, original_dict)
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
