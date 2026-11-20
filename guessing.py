import random
import string
# project 1:number guessing game


def guessing_game():

    secret = random.randint(1, 20)
    tries = 0
    print("I'm thinking of a number between 1 and 20")

    while True:
        # get user input and nsure it's  a valid integer
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please type a whole number.")
            continue

        tries += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("You guessed it! The number was", secret)
            print("You took", tries, "tries.")
            break
