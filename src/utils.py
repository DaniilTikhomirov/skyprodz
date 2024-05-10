import json
from typing import Any
import requests
import os.path


def unpack_json(path: str) -> Any:
    """
    открывает json файл
    :param path: путь к файлу
    :return: переобразованный json файл в list[dict] или пустой список
    """
    try:
        with open(os.path.relpath(path), "r", encoding="utf8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                return []
            else:
                return data
    except FileNotFoundError:
        return []


def write_xml_from_web(url: str, name: str) -> None:
    """
    записывает xml файл с сайта
    :param url:ссылка на сайт
    :param name:имя файла
    :return: None
    """
    req = requests.get(url)
    with open(os.path.join("..", "data", f"{name}.xml"), "wb") as file:
        file.write(req.content)
