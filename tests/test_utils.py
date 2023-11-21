import pytest
from src.utils import load_data_from_json, transaction_amount_rub


@pytest.fixture
def transaction_rub():
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


@pytest.fixture()
def transaction_usd():
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_load_data_from_json1(transaction_rub):
    list_data = load_data_from_json("data/operations.json")
    assert list_data[0] == transaction_rub


def test_load_data_from_json2():
    list_data = load_data_from_json("tests/operations.json")
    assert list_data == []


def test_transaction_amount_rub(transaction_rub):
    assert transaction_amount_rub(transaction_rub) == 31957.58


def test_transaction_amount_usd(transaction_usd):
    with pytest.raises(ValueError):
        transaction_amount_rub(transaction_usd)
