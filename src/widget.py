from src.mask import security_card, security_num


def mask_card_and_num(name_and_number: str) -> str:
    """проверяет номер это или счет и маскирует карту или счет"""
    num_list = []
    alpha_list = []
    for word in name_and_number:
        if word.isalpha() or word == " ":
            alpha_list.append(word)
        elif word.isdigit():
            num_list.append(word)
    num = "".join(num_list)
    alpha = "".join(alpha_list).strip()
    if alpha.lower() == "счет" or alpha.lower() == "счёт":
        security_num_ = security_num(num)
        if security_num_ != "не правильно введены данные":
            return f"{alpha} {security_num_}"
        return security_num_
    else:
        security_num_ = security_card(num)
        if security_num_ != "не правильно введены данные":
            return f"{alpha} {security_num_}"
        return security_num_


def format_date(date_time: str) -> str:
    """форматирует дату и время"""
    date_time_list = date_time.split("-")
    date_time_list[-1] = date_time_list[-1].split("T")[0]
    date_time = ".".join(date_time_list[::-1])
    return date_time
