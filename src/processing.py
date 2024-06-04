import re
from typing import Any


def filter_dict(dictionary: list[dict], argument: str = "EXECUTED") -> list[dict]:
    """фильтрует словарь по ключу state"""
    return list(filter(lambda x: x.get("state") == argument, dictionary))


def sort_dict(dictionary: list[dict], reverse: bool = False) -> list[dict]:
    """сортирует список со словарями"""
    return sorted(dictionary, key=lambda x: x.get("date"), reverse=reverse)


def find_description(data: list[dict], find_line: Any | None) -> list:
    """фильтрует данные по строке"""
    return list(filter(lambda x: re.search(find_line, x.get("description")), data))
