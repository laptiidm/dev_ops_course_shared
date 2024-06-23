import random

def number_guessing_game():

    secret_number = random.randint(1, 100)
    max_attempts = 5
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess == secret_number:
            print("Congratulations! You guessed the right number.")
            return
        
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts += 1

    
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")


number_guessing_game()
