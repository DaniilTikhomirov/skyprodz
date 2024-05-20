import json
import os.path
from datetime import datetime
from unittest.mock import Mock, patch

from src.utils import unpack_json, write_xml_from_web


@patch("builtins.open")
def test_unpack_json(mock_open: Mock) -> None:
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.read.return_value = json.dumps([{"test": "test"}])
    assert unpack_json(os.path.join("..", "data", "operations.json"))
    mock_open.assert_called_once_with(os.path.join("..", "data", "operations.json"), "r", encoding="utf8")


def test_write_xml_from_web() -> None:
    with patch("builtins.open") as mock_open:
        with patch("requests.get") as mock_get:
            time_now = datetime.strftime(datetime.now(), "%d/%m/%Y")
            url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}"
            write_xml_from_web(url, "cbr")
            mock_open.assert_called_once_with(os.path.join("..", "data", "cbr.xml"), "wb")
            mock_get.assert_called_once_with(f"https://cbr.ru/scripts/XML_daily.asp?date_req={time_now}")
