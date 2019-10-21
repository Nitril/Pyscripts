import random
import sys


def guessgame():
    number = random.randint(1, 101)

    print("I am thinking of a number")

    guess = int(input("What's your guess?"))
    attempts = 3
    while isinstance(guess, int):

        print(f"Your number is: {guess}")

        if guess > number:
            print("Too high")
            guess = int(input("What's your guess?"))
        elif guess < number:
            print("Too low")
            guess = int(input("What's your guess?"))
        else:
            print("You got it!")
            sys.exit(0)
            return


# elif not guess.isdigit():
#     print("You have not provided a number. Try again.")

guessgame()
