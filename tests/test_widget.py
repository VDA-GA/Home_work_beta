import pytest

from src.widget import do_masks_number_card_or_account, get_data_from_time


@pytest.mark.parametrize(
    "number, expected_result",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Счет 12345678901234567890", "Счет **7890"),
    ],
)
def test_do_masks_number_card_or_account_for_card(number, expected_result):
    assert do_masks_number_card_or_account(number) == expected_result


@pytest.mark.parametrize(
    "data, expected_result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-10-14T08:21:33.419441", "14.10.2018"),
    ],
)
def test_get_data_from_time(data, expected_result):
    assert get_data_from_time(data) == expected_result
