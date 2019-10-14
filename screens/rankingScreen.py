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
        template = "{:<20}|{:<30}|{:<26}|{:^30}"
        lines = []
        for key in player_dict.keys():
            for character in player_dict[key]:
                key_decision = "" if not character.key_decisions else character.key_decisions[0]
                lines.append(template.format(key, character.name, str(character.time_played), key_decision))
                for key_decision in character.key_decisions[1:]:
                    lines.append(template.format("↳", "", "", key_decision))
        formated_top = self.format_centralized(title, "-")
        formated_template = "\n".join(lines)
        formated_bottom = self.format_centralized("", '-')
        formated_screen = "{}\n{}\n{}\n".format(formated_top, formated_template, formated_bottom)
        return self.print_wait_confimation(formated_screen)
