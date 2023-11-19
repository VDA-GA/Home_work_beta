import json
from typing import Any


def load_data_from_json(filename: str) -> Any:
    """Загружает данные из JSON-файла
    :param filename: путь к файлу .json
    :return список data или пустой список в случае если
    файл пустой, содержит не список или не найден"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        return []


def transaction_amount_rub(transaction: dict) -> float:
    """Выводит сумму транзакции в рублях
    :param transaction: данные по транзакции в виде словаря
    :return сумма транзакции"""
    if transaction["operationAmount"]["currency"]["name"] == "руб.":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
