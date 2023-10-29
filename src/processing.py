from typing import List


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

    if order:
        return sorted(list_data, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(list_data, key=lambda x: x["date"])
