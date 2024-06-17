import os.path

from src.processing import filter_dict, find_description, sort_dict
from src.utils import unpack_csv, unpack_json, unpack_excel


def main() -> None:
    info = {
        1: {'name': 'json', 'func': unpack_json, 'file_name': 'operations.json'},
        2: {'name': 'csv', 'func': unpack_csv, 'file_name': 'transactions.csv'},
        3: {'name': 'exel', 'func': unpack_excel, 'file_name': 'transactions_excel.xlsx'}}
    sort_info = ['EXECUTED', 'CANCELED', 'PENDING']

    print("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями. 
Выберите необходимый пункт меню:

1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла
""")

    user_num = int(input())
    print(f"Для обработки выбран {info[user_num]['name']} файл.")

    name = info[user_num]['file_name']
    file = info[user_num]['func'](os.path.join("data", name))

    print("""Введите статус по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

    while True:
        user_sort = input().upper()
        if user_sort in sort_info:
            file = filter_dict(file, argument=user_sort)
        else:
            continue


if __name__ == '__main__':
    main()
