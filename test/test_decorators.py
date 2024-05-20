import datetime
from typing import Any
from unittest.mock import patch

import pytest

from src.decorators import log


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
    [
        (1, 2, "05-20-24 17:43:56 my_function ok"),
        (1, "2", "05-20-24 17:43:56 my_function error: TypeError Input:(1, '2'), {}"),
    ],
)
def test_log_file(a: str | int, b: str | int, answer: str) -> None:
    target = datetime.datetime(2024, 5, 20, 17, 43, 56)
    with patch("datetime.datetime") as mock_now:
        mock_now.now.return_value = target
        sum_(a, b)
        with open("t2.txt", "r", encoding="utf-8") as f:
            for line in f:
                pass
        assert line.strip() == answer


@pytest.mark.parametrize(
    "a, b, answer",
    [
        (1, 2, "05-20-24 17:43:56 my_function ok"),
        (1, "2", "05-20-24 17:43:56 my_function error: TypeError Input:(1, '2'), {}"),
    ],
)
def test_log_console(a: str | int, b: str | int, answer: str) -> None:
    target = datetime.datetime(2024, 5, 20, 17, 43, 56)
    with patch("datetime.datetime") as mock_now:
        mock_now.now.return_value = target
        assert sum_2(a, b) == answer
