from src.mask import security_card, security_num

print(security_card("1234123412341234"))
print(security_num("73654108430135874305"))
print(security_card(1234123412341234))
print(security_num(73654108430135874305))
print(security_card("1234123412341234857"))
print(security_num("73654108430135874305579"))
print(security_card(1234123412341234846))
print(security_num(736541084301358743059843))
