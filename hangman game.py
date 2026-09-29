import random

# List of 5 predefined words
words = ["python", "computer", "program", "school", "coding"]

# Select a random word
word = random.choice(words)

# Store correctly guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
incorrect_guesses = 0
max_guesses = 6

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have 6 incorrect guesses.")

# Main game loop
while incorrect_guesses < max_guesses:

    # Display the word with blanks
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses:", incorrect_guesses, "/", max_guesses)

    # Check if the whole word has been guessed
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Get user's guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add guess to the list
    guessed_letters.append(guess)

    # Check whether the guess is correct
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)