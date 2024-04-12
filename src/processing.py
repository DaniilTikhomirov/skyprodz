def filter_dict(dictionary: list[dict], argument: str = "EXECUTED") -> list[dict]:
    """фильтрует словарь по ключу state"""
    return list(filter(lambda x: x["state"] == argument, dictionary))