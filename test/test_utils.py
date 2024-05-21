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


# @patch('pandas.read_csv')
# def test_unpack_csv(mock_read):
#     sample_dict = {'PassengerId': [1, 2, 3, 4, 5],
#                    'Survived': [0, 1, 1, 1, 0],
#                    'Pclass': [3, 1, 3, 1, 3],
#                    'Name': ['name1', 'name2', 'name3', 'name4', 'name5'],
#                    'Sex': ['male', 'female', 'female', 'female', 'male'],
#                    'Age': [22.0, 38.0, 26.0, 35.0, 35.0],
#                    'SibSp': [1, 1, 0, 1, 0],
#                    'Parch': [0, 0, 0, 0, 0],
#                    'Ticket': ['tic1', 'tic2', 'tic3', 'tic4', 'tic5'],
#                    'Fare': [7.3, 71.3, 7.9, 53.1, 8.1],
#                    'Cabin': [None, 'C85', None, 'C123', None],
#                    'Embarked': ['S', 'C', 'S', 'S', 'S']}
#     mock_file = mock_read.return_value.__enter__.return_value
#     mock_file.read.return_value = pd.DataFrame(sample_dict)
#     assert unpack_csv(os.path("..", "data", "transactions.csv")) == pd.DataFrame(sample_dict)
