value_menu = open('dollar_menu.txt', 'w')
value_menu.write('cheeky spam')
value_menu.write('cherrio spam')
value_menu.write('pip pip spam')
value_menu.close()


dollar_spam = open('dollar_menu.txt', 'r')
print(dollar_spam.read())
dollar_spam.close()