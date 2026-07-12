import json
import os

HISTORY_FILE = "history.json"


def save_history(analysis):

    history = []

    if os.path.exists(HISTORY_FILE):

        try:
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)

        except Exception:
            history = []

    history.append(analysis)

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    try:

        with open(HISTORY_FILE, "r") as f:
            return json.load(f)

    except Exception:

        return []