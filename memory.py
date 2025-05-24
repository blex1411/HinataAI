# memory.py
import json
from config import MEMORY_FILE

def load_memory():
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def get_user_data(user_id):
    data = load_memory()
    return data.get(str(user_id), {"history": [], "scenario": "teman"})

def update_user_data(user_id, key, value):
    data = load_memory()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}
    data[uid][key] = value
    save_memory(data)
