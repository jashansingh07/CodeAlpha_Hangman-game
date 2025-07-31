import random

# Expanded word list (20 simple words)
words = [
    "apple", "house", "train", "grass", "water",
    "mouse", "cloud", "river", "plane", "bread",
    "shirt", "table", "plant", "beach", "chair",
    "clock", "stone", "piano", "watch", "lemon"
]
secret_word = random.choice(words).lower()
guessed_letters = []
max_incorrect = 6
incorrect_guesses = 0

print("Welcome to Hangman!")
print(f"The secret word has {len(secret_word)} letters.")

while True:
    # Show current progress
    display_word = ""
    for char in secret_word:
        if char in guessed_letters:
            display_word += char + " "
        else:
            display_word += "_ "
    print("Word:", display_word.strip())
    print("Previous guesses:", ' '.join(sorted(guessed_letters)))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")

    # Get user guess
    guess = input("Guess a letter: ").lower().strip()
    if not (len(guess) == 1 and guess.isalpha()):
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!")
    else:
        print("Incorrect guess.")
        incorrect_guesses += 1

    # Check for win
    if all(char in guessed_letters for char in secret_word):
        print(f"Congratulations! The word was '{secret_word}'. You win!")
        break
    # Check for loss
    if incorrect_guesses >= max_incorrect:
        print(f"Sorry, you've run out of guesses. The word was '{secret_word}'.")
        break

print("Game Over.")
