from functools import wraps
from datetime import datetime
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Any:
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
                            f"{err}. Inputs: {args}, {kwargs} \n")
                else:
                    print(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {func.__name__} "
                        f"error: {err}. Inputs: {args}, {kwargs} \n")

        return inner

    return wrapper
