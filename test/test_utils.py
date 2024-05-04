import pytest
from src.utils import unpack_json
from unittest.mock import Mock


@pytest.fixture
def data() -> list[dict]:
    return [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
    ]


def test_unpack_json(data: list[dict]) -> None:
    assert unpack_json("C:\\Users\\Student Free\\PycharmProjects\\Bank_project\\test\\test_data\\test.json") == data


def test_write_xml_from_web(data: list[dict]) -> None:
    write_xml_from_web_mock = Mock(return_value="xml-file")
    assert write_xml_from_web_mock() == "xml-file"
