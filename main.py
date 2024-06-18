import os.path

from src.processing import filter_dict, find_description, sort_dict
from src.utils import unpack_csv, unpack_excel, unpack_json
from src.widget import format_date, mask_card_and_num


def main() -> None:
    """
    сборка всех модулей
    :return: None
    """
    list_func = [unpack_json, unpack_csv, unpack_excel]
    info = {
        1: {"name": "json", "file_name": "operations.json"},
        2: {"name": "csv", "file_name": "transactions.csv"},
        3: {"name": "exel", "file_name": "transactions_excel.xlsx"},
    }
    status_list = ["EXECUTED", "CANCELED", "PENDING"]

    print("Привет! Добро пожаловать в программу работы с банковскими транзакициями.")
    print("Выберите необходимый пункт меню:")

    while True:
        print(
            """1. Получить информацию о транзакциях из json файла
2. Получить информацию о транзакциях из csv файла
3. Получить информацию о транзакциях из xlsx файла
"""
        )
        user_num = int(input())
        name = info[user_num]["name"]
        file_name = info[user_num]["file_name"]
        my_func = list_func[user_num - 1]
        if 1 <= user_num <= 3:
            break

        else:
            print("я не знаю как с этим работать попробуйте выбрать другое")
            print()

    print(f"Для обработки выбран {name} файл.")
    data = my_func(os.path.join("data", str(file_name)))

    while True:
        print("Введите статус по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        user_status = input().upper()
        if user_status in status_list:
            data = filter_dict(data, argument=user_status)
            print(f'Операции отфильтрованы по статусу "{user_status}"')
            print()
            break

        else:
            print(f'Статус операции "{user_status}" недоступен.')
            print()

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                user_input = input().lower()
                if "возраст" in user_input:
                    data = sort_dict(data, reverse=False)
                    print("отсортировано по возростанию")
                    print()
                    break

                elif "убыван" in user_input:
                    data = sort_dict(data, reverse=False)
                    print("отсартировано по убыванию")
                    print()
                    break

                else:
                    print("повторите попытку и напишите немного по дргуому")
                    print()
            break

        elif user_input == "нет":
            break

        else:
            print("такого варианта нет")
            print()

    while True:
        print("Выводить только рублевые тразакции? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            # проверка на рубли для разных файлов
            data = [
                i
                for i in data
                if i.get("operationAmount", {"currency": {"code": ""}}).get("currency").get("code") == "RUB"
                or i.get("currency_code") == "RUB"
            ]
            break

        elif user_input == "нет":
            break

        else:
            print("не нашел такого варианта, попробуйте еще раз")
            print()

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_input = input().lower()
        if user_input == "да":
            print("введите слово по которому отсортировать")
            print()
            user_input = input()
            data = find_description(data, find_line=user_input)
            break

        elif user_input == "нет":
            break

        else:
            print("не нашел такого варианта, попробуйте еще раз")
            print()

    print("Распечатываю итоговый список транзакций...")
    print()
    print(f"Всего банковских операций в выборке: {len(data)}")

    for operation in data:
        date = format_date(operation.get("date", "9999-99-99T99:99:99.999999"))
        to_ = mask_card_and_num(operation.get("to", "null"))
        description = operation.get("description", "")
        currency = ""
        summ = "0"
        if operation.get("amount", False):
            summ = operation["amount"]
            currency = operation["currency_name"]

        elif operation.get("operationAmount", False):
            summ = operation["operationAmount"]["amount"]
            currency = operation["operationAmount"]["currency"]["name"]

        if "перевод" in description.lower():
            from_ = mask_card_and_num(operation["from"])
            print(
                f"""{date} {description}
{from_} -> {to_}
{summ} {currency}
"""
            )
        else:
            print(
                f"""{date} {description}
{to_}
{summ} {currency}
            """
            )


if __name__ == "__main__":
    main()
