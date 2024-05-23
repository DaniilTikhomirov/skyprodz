import json
import os.path
from datetime import datetime
from unittest.mock import Mock, patch

from pandas import DataFrame

from src.utils import unpack_csv, unpack_excel, unpack_json, write_xml_from_web


@patch("builtins.open")
def test_unpack_json(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert unpack_json(os.path.join("..", "data", "operations.json"))
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf8")


def test_unpack_json_file_error() -> None:
    assert unpack_json(os.path.join("..", "data", "uio.json")) == []


def test_write_xml_from_web() -> None:
    with patch("builtins.open") as mock_open:
        with patch("requests.get") as mock_get:
            time_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
            url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}"
            write_xml_from_web(url, "cbr")
            mock_open.assert_called_once_with(os.path.join("..", "data", "cbr.xml"), "wb")
            mock_get.assert_called_once_with(f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}")


def test_unpack_csv() -> None:
    with patch("pandas.read_csv") as mock_csv:
        mock_csv.return_value = DataFrame({"test": ["test"]})
        assert unpack_csv(os.path.join("..", "data", "test.csv")) == [{"test": "test"}]


def test_unpack_excel() -> None:
    with patch("pandas.read_excel") as mock_csv:
        mock_csv.return_value = DataFrame({"test": ["test"]})
        assert unpack_excel(os.path.join("..", "data", "test.csv")) == [{"test": "test"}]
