import os.path
from datetime import datetime

from src.currency import get_currencies, calculate_amount_in_rub
from decimal import Decimal
from unittest.mock import patch


def test_get_currencies_rub() -> None:
    assert get_currencies("RUB") == Decimal("1")


@patch('builtins.open', create=True)
def test_get_currencies(mock_open) -> None:
    with patch('requests.get') as mock_get:
        mock_open.return_value.__enter__.return_value.read.return_value = None
        mock_get.return_value.Decimal.return_value = Decimal('91.890')
        assert get_currencies("USD") == Decimal('91.890')
        mock_open.assert_called_once_with(os.path.join("..", "data", f"cbr.xml"), "wb")
        time_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
        mock_get.assert_called_once_with(f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}")


def test_calculate_amount_in_rub() -> None:
    dict_operation = {
        "id": 649467725,
        "state": "EXECUTED",
        "date": "2018-04-14T19:35:28.978265",
        "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Счет 27248529432547658655",
        "to": "Счет 97584898735659638967",
    }
    assert calculate_amount_in_rub(dict_operation) == Decimal("96995.73")
