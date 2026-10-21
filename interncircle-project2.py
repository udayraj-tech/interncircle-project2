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

def count_words(path):
    print(f"\n--- Word Counter for {path} ---")
    try:
        # Always open files with a with block so they close properly
        with open(path, encoding="utf-8") as f:
            text = f.read().lower()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

    # Clean punctuation and split into words
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    
    counts = Counter(words)
    
    if counts:
        print(f"Total words: {sum(counts.values())}")
        print(f"Unique words: {len(counts)}")
        print("\nTop 10 most common words:")
        # Print the ten most common words with their counts, aligned in columns
        for word, n in counts.most_common(10):
            print(f"{word:<15} {n:>5}")
    return counts

def main():
    best_score = 0
    while True:
        print("\n--- Main Menu ---")
        print("1) Play the game")
        print("2) Count words in a file")
        print("3) Quit")
        
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            score = play_game()
            if score > best_score:
                best_score = score
            print(f"Best score so far: {best_score}")
        elif choice == "2":
            filename = input("Enter the text file name (e.g., sample.txt): ").strip()
            count_words(filename)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()