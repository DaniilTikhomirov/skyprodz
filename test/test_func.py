from src.mask import security_card, security_num
from src.widget import mask_card_and_num

test = ["Maestro 1596837868705199",
        "Счет 64686473678894779589",
        "MasterCard 7158300734726758",
        "Счет 35383033474447895560",
        "Visa Classic 6831982476737658",
        "Visa Platinum 8990922113665229",
        "Visa Gold 5999414228426353",
        "Счет 73654108430135874305"]

# print(security_card("1234123412341234"))
# print(security_num("73654108430135874305"))
# print(security_card("1234123412341234857"))
# print(security_num("73654108430135874305579"))

for line in test:
    print(mask_card_and_num(line))
