import json

STATE_FILE = "data/state.json"

def save_state(data):
    with open(STATE_FILE, "w") as f:
        json.dump(data, f)

def load_state():
    try:
        with open(STATE_FILE, "r") as f:
            return json.load(f)
    except:
        return {}
