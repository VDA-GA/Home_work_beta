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
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf8") as file:
                        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} ok \n")
                else:
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} ok \n")
                return result
            except Exception as err:
                if filename:
                    with open(filename, "a", encoding="utf8") as file:
                        file.write(
                            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} error: "
                            f"{err}. Inputs: {args}, {kwargs} \n"
                        )
                else:
                    print(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} "
                        f"error: {err}. Inputs: {args}, {kwargs} \n"
                    )

        return inner

    return wrapper
