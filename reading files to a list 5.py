value_menu = open('dollar_menu.txt', 'w')
value_menu.write('cheeky spam\n')
value_menu.write('cherrio spam\n')
value_menu.write('pip pip spam\n')
value_menu.close()

dollar_spam = open('dollar_menu.txt', 'r')
dollar_menu = [line for line in dollar_spam]
print(dollar_menu)
dollar_spam.close()
 
 # This is simplier way to write code for same output as the file "reading files to a list 4" ? Still showing \n, see next file 
