from character import Character
from player import Player, CharacterAlreadyExistsError
import string
import random
from playerDao import PlayerDao


class PlayerController:

    def __init__(self, main_controller, log):
        self.__main_controller = main_controller
        self.__log = log
        self.__player_dao = PlayerDao()
        self.__characters = {}

    @property
    def players(self):
        return self.__player_dao.get_all()

    @property
    def complete_players(self):
        return self.__player_dao.get_dict()

    @property
    def player(self, name):
        return self.__player_dao.get(name)

    def add_to_player(self, player, char):
        player.new_character(char)
        self.__player_dao.add_char(player, char)

    @property
    def has_players(self):
        self.__log.info("Checking if it has players")
        return len(self.__player_dao.get_all()) > 0

    def update_player(self, old_name, new_name, new_age):
        self.__player_dao.update_player(old_name, new_name, new_age)

    def remove_player(self, player):
        self.__player_dao.remove_player(player)

    def remove_char(self, player, char):
        self.__player_dao.remove_char(player, char)

    def exists_player(self, name):
        self.__log.info("Checking if player %s exists", name)
        return self.__player_dao.get(name)

    def exists_character(self, player_name: str, char_name: str):
        self.__log.info("Checking if character %s exists", char_name)
        return self.__player_dao.get_char(player_name, char_name)

    def search_char(self, player_name: str, char_name: str):
        return self.__player_dao.get_char(player_name, char_name)

    def select(self, player_name: str, char_name: str):
        self.__log.info("Selecting char %s from player %s", char_name, player_name)
        return self.__player_dao.get(player_name), self.search_char(player_name, char_name)

    def create_character(self, player_name: str, player_age: int, char_name: str):
        self.__log.info("New player %s with age %s with char name %s", player_name, player_age, char_name)
        char = Character(char_name)
        player = self.__player_dao.get(player_name)

        if player and self.__player_dao.get(player_name).age == player_age:
            try:
                self.__player_dao.add_char(player, char)
            except CharacterAlreadyExistsError:
                return
            return player

        elif player and player.age != player_age:
            return

        new_player = Player(player_name=player_name, player_age=player_age, character=char)
        self.__player_dao.add_player(new_player)
        return new_player

    def populate(self):
        self.__log.info("Populating players to test")
        for x in range(10):
            name = "".join([string.ascii_lowercase[x] for x in range(0, random.randint(1, 10))])
            age = x
            char_name = "".join([string.ascii_lowercase[x] for x in range(0, random.randint(1, 10))])
            self.create_character(name, age, char_name)