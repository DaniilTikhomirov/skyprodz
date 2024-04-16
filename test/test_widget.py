import pytest

from src.widget import format_date, mask_card_and_num


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Maestro 15968378658705199678", "не правильно введены данные"),
        ("Счет 6468647367887877894779589", "не правильно введены данные"),
        ("Maestro 1596837865870519967h", "не правильно введены данные"),
        ("Счет 646864736788787789477958g", "не правильно введены данные"),
        ("Счет 6468647367887877894779", "не правильно введены данные"),
        ("Maestro 15968378687051997999", "не правильно введены данные"),
    ],
)
def test_mask_card_and_num(n: str, expected_result: str) -> None:
    assert mask_card_and_num(n) == expected_result


@pytest.mark.parametrize(
    "n, expected_result",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2018-08-11T02:26:18.671407", "11.08.2018"),
        ("2019-07-11T02:26:18.671407", "11.07.2019"),
    ],
)
def test_format_date(n: str, expected_result: str) -> None:
    assert format_date(n) == expected_result
