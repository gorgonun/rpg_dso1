from character import Character
from player import Player, CharacterAlreadyExistsError
import string
import random

class PlayerController:

    def __init__(self, main_controller, log):
        self.__main_controller = main_controller
        self.__log = log
        self.__players = {}
        self.__characters = {}

    @property
    def players(self):
        return [x["player"] for x in self.__players.values()]

    @property
    def complete_players(self):
        return self.__players

    @property
    def player(self, name):
        return self.__players.get(name)["player"]

    def add_to_player(self, player, char):
        player.new_character(char)

    @property
    def has_players(self):
        self.__log.info("Checking if it has players")
        return len(self.__players) > 0

    def update_player(self, old_name, new_name, new_age):
        self.__players[old_name]["player"].name = new_name
        self.__players[old_name]["player"].age = new_age
        self.__players[new_name] = self.__players.pop(old_name)

    def remove_player(self, name):
        self.__players.pop(name)

    def remove_char(self, player, char):
        self.__players.get(player.name)["characters"].remove(char)
        if len( self.__players.get(player.name)["characters"]) == 0:
            self.remove_player(player.name)

    def exists_player(self, name):
        self.__log.info("Checking if player %s exists", name)
        return self.__players.get(name, False)

    def exists_character(self, player_name: str, char_name: str):
        self.__log.info("Checking if character %s exists", char_name)
        if self.search_char(player_name, char_name):
            return True

    def search_char(self, player_name: str, char_name: str):
        for char in self.__players[player_name]["characters"]:
            if char.name == char_name:
                return char
    
    def select(self, player_name: str, char_name: str):
        self.__log.info("Selecting char %s from player %s", char_name, player_name)
        return self.__players[player_name]["player"], self.search_char(player_name, char_name)

    def create_character(self, player_name: str, player_age: int, char_name: str):
        self.__log.info("New player %s with age %s with char name %s", player_name, player_age, char_name)
        char = Character(char_name)

        if self.__players.get(player_name) and self.__players.get(player_name)["player"].age == player_age:
            try:
                self.add_to_player(self.__players[player_name]["player"], char)
            except CharacterAlreadyExistsError:
                return
            return self.__players[player_name]["player"]
        
        elif self.__players.get(player_name) and self.__players.get(player_name)["player"].age != player_age:
            return

        player = Player(player_name=player_name, player_age=player_age, character=char)
        self.__players.update({player_name: {"player": player, "characters": player.characters}})
        return player

    def populate(self):
        self.__log.info("Populating players to test")
        for x in range(10):
            name = "".join([string.ascii_lowercase[x] for x in range(0, random.randint(1, 10))])
            age = x
            char_name = "".join([string.ascii_lowercase[x] for x in range(0, random.randint(1, 10))])
            self.create_character(name, age, char_name)
