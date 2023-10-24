from masks import do_mask_cart_number, do_mask_account_number


def do_masks_number_card_or_account(input_number: str) -> str:
    """
    Принимает номер счета/карты возвращает маску в виде
    для карты: Visa Platinum 7000 79** **** 6361
    для счета: Счет **4305
    :param input_number: тип карты/счета и номер для маскирования
    :return: Маскированный по правилу номер
    """

    if "счет" or "счёт" in input_number.lower():
        mask = do_mask_account_number(input_number[(len(input_number) - 20): -1])
        return input_number[0: (len(input_number) - 20)] + mask
    else:
        mask = do_mask_cart_number(input_number[(len(input_number) - 16): -1])
        return input_number[0: (len(input_number) - 16)] + mask
