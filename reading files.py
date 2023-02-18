sales_log = open('dollar_menu.txt', 'w')
sales_log.write('The Spam Van\n')
sales_log.write('Sales Log')
sales_log.close()

other_name = open('dollar_menu.txt', 'r')
print(other_name.read())
other_name.close()