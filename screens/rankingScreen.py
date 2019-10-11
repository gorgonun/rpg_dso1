from screen import Screen
from datetime import datetime

class RankingScreen(Screen):
    
    def __init__(self, log):
        self.__log = log

    @property
    def log(self):
        return self.__log

    def show_ranking(self, player_dict: dict):
        title = "Ranking"
        template = "|{:<30}|{:<26}|{:^30}|"
        menu = [("Exit", lambda: 0)]
        lines = []
        for key in player_dict.keys():
            lines.append(template.format(key, str(player_dict[key]["date"]), " ".join(player_dict[key]["key_decisions"][0])))
            for key_decision in player_dict[key]["key_decisions"][1:]:
                lines.append(template.format("", "", " ".join(key_decision)))
        formated_top = super().format_centralized(title, "-")
        formated_template = "\n".join(lines)
        formated_bottom = super().format_centralized("", '-')
        formated_screen = "{}\n{}\n{}\n".format(formated_top, formated_template, formated_bottom)
        return super().get_menu_input("", menu, text_screen=formated_screen)

RankingScreen().show_ranking({
    "jose": {"date": datetime.now(), "key_decisions": [("thief", "woman"), ("kill", "friend")]},
    "jose1": {"date": datetime.now(), "key_decisions": [("thief", "woman"), ("kill", "friend")]}
})