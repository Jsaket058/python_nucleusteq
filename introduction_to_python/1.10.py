import random

def number_guessing_game() -> None:
    """
    A number guessing game between 1 and 100.
    """
    secret_number = random.randint(1, 100)
    print("Guess a number between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed it!")
            break

number_guessing_game()
