
import random
words = ["python", "apple", "computer", "college", "coding"]
secret_word = random.choice(words)
guessed_letters = []
max_attempts = 6
wrong_guesses = 0

print("================================")
print("       WELCOME TO HANGMAN       ")
print("================================")
while wrong_guesses < max_attempts:

    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        break

    # Take input from player
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guessed letter
    if guess in secret_word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

# Losing condition
if wrong_guesses == max_attempts:
    print("\nGame Over!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
