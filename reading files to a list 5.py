value_menu = open('dollar_menu.txt', 'w')
value_menu.write('cheeky spam\n')
value_menu.write('cherrio spam\n')
value_menu.write('pip pip spam\n')
value_menu.close()

dollar_spam = open('dollar_menu.txt', 'r')
dollar_menu = []
for line in dollar_spam:
    line = line.strip()
    dollar_menu.append(line)
print(dollar_menu)
dollar_spam.close()

# it worked?? still have the '' and [] around the