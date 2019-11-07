class CharacterAlreadyExistsError(Exception):
    pass

class Player:

    def __init__(self, player_name: str, player_age: int, character):
        self.__name = player_name
        self.__age = player_age
        self.__characters = {character.name: character}

    def new_character(self, character):
        if self.__characters.get(character.name):
            raise CharacterAlreadyExistsError
        self.__characters[character.name] = character

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def characters(self):
        return list(self.__characters.values())

    def character(self, name):
        return self.__characters.get(name)

    def __len__(self):
        return len(self.__name)

    def __str__(self):
        return self.__name