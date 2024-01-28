'''
Aryan Singhal
CIS 41A   Winter 2024
Unit E, Problem E
'''

import random

def guessing_game():
    secret_num = random.randint(1, 100)
    guess_count = 0

    print("Welcome to the guessing game.")
    print("You need to guess a number from 1 to 100.")

    while True:
        guess = int(input("What is your guess? "))
        guess_count += 1

        if guess < secret_num:
            print("Guess is too low.")
        elif guess > secret_num:
            print("Guess is too high.")
        else:
            print(f"Congratulations!\nYou guessed the secret number in {guess_count} guesses!")
            break

guessing_game()


'''
Execution results:

#1
Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high.
What is your guess? 25
Congratulations!
You guessed the secret number in 2 guesses!

#2
Welcome to the guessing game.
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too high.
What is your guess? 25
Guess is too low.
What is your guess? 37
Guess is too high.
What is your guess? 30
Guess is too high.
What is your guess? 27
Guess is too low.
What is your guess? 28
Congratulations!
You guessed the secret number in 6 guesses!
'''