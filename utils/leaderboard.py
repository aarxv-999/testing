# utils/leaderboard.py
import json
import os

LEADERBOARD_FILE = "leaderboard.json"

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return {}
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)

def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)

def update_leaderboard(staff_name):
    data = load_leaderboard()
    if staff_name in data:
        data[staff_name] += 10  # 10 points per event
    else:
        data[staff_name] = 10
    save_leaderboard(data)
    return data
