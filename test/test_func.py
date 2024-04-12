from src.mask import security_card, security_num
from src.widget import format_date, mask_card_and_num
from src.processing import filter_dict

test = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

test2 = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
         {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
         {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

print(filter_dict(test2, "CANCELED"))

print(security_card("1234123412341234"))
print(security_num("73654108430135874305"))
print(security_card("1234123412341234857"))
print(security_num("73654108430135874305579"))

for line in test:
    print(mask_card_and_num(line))

print(format_date("2018-07-11T02:26:18.671407"))
