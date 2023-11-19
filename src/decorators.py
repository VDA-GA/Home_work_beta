from functools import wraps
from datetime import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Any:
    """
    Логирует вызов декорируемой функции и ее результат в файл или в консоль
    принимает на вход filename - название файла для записи логов, по умолчанию отсутствует

    Пример использования:

    @log('my_log.txt')
    def my_func(x, y):
       return x / y

    my_func(1, 0)
    # Вывод: запись в файл следующей строки:
    2023-11-12 14:28:25 my_func error: division by zero. Inputs: (1, 0), {}
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                result = func(*args, **kwargs)
                log_message = f"{time_now} {func.__name__} ok \n"
            except Exception as err:
                log_message = f"{time_now} {func.__name__} error: {err}. Inputs: {args}, {kwargs} \n"
                result = None

            if filename:
                with open(filename, "a", encoding="utf8") as file:
                    file.write(log_message)
            else:
                print(log_message)
            return result

        return inner

    return wrapper
