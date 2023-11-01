import os


def do_mask_cart_number(cart_number: int | str) -> str:
    """
    Принимает номер карты возвращает маску в виде XXXX XX** **** XXXX
    :param cart_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """

    cart_number = str(cart_number)
    return cart_number[0:4] + " " + cart_number[4:6] + "**" + " **** " + cart_number[12:16]


def do_mask_account_number(account_number: int | str) -> str:
    """
    Принимает номер счета возвращает маску в виде **4305
    :param account_number: Номер для маскирования
    :return: Маскированный по правилу номер
    """

    account_number = str(account_number)
    return "**" + account_number[16::]


def make_dict_content_folder(path: str = os.getcwd(), req: bool = False) -> dict:
    """Возвращает словарь с количеством файлов и папок.
    Параметры:
            path (str): путь к директории, по умолчанию путь где лежит файл с функцией
            req (bool): проводить ли рекурсивный подсчет, по умоланию нет(False)
    Возвращаемое значение:
            dict_content (dict):
            {"files": количество файлов в директории, "folders": количество папок в директории}

    """
    list_dirs_files = os.listdir(path)
    count_dir = 0
    count_files = 0

    if req:
        for path, dirs, files in os.walk(path):
            for _ in files:
                count_files += 1
            for _ in dirs:
                count_dir += 1
        dict_content = {"files": count_files, "folders": count_dir}
        return dict_content
    else:
        for i in range(0, len(list_dirs_files)):
            if os.path.isdir(os.path.join(path, list_dirs_files[i])):
                count_dir += 1
        count_files = len(list_dirs_files) - count_dir
        dict_content = {"files": count_files, "folders": count_dir}
        return dict_content
