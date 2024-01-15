from config import *
import json
from datetime import datetime


def load_json():
    with open(OPERATION, 'r', encoding="UTF-8") as file:
        json_user_operations = json.load(file)
    return json_user_operations
