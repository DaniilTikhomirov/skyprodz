import re
from collections import Counter


def filter_dict(dictionary: list[dict], argument: str = "EXECUTED") -> list[dict]:
    """фильтрует словарь по ключу state"""
    return list(filter(lambda x: x.get("state", 0) == argument, dictionary))


def sort_dict(dictionary: list[dict], reverse: bool = False) -> list[dict]:
    """сортирует список со словарями"""
    return sorted(dictionary, key=lambda x: x.get("date", 0), reverse=reverse)


def find_description(data: list[dict], find_line: str) -> list:
    """фильтрует данные по строке"""
    return list(filter(lambda x: re.search(find_line.lower(), x.get("description", "").lower()), data))


def count_category(data: list[dict], category: list) -> dict:
    new_list = [i.get("description", "") for i in data if i.get("description", "") in category]
    return Counter(new_list)
