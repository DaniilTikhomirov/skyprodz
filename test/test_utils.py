import pytest
from src.utils import unpack_json
from unittest.mock import Mock
import os.path


@pytest.fixture
def data() -> dict:
    return {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }


def test_unpack_json(data: list[dict]) -> None:
    assert unpack_json(os.path.join("..", "data", "operations.json"))[0] == data


def test_write_xml_from_web(data: list[dict]) -> None:
    write_xml_from_web_mock = Mock(return_value="xml-file")
    assert write_xml_from_web_mock() == "xml-file"
