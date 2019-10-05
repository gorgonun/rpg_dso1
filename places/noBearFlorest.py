from place import Place

class NoBearFlorest(Place):

    def __init__(self):
        self.__full_path = "stage1 florest north nobear"
        self.__commands = ["steal_bag", "help_woman"]

    def steal_bag(self):
        return {"move": self.as_list(self.root + " village"), "imediate_consequence": "You steal the woman's bag and go away to the village."}

    def help_woman(self):
        return {"move": self.as_list(self.root + " village"), "imediate_consequence": "You help the woman and she gives you an misterous book. You come back to the village."}

    @property
    def full_path(self):
        return self.__full_path

    @property
    def commands(self):
        return self.__commands
