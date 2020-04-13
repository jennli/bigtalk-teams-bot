import json
import os


def get_bigtalks():
    target_path = os.path.join(os.path.dirname(__file__), 'db.json')
    with open(target_path) as f:
        return json.load(f)["payload"]