from place import Place

class Village(Place):

    def __init__(self):
        self.__full_path = "stage1 forest north"
        self.__commands = ["kill bear", "go away", "push him away"]

    def kill_bear(self):
        return {"move": self.as_list(self.full_path) + "nobear", "imediate_consequence": "you take an arrow in your pouch and, with your ranger skill, kill the bear with one arrow in his head"}

    def go_away(self):
        return {"move": self.as_list(self.full_path + " village"), "imediate_consequence": "You go away, trying to not be envolved in problems. You go to the village."}

    def push_him_away(self):
        return {"imediate_consequence": "You try to push the bear away screaming with him and throwing stones in his direction. He goes away. In your back you hear a bear roar. When you turn, you feel your skin being rip. You're dead.", "dead": ""}

    @property
    def full_path(self):
        return self.__full_path

    @property
    def commands(self):
        return self.__commands
