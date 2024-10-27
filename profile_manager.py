import os
import json

PROFILE_DIR = "profiles/"

def create_profile(username):
    profile_path = f"{PROFILE_DIR}{username}.json"
    if not os.path.exists(PROFILE_DIR):
        os.makedirs(PROFILE_DIR)

    profile_data = {
        "username": username,
        "accuracy": {"easy": 0, "medium": 0, "hard": 0},
        "sessions_completed": 0
    }

    with open(profile_path, 'w') as file:
        json.dump(profile_data, file)
    print(f"Profile created for {username}!")

def load_profile(username):
    profile_path = f"{PROFILE_DIR}{username}.json"
    if os.path.exists(profile_path):
        with open(profile_path, 'r') as file:
            return json.load(file)
    else:
        print(f"Profile for {username} not found.")
        return None
