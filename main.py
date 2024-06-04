import os.path

from src.utils import unpack_json, unpack_csv, unpack_excel
from src.processing import filter_dict, sort_dict, find_description


def main() -> None:
    dict_function = {1: [unpack_json, "json", "operations.json"],
                     2: [unpack_csv, "csv", "transactions.csv"],
                     3: [unpack_excel, "exel", "transactions_excel.xlsx"]}
    list_status = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        print("""Программа: Привет! Добро пожаловать в программу работы с банковскими транзакициями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из json файла
    2. Получить информацию о транзакциях из csv файла
    3. Получить информацию о транзакциях из xlsx файла""")
        answer = input()
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= 3:
                print(f"Для обработки выбран {dict_function[answer][1]} файл.")
                info = dict_function[answer][0](os.path.join("data", dict_function[answer][2]))
                break
            else:
                print("не правильно введены данные попробуй еше раз")
                continue
        else:
            print("не правильно введены данные попробуй еше раз")
            continue

    while True:
        print()
        print("""Введите статус по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        answer = input().upper()
        if answer in list_status:
            info = filter_dict(info, answer)
            print(f"Операции отфильтрованы по статусу {answer}")
            print()
            break

        else:
            print(f"Статус операции {answer} недоступен.")
            continue

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        answer = input().lower()
        if answer == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            answer = input().lower()
            if answer.count("возростан") > 0:
                info = sort_dict(info)
                break
            elif answer.count("убыван") > 0:
                info = sort_dict(info, True)
                break
            else:
                print("не верно ведены данные, пропустить ? да/нет")
                answer = input().lower()
                if answer == "да":
                    break
                else:
                    continue
        else:
            break
    print("Выводить только рублевые тразакции? Да/Нет")
    answer = input().lower()
    if answer == "да":
        info = list(filter(lambda x: x.get("operationAmount").get("currency").get("code") == "RUB", info))
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    answer = input().lower()
    if answer == "да":
        print("ведите слово для поиска")
        answer = input()
        info = find_description(info, answer)
    print(info)


if __name__ == '__main__':
    main()
