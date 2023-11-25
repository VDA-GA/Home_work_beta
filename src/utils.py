import json
import logging
import pandas as pd
# from pathlib import Path
from typing import List, Any
from src.log_func import logging_function

logging_function('HW')
logger = logging.getLogger('HW.utils')


def load_data_from_csv(filename: str) -> pd.DataFrame:
    """Загружает данные из csv-файла
        :param filename: путь к файлу .csv
        :return объект DataFrame"""
    df_data = pd.read_csv(filename, sep=';', header=0)
    return df_data


def load_data_from_xlsx(filename: str) -> pd.DataFrame:
    """Загружает данные из excell-файла
            :param filename: путь к файлу .xlsl или .xls
            :return объект DataFrame"""
    df_data = pd.read_excel(filename)
    return df_data


def load_data_from_json(filename: str) -> Any:
    """Загружает данные из JSON-файла
        :param filename: путь к файлу .json
        :return: список data[dict] или пустой список в случае если файл пустой,
        содержит не список или не найден"""

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


def list_of_dict_from_dataframe(df: pd.DataFrame) -> List[dict[Any, Any]]:
    """Преобразует DataFrame объект в список словарей по транзакции
    :param df: DataFrame object
    :return: список словарей транзакций"""
    df_shape = df.shape
    list_transactions = []
    for i in range(0, df_shape[0] - 1):
        dict_transactions = {
            "id": df.id[i],
            "state": df.state[i],
            "date": df.date[i],
            "operationAmount": {
                "amount": df.amount[i],
                "currency": {
                    "name": df.currency_name[i],
                    "code": df.currency_code[i]
                }
            },
            "description": df.description[i],
            "from": '' if 'nan' else df.iloc[i, 6],
            "to": df.iloc[i, 7]
        }
        list_transactions.append(dict_transactions)
    return list_transactions

#    def get_right_path(filename):
#       path_to_project = Path(Path.cwd()).parent
#        abs_path = Path(path_to_project, filename)
#        return abs_path

# path = get_right_path('data/operations.json')
# res = load_data_from_json(path)
# pattern = re.compile('Перевод организации')
# string = res[3]["description"]
# print(string)
# matches = pattern.search(string)
# print(matches)
# l = matches_in_descriptions(res, 'Перевод организации')
# pprint(l)

# d = count_transactions_by_categories(res, ['Перевод организации', 'Открытие вклада', 'Перевод со счета на счет',
# 'Перевод с карты на счет'])
# pprint(f'd = {d}')
