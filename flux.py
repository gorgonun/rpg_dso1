from history import history

def get_text(key):
    return history[key]

def place(name, textid=None, places=None):
    result = {name: {}}
    result[name]["placename"] = name
    if textid: result[name]["text"] = get_text(textid)
    if places: result[name]["places"] = {**places}
    return result

flux = {
    "stage1": {
        "places": {
            **place("florest", "stage1 florest", {**place("north", "stage1 florest north", place("nobear", "stage1 florest north nobear"))}),
            **place("village", "stage1 village")
        }   
    }
}
