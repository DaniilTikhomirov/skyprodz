import datetime
import typing


def log(*, filename: str | None = None) -> typing.Callable:
    """
    декоратор, который пишет информацию о работе функции если, указать имя файла
    то напишет текстовый файл в той же дериктории, где вызвана функция,
    если же не указать напишет в консоль.


    filename: str | None аргумент, который принимает имя файла, если его не написать то принимает NONE
    и выводит информацию о работе функции в консоль
    """

    def wrapper(func: typing.Callable[[typing.Any], typing.Any]) -> typing.Callable[[typing.Any], str]:
        def init(*args: typing.Any, **kwargs: typing.Any) -> str:
            """
            проверяет дали ли названия файла если нет то пишет в консоль
            если дали создает документ в который записывает время и ошибку
            """
            if filename is not None:
                with open(filename, "a", encoding="utf8") as file:
                    # проверка на ошибки
                    try:
                        func(*args, **kwargs)
                    except Exception as exeption:
                        # time - берет актуальное время и форматирует его по формуле
                        # type(exeption).__name__ - получает имя ошибки
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
                    # time - берет актуальное время и форматирует его по формуле
                    # type(exeption).__name__ - получает имя ошибки
                    time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
                    print(f"{time} my_function error: {type(exeption).__name__} Input:{args}, {kwargs}")
                    return f"{time} my_function error: {type(exeption).__name__} Input:{args}, {kwargs}"
                else:
                    time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))
                    print(f"{time} my_function ok")
                    return f"{time} my_function ok"

        return init

    return wrapper
