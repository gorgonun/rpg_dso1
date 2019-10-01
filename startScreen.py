from screen import Screen


class StartScreen(Screen):
    
    def __init__(self):
        text = "Start menu"
        start = lambda: print("char_screen")
        create = lambda: print("Creating")
        # menu = {"Start game": start, "Create character": create}
        menu = [("Start game", start), ("Create character", create), ("Exit", exit)]
        super().get_menu_input(text, menu)

StartScreen()