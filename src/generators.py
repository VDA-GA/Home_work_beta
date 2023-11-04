from typing import Any, Generator, List

from src.transactions import transactions


def filter_by_currency(list_transactions: List[dict], currency: str) -> Any:
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)
    # Another way:
    # return (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(list_transactions: List[dict]) -> Generator:
    return (x["description"] for x in transactions)


def card_number_generator(start_number: int, end_number: int) -> Generator:
    x = start_number
    while x <= end_number:
        number = "0" * (16 - len(str(x))) + str(x)
        masked_card_number = " ".join([number[i : i + 4] for i in range(0, 16, 4)])
        yield masked_card_number
        x += 1
