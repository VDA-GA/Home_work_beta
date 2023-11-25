from typing import List
import re


def filter_dict(list_data: List[dict], state: str = "EXECUTED") -> List[dict]:
    """
    Принимает список словарей в виде {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}
    возвращает список словарей отфильтрованных по значению ключа state: EXECUTED или CANCELED
    :param list_data: исходный список словарей
    :param state: значение state для фильтрации, по умолчанию EXECUTED
    :return: отфильтрованный список словарей по значению ключа state
    """

    filter_list: list[dict] = []
    for data in list_data:
        if data["state"] == state:
            filter_list.append(data)
    return filter_list


def sorted_list_on_date(list_data: List[dict], order: bool = True) -> List[dict]:
    """
    Принимает список словарей в виде {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}
    возвращает список словарей отсортированных по значению ключа date
    :param list_data: исходный список словарей
    :param order: порядок по умолчанию True - сортировка по убыванию
    :return: отфильтрованный список словарей по значению ключа state
    """

    return sorted(list_data, key=lambda x: x["date"], reverse=order)


def matches_in_descriptions(list_of_transactions: List[dict], search_string: str) -> List[dict]:
    """Функция принимает список словарей транзакций и строку поиска по категории
    :param list_of_transactions: список словарей с транзакциями
    :param search_string: строка поиска по типу категории
    :return: список словарей отфильтрованных по указанной категории"""

    pattern = re.compile(search_string)
    list_of_dict_with_matches = []
    for i in range(0, len(list_of_transactions)):
        if list_of_transactions[i] != {}:
            string = list_of_transactions[i]["description"]
            matches = pattern.search(string)
            if matches:
                list_of_dict_with_matches.append(list_of_transactions[i])
    return list_of_dict_with_matches


def count_transactions_by_categories(list_of_transactions: List[dict], list_categories: list) -> dict:
    """Функция принимает список словарей транзакций и список категорий
        :param list_of_transactions: список словарей с транзакциями
        :param list_categories: список категорий
        :return: словарь с ключом тип категории и значением количество операций указанной категории"""

    dict_of_analysis_by_category = {}
    for category in list_categories:
        list_of_matches_transactions = matches_in_descriptions(list_of_transactions, category)
        dict_of_analysis_by_category[category] = len(list_of_matches_transactions)
    return dict_of_analysis_by_category
