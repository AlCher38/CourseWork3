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
    Функция вывода последних 5 операций
    :return:
    """
    sort_list = sorted(operations, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=True)
    list_operation = sort_list[:5]
    return list_operation


def change_date(date):
    """
    Функция форматирования даты, пример: 14.10.2018
    :return: date_operations
    проверка print(change_date(sort_date_operations(get_executed_operations(load_json()))))
    """
    date_operations = []
    for list_data in date:
        sort_data = datetime.strptime(list_data['date'], "%Y-%m-%dT%H:%M:%S.%f")
        format_date = f"{sort_data: %d.%m.%Y}"
        date_operations.append(format_date)
    return date_operations


def mask_card_number(card_number):
    """
    скрытие номера карты
    проверка: print(mask_card_number("Maestro 1596837868705199"))
    """
    mask_number = "{} {}** **** {}".format(card_number[:-12], card_number[-10:-8], card_number[-4:])
    return mask_number


def mask_amount_number(amount_number):
    """
    скрытие номера счета
    проверка print(mask_amount_number("Счет 35383033474447895560"))
    """
    mask_amount = "Счёт **{}".format(amount_number[-4:])
    return mask_amount



