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
    Сортировка operations.json есть ли EXECUTTED
    :return: executed_operations
    """
    executed_operations = []
    for value in values:
        if value == {}:
            continue
        elif value['state'] == 'EXECUTED':
            executed_operations.append(value)
    return executed_operations


def sort_date_operations(operations):
    """
    Функция сортировки даты
    :return:
    """
    sort_list = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    list_operation = sort_list[:5]
    return list_operation


def change_date(date):
    """
    Функция форматирования даты, пример: 14.10.2018
    :return: date_operations
    """
    date_operations = []
    for list_data in date:
        sort_data = datetime.strptime(list_data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        format_date = f"{sort_data: %d.%m.%Y}"
        date_operations.append(format_date)

    return date_operations


print(change_date(sort_date_operations(get_executed_operations(load_json()))))
