from src.mask import security_card, security_num


def mask_card_and_num(name_and_number: str) -> str:
    num = []
    alpha = []
    for word in name_and_number:
        if word.isalpha():
            alpha.append(word)
        elif word.isdigit():
            num.append(word)
    num = "".join(num)
    alpha = "".join(alpha)
    if alpha.lower() == "счет" or alpha.lower() == "счёт":
        return security_num(num)
    else:
        return security_card(num)

