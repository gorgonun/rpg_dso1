from dao import Dao


class PlayerDao(Dao):

    def __init__(self, datasource="players.pickle"):
        super().__init__(datasource)

    def get_all(self):
        return [x for x in self.object_cache.values()]

    def get_dict(self):
        return self.object_cache

    def get(self, name):
        player = self.object_cache.get(name)
        if player:
            return player
        return player

    def get_char(self, player_name, char_name):
        for char in self.object_cache[player_name].characters:
            if char.name == char_name:
                return char

    def add_char(self, player, char):
        self.object_cache[player.name].new_character(char)
        self.update()

    def add_player(self, player):
        self.object_cache.update({player.name: player})
        self.update()

    def remove_player(self, player):
        self.object_cache.pop(player.name)
        self.update()

    def remove_char(self, player, char):
        player = self.get(player.name)
        player.remove(char)
        if len(player.characters) == 0:
            self.remove_player(player)
        self.update()

    def update_player(self, old_name, new_name, new_age):
        self.object_cache[old_name]["player"].name = new_name
        self.object_cache[old_name]["player"].age = new_age
        self.object_cache[new_name] = self.object_cache.pop(old_name)
        self.update()

    def save(self):
        self.update()
