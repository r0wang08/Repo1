menu = ['Knackered Spam', 'Pip pip Spam', 'Squidgy Spam', 'Smashing Spam']
# Let's store menu items with their prices in a dictionary
menu_prices = {}
price = 0.50
for item in menu:
    menu_prices[item] = price
    price = price + 1
for name, price in menu_prices.items():
    print(name, ': $', format(price, '.2f'), sep='')

performances = {'Ventriloquism': '9:00am',
                'Snake Charmer': '12:00pm',
                'Amazing Acrobatics': '2:00pm',
                'Enchanted Elephants': '5:00pm'}

for i, j in performances.items():
    print(i, ':', j, sep='')


## Another randomn file 
    import random

num = random.randint(1, 10)

guess = int(input('Guess a number between 1 and 10'))
# Add while loop here
while(guess != num) :
    guess = int(input('Guess again'))

print('You win!') 

import random

num = random.randint(1,10)

guess = int(input('Guess a number between 1 and 10'))

times = 1
while guess != num:
    guess = int(input('Guess again'))
    times = times + 1
    if (times == 3):
        break

if (guess == num):
    print('You win!')
else:
    print('You lose! The number was', num)