def filter_dict(dictionary: list[dict], argument: str = "EXECUTED") -> list[dict]:
    """фильтрует словарь по ключу state"""
    return list(filter(lambda x: x["state"] == argument, dictionary))


def sort_dict(dictionary: list[dict], reverse: bool = False) -> list[dict]:
    return sorted(dictionary, key=lambda x: x["date"], reverse=reverse)
