# Rock Paper Scissors
# Versus Random Generated Choice

from random import randint

print('Welcome! \n\nRock \nPapper \nScissors\n\n')
user_choice = input('Enter your choice: ').casefold()
computer_choice = ''
rand= randint(0, 2)

if user_choice: # checks if empty
    if rand == 0: # Rock
        computer_choice = 'rock'
        if user_choice == 'paper':
            print('Computer plays rock.')
            print('User wins!')
        elif user_choice == 'scissors':
            print('Computer plays rock.')
            print('Computer wins!')
        elif user_choice == computer_choice:
            print('Computer plays, ' + computer_choice)
            print("It's a tie.")
    elif rand == 1: # Paper
        computer_choice = 'paper'
        if user_choice == 'rock':
            print('Computer plays paper.')
            print('Computer wins!')
        elif user_choice == 'scissors':
            print('Computer plays paper.')
            print('User wins!')
        elif user_choice == computer_choice:
            print('Computer plays, ' + computer_choice)
            print("It's a tie.")
    elif rand == 2: # Scissors
        computer_choice = 'scissors'
        if user_choice == 'paper':
            print('Computer plays scissors.')
            print('Computer wins!')
        elif user_choice == 'rock':
            print('Computer plays scissors.')
            print('User wins!')
        elif user_choice == computer_choice:
            print('Computer plays, ' + computer_choice)
            print("It's a tie.")
        else:
            print('Invalid input.')

else:
    print('Invalid input.')
