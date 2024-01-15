from config import *
import json
from datetime import datetime


def load_json():
    """
    Открытие файла operations.json
    :return: json_user_operations
    """
    with open(OPERATION, 'r', encoding="UTF-8") as file:
        json_user_operations = json.load(file)
    return json_user_operations


def get_executed_operations(values):
    """
    Последние 5 выполненных (EXECUTED) операций выведеных на экран.
    :return: executed_operations
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value['state'] == 'EXECUTED':
            executed_operations.append(value)

    return executed_operations
