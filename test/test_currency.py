import os.path
import pytest

import xml.etree.ElementTree as ET
from src.currency import get_currencies, calculate_amount_in_rub
from decimal import Decimal
from unittest.mock import patch


@pytest.fixture
def data():
    return '''<?xml version="1.0" encoding="windows-1251"?>
<ValCurs Date="15.05.2024" name="Foreign Currency Market">
    <Valute ID="R01235">
        <NumCode>840</NumCode>
        <CharCode>USD</CharCode>
        <Nominal>1</Nominal>
        <Name>Доллар США</Name>
        <Value>74,3250</Value>
    </Valute>
    <Valute ID="R01239">
        <NumCode>978</NumCode>
        <CharCode>EUR</CharCode>
        <Nominal>1</Nominal>
        <Name>Евро</Name>
        <Value>90,1234</Value>
    </Valute>
</ValCurs>'''


def test_get_currencies_rub() -> None:
    assert get_currencies("RUB") == Decimal("1")


def test_get_currencies(data) -> None:
    with patch('builtins.open') as mock_open:
        with patch('xml.etree.ElementTree.parse') as parse_mock:
            mock_tree = ET.fromstring(data)
            parse_mock.return_value = mock_tree
            mock_file = mock_open.return_value.__enter__.return_value
            mock_file.read.return_value = data
            value = get_currencies('USD')
            assert value == Decimal("74,3250")


# def test_calculate_amount_in_rub() -> None:
#     dict_operation = {
#         "id": 649467725,
#         "state": "EXECUTED",
#         "date": "2018-04-14T19:35:28.978265",
#         "operationAmount": {"amount": "96995.73", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Счет 27248529432547658655",
#         "to": "Счет 97584898735659638967",
#     }
#     assert calculate_amount_in_rub(dict_operation) == Decimal("96995.73")
