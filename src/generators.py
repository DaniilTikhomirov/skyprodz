import typing


def filter_by_currency(transactions: list, value: str) -> typing.Iterator:
    """фильтрует по валюте и воврощает обьект"""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == value.upper(), transactions)


def transaction_descriptions(transactions: list) -> typing.Generator:
    """возврощает обьект с операциями"""
    return (item["description"] for item in transactions)


def card_number_generator(start: int, end: int) -> typing.Generator:
    """генирирует номера карт"""
    return (
        str(10000_0000_0000_0000 + i)[1:5]
        + " "
        + str(10000_0000_0000_0000 + i)[5:9]
        + " "
        + str(10000_0000_0000_0000 + i)[9:13]
        + " "
        + str(10000_0000_0000_0000 + i)[13:]
        for i in range(start, end + 1)
    )
