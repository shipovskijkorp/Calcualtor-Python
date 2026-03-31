import json
import os

CURRENT_VERSION = 3.0

DEFAULT_CONFIG = {
    "password": {
        "max_length": 1024
    },

    "meme-mode": {
        "tumbler": "true"
    },
    
    "config": {
        "config_version": 3.0
    }
}


def load_config(filename="config.json"):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(script_dir, filename)

    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(DEFAULT_CONFIG, file, ensure_ascii=False, indent=4)
        print(f"Конфиг создан: {path}")
        return DEFAULT_CONFIG

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)