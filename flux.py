from history import history


def get_text(key):
    return history[key]


def place(name, textid=None, places_inside=None):
    result = {name: {}}
    result[name]["placename"] = name
    if textid: result[name]["data"] = get_text(textid)
    if places_inside: result[name]["places"] = {**places_inside}
    return result

flux = {}
flux.update(place("forest", "forest",
                  place("north", "forest north",
                        place("nobear", "forest north nobear"))))

flux.update(place("village", "village"))
