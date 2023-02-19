value_menu = open('dollar_menu.txt', 'w')
value_menu.write('cheeky spam\n')
value_menu.write('cherrio spam\n')
value_menu.write('pip pip spam\n')
value_menu.close()

dollar_spam = open('dollar_menu.txt', 'r')
dollar_menu = [line.strip() for line in dollar_spam]
print(dollar_menu)
dollar_spam.close()
 
 # have to next line = line.strip() into the for loop to work, using "line.strip()" in replace of "line" 
