def as_consequence_dict(consequence: str, carma: int=0, dead: bool=False, key_decision: str=""):
    return {"consequence": consequence, "carma": carma, "dead": dead, "key_decision": key_decision}

def as_history_dict(id: str, introduction: str, **kwargs):
    introduction = {"introduction": introduction}
    actions = {key.replace(" ", "_"): value for key, value in kwargs.items()}
    return {id: {**introduction, **actions}}

history = {
    **as_history_dict(
        "forest",
        "Inside the vast forest in the countryside you are starving, going to a famous hunter area.",
        move_north=as_consequence_dict("You walk")
        ),
    **as_history_dict(
        "forest north",
        "As you come closer, you find a woman laying on a stone, with a full bag in her left. In her right, distant by some metters, there is a bear slowing going away.",
        kill_bear=as_consequence_dict("you take an arrow in your pouch and, with your ranger skill, kill the bear with one arrow in his head", carma=-1),
        go_away=as_consequence_dict("You go away, trying to not be envolved in problems. You go to the village.", carma=-1),
        push_him_away=as_consequence_dict("You try to push the bear away screaming with him and throwing stones in his direction. He goes away. In your back you hear a bear roar. When you turn, you feel your skin being ripped away. You're dead.", dead=True, key_decision="push him away"),
    ),
    **as_history_dict(
        "forest north nobear",
        "Now you and the woman are safe from the enemy.",
        steal_bag=as_consequence_dict("You steal the woman's bag and go away to the village.", carma=-1, key_decision="steal bag"),
        help_woman=as_consequence_dict("You help the woman and she gives you an misterous book. You come back to the village.", carma=1, key_decision="help woman")
    ),
    **as_history_dict(
        "village",
        "You see your village destructed and your father in the ground, probably dead.",
        walk_away=as_consequence_dict("When you try to walk away, an arrow get you in the belly. You are dead", key_decision="walk away", dead=True)
    )
}
