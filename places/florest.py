from place import Place

class Florest(Place):

    def __init__(self):
        self.__full_path = "stage1 florest"
        self.__commands = ["move north", "move south"]

    def move_north(self):
        return {"move": self.as_list(self.full_path + " north"), "imediate_consequence": "You walk"}

    @property
    def full_path(self):
        return self.__full_path

    @property
    def commands(self):
        return self.__commands
