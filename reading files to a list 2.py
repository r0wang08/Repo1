value_menu = open('dollar2_menu.txt', 'w')
value_menu.write('cheeky spam\n')
value_menu.write('cherrio spam\n')
value_menu.write('pip pip spam')
value_menu.close()

# why not work when in a function def? works if remove def...line
def read_dollar2_menu():
    dollar_spam = open('dollar2_menu.txt', 'r')
    print('1st line:', dollar_spam.readline())
    print('2nd line:', dollar_spam.readline())
    dollar_spam.close()


