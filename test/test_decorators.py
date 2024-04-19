import datetime
from typing import Any

import pytest

from src.decorators import log

time = str(datetime.datetime.now().strftime("%m-%d-%y %H:%M:%S"))


@log(filename="t2.txt")
def sum_(a: Any, b: Any) -> Any:
    """сумма"""
    return a + b


@log()
def sum_2(a: Any, b: Any) -> Any:
    """сумма"""
    return a + b


@pytest.mark.parametrize(
    "a, b, answer",
    [(1, 2, f"{time} my_function ok"), (1, "2", f"{time} my_function error: TypeError Input:(1, '2'), {'{}'}")],
)
def test_log_file(a: str | int, b: str | int, answer: str) -> None:
    sum_(a, b)
    with open("t2.txt", "r", encoding="utf-8") as f:
        for line in f:
            pass
    assert line.strip() == answer


@pytest.mark.parametrize(
    "a, b, answer",
    [(1, 2, f"{time} my_function ok"), (1, "2", f"{time} my_function error: TypeError Input:(1, '2'), {'{}'}")],
)
def test_log_console(a: str | int, b: str | int, answer: str) -> None:
    assert sum_2(a, b) == answer
