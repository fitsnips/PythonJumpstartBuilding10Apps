#!/usr/bin/env python3

import random

def print_banner():
    print('----------------------------------')
    print('     GUESS THE NUMBER App         ')
    print('----------------------------------')






print_banner()

random_number = random.randint(0,100)
loop = True
guess_count = 1

while loop == True:
    user_number = int(input('Guess a number between 0 and 100: '))

    if random_number == user_number:
        print('You the man! Guessed {} is correct in {} turns'.format(random_number, guess_count))
        loop = False
    elif random_number > user_number:
        print('{} is to low my friend! '.format(user_number))
        guess_count += 1
    elif random_number < user_number:
        print('{} is to high my friend! '.format(user_number))
        guess_count += 1
    else:
        print('You ran face first into to a wall, game over.')
        loop = False

