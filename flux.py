from history import history

def get_text(key):
    return history[key]

def place(name, textid=None, places=None):
    result = {name: {}}
    result[name]["placename"] = name
    if textid: result[name]["data"] = get_text(textid)
    if places: result[name]["places"] = {**places}
    return result

flux = {
    "stage1": {
        "places": {
            **place("forest", "stage1 forest", {
                **place("north", "stage1 forest north",
                    place("nobear", "stage1 forest north nobear")
                    )
                }
            ),
            **place("village", "stage1 village")
        }
    }
}
