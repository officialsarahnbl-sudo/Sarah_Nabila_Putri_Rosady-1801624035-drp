import json
import os

FILE_DB = "users.json"

def load_users():
    if not os.path.exists(FILE_DB):
        return {}

    try:
        with open(FILE_DB, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_users(users):
    with open(FILE_DB, "w") as f:
        json.dump(users, f, indent=4)