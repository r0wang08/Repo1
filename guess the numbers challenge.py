import random

num = random.randint(1, 10)

guess = int(input('Guess a number between 1 and 10\n'))
times = 1

while guess != num:
    guess = int(input('Guess again\n'))
    times += 1
    if times == 3:
        break

if guess == num:
	  print('You win!')
else:
    print('You lose! The number was', num)
    

def lotto_numbers():
    lotto_nums = []
    for i in range(5):
        lotto_nums.append(random.randint(1, 53)) 
    
    return lotto_nums
  
def main():
    numbers = lotto_numbers()
    print('Lotto numbers: ', numbers)
    
main()
