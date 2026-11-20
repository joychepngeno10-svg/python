import random


def guessing_game():
    print("welcome to the number guessing game!")
    print("i'm thinking of a number between 1 and 100.")
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        # Get user input and ensure it's a valid integer
        user_input = input("Enter your guess: ").strip()

        try:
            guess = int(user_input)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        attempts += 1
        # check the guess against the secret number
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number in",
                  attempts, "attempts.")
        break


# run the guessing game
if __name__ == "__main__":
    guessing_game()
