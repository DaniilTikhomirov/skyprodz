def security_card(num: str | int) -> str:
    """маскирует номер карты"""
    num = str(num)
    if num.isdigit() and len(num) == 16:
        list_num: list = []
        list_num.extend(num)
        list_num[4], list_num[8], list_num[12] = " " + list_num[4], " " + list_num[8], " " + list_num[12]
        num = "".join(list_num)
        list_num = num.split()
        list_num[1] = list_num[1][:2] + "**"
        list_num[2] = "****"
        return " ".join(list_num)
    return "не правильно введены данные"


def security_num(num: str | int) -> str:
    """маскирует номер счета"""
    num = str(num)
    if num.isdigit() and len(num) == 20:
        return "**" + num[-4:]
    return "не правильно введены данные"
