import pytest

from src.mask import security_card, security_num


@pytest.fixture()
def coll() -> str:
    return "73654108430135874305"


def test_security_num(coll: str) -> None:
    assert security_num(coll) == "**4305"


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("73654108430135874305", "**4305"),
        ("346788", "не правильно введены данные"),
        ("fjjk", "не правильно введены данные"),
        ("7365410843013587430544", "не правильно введены данные"),
    ],
)
def test_security_num_all(n: str, expected_result: str) -> None:
    assert security_num(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("dfh", "не правильно введены данные"),
        ("7000792289606361789", "не правильно введены данные"),
        ("70007922896063", "не правильно введены данные"),
    ],
)
def test_security_card(n: str, expected_result: str) -> None:
    assert security_card(n) == expected_result
