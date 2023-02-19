value_menu = open('dollar_menu.txt', 'w')
value_menu.write('cheeky spam\n')
value_menu.write('cherrio spam\n')
value_menu.write('pip pip spam\n')
value_menu.close()

def read_dollar_menu():
        dollar_spam = open('dollar_menu.txt', 'r')
        for line in dollar_spam:
                 print(line)
        dollar_spam.close()
read_dollar_menu()