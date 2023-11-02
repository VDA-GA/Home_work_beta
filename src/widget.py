from src.masks import do_mask_account_number, do_mask_cart_number


def do_masks_number_card_or_account(input_number: str) -> str:
    """
    Принимает номер счета/карты возвращает маску в виде
    для карты: Visa Platinum 7000 79** **** 6361
    для счета: Счет **4305
    :param input_number: тип карты/счета и номер для маскирования
    :return: Маскированный по правилу номер
    """

    if "счет" in input_number.lower():
        mask = do_mask_account_number(input_number[(len(input_number) - 20):])
        return input_number[0: (len(input_number) - 20)] + mask
    else:
        mask = do_mask_cart_number(input_number[(len(input_number) - 16):])
        print(input_number[(len(input_number) - 16):])

        return input_number[0: (len(input_number) - 16)] + mask


def get_data_from_time(str_time: str) -> str:
    """
    Принимает строку в виде 2018-07-11T02:26:18.671407
    возвращает дату в виде 11.07.2018
    :param str_time: исходная строка
    :return: дата
    """
    data = str_time[8:10] + "." + str_time[5:7] + "." + str_time[0:4]
    return data
