import logging


def logging_function(name_module:str) -> None:
    # Инициализация логгера (конкретного регистратора):
    logger = logging.getLogger(name_module)
    # Установка уровня логгирования:
    logger.setLevel(logging.DEBUG)
    # Создание и настройка хендлера для вывода в консоль:
    handler1 = logging.StreamHandler()
    handler1.setFormatter(
        logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    handler1.setLevel(logging.DEBUG)
    # Создание и настройка хендлера вывода в файл:
    handler2 = logging.FileHandler(filename='log.txt', encoding='utf-8')
    handler2.setFormatter(
        logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S'))
    handler2.setLevel(logging.DEBUG)
    # Добавление хенжлеров к конкретному экземпляру логгера:
    logger.addHandler(handler1)
    logger.addHandler(handler2)
    logger.debug('Логер инициализирован')
