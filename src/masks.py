import logging
from log_func import logging_function

logging_function('HW')
logger = logging.getLogger('HW.masks')


def do_mask_cart_number(cart_number: int | str) -> str:
    """
    Принимает номер карты возвращает маску в виде XXXX XX** **** XXXX
    :param cart_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """

    cart_number = str(cart_number)
    logger.debug('Номер карты получен')
    return cart_number[0:4] + " " + cart_number[4:6] + "**" + " **** " + cart_number[12:16]


def do_mask_account_number(account_number: int | str) -> str:
    """
    Принимает номер счета возвращает маску в виде **4305
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    account_number = str(account_number)
    logger.debug('Номер счета получен')
    return "**" + account_number[16::]
