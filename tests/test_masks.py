import pytest

from src.masks import do_mask_account_number, do_mask_cart_number


@pytest.mark.parametrize('cart_number, expected_result', [('1234567891234567', '1234 56** **** 4567'),
                                                          (1234567891234567, '1234 56** **** 4567')])
def test_do_mask_cart_number(cart_number, expected_result):
    assert do_mask_cart_number(cart_number) == expected_result


@pytest.mark.parametrize('account_number, expected_result', [('01234567890123456789', '**6789'),
                                                             (12345678901234567890, '**7890')])
def test_do_mask_account_number(account_number, expected_result):
    assert do_mask_account_number(account_number) == expected_result
