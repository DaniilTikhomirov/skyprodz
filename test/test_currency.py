import os.path

import xml.etree.ElementTree as ET
from src.currency import get_currencies, calculate_amount_in_rub
from decimal import Decimal
from unittest.mock import patch


def test_get_currencies_rub() -> None:
    assert get_currencies("RUB") == Decimal("1")


def test_get_currencies() -> None:
    with patch('xml.etree.ElementTree.parse') as mock_pars:
        with patch('xml.etree.ElementTree.Element') as mock_element:
            with patch(f'xml.etree.ElementTree.Element.find') as mock_find:
                mock_find.return_value = '90'
                assert get_currencies("USD") == Decimal('0')
                mock_pars.assert_called_once_with(os.path.join("..", "data", "cbr.xml"))


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
