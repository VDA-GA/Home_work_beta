import json
import logging
from typing import Any
from src.log_func import logging_function

logging_function('HW')
logger = logging.getLogger('HW.utils')


def load_data_from_json(filename: str) -> Any:
    """Загружает данные из JSON-файла
    :param filename: путь к файлу .json
    :return список data или пустой список в случае если
    файл пустой, содержит не список или не найден"""
    try:
        logger.debug(f'Открытие файла {filename}')
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
        logger.info('Список из файла получен')
        logger.debug(f'Получен список из {len(data)} транзакций')
        return data
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as err:
        logger.error(err)
        return []


def transaction_amount_rub(transaction: dict) -> float:
    """Выводит сумму транзакции в рублях
    :param transaction: данные по транзакции в виде словаря
    :return сумма транзакции"""
    logger.debug('Получена транзакция')
    if transaction["operationAmount"]["currency"]["name"] == "руб.":
        logger.info('Транзакция в рублях присутствует')
        return float(transaction["operationAmount"]["amount"])
    else:
        logger.error(f'{ValueError} Транзакция выполнена не в рублях.')
        raise ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
