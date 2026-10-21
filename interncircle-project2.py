import random
import string
from collections import Counter

def play_game():
    print("\n--- Number Guessing Game ---")
    # Import random once at the top, and pick the number before the loop starts
    secret = random.randint(1, 100)
    attempts = 0
    max_score = 100
    penalty = 10

    while True:
        raw_input = input("Guess a number between 1 and 100 (or type 'q' to quit): ").strip()
        if raw_input.lower() == 'q':
            return 0

        try:
            guess = int(raw_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        attempts += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            # Score is 100 minus 10 points per wrong guess, minimum 0
            score = max(0, max_score - ((attempts - 1) * penalty))
            print(f"Correct! You guessed it in {attempts} attempts. Your score: {score}")
            return score