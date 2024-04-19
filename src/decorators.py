import datetime
import os
import typing


def log(*, filename: str | None = None) -> typing.Callable:
    def wrapper(func: typing.Callable) -> typing.Callable:
        def init(*args: typing.Any, **kwargs: typing.Any) -> str:
            """
            проверяет дали ли названия файла если нет то пишет в консоль
            если дали создает документ в который записывает время и ошибку
            """
            if filename is not None:
                file_path_ = os.path.join("..", "test_txt", filename)
                with open(file_path_, "a", encoding="utf8") as file:
                    try:
                        func(*args, **kwargs)
                    except Exception as exeption:
                        time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
                        file.write(f"{time} my_function error: {type(exeption).__name__} Input:{args}, {kwargs}\n")
                        return f"{time} my_function error: {type(exeption).__name__} Input:{args}, {kwargs}"
                    else:
                        time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
                        file.write(f"{time} my_function ok\n")
                        return f"{time} my_function ok"
            else:
                try:
                    func(*args, **kwargs)
                except Exception as exeption:
                    time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
                    print(f"{time} my_function error: {type(exeption).__name__} Input:{args}, {kwargs}")
                    return f"{time} my_function error: {type(exeption).__name__} Input:{args}, {kwargs}"
                else:
                    time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
                    print(f"{time} my_function ok")
                    return f"{time} my_function ok"

        return init

    return wrapper
