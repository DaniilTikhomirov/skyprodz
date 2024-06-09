import re


def filter_dict(dictionary: list, argument: str = "EXECUTED") -> list[dict]:
    """фильтрует словарь по ключу state"""
    return list(filter(lambda x: x.get("state") == argument, dictionary))


def sort_dict(dictionary: list, reverse: bool = False) -> list[dict]:
    """сортирует список со словарями"""
    return sorted(dictionary, key=lambda x: x.get("date", 0), reverse=reverse)


def find_element(data: list[dict], obj: str) -> list[dict]:
    return list(filter(lambda x: re.search(obj, x.get("description")), data))


