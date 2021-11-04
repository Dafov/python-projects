import random

def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_num:
            print('Try again. Too low.')
        elif guess > random_num:
            print('Try again. Too high.')
    
    print(f'Congratulations! You have guessed the number {random_num}!')

guess(50)
