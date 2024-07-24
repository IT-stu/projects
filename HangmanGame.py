# Hangman Game
import random
# List of words for the game
words = ["apple", "banana", "cherry", "mango", "berry", "orange", "grape", "gowya"]

def choose_word():
    """Selects a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters filled in."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of allowed incorrect guesses
    
    print("Welcome to Hangman!")
    print("Guess the any Fruit at this list \n",words)
    print(display_word(word_to_guess, guessed_letters))
    
    while attempts > 0:
        guess = input("Guess a letter: ").lower()
        if len(guess)==0:
            print("Please enter any letter")
            continue
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.add(guess)
            print("Correct guess!")
        else:
            attempts -= 1
            print(f"Incorrect guess! You have {attempts} attempts left.")

        print(display_word(word_to_guess, guessed_letters))

        if "_" not in display_word(word_to_guess, guessed_letters):
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            ch=input("Enter 1 To Start again")
            break

    if attempts == 0:
        print(f"Sorry, you're out of attempts. The word was: {word_to_guess}")
        ch=input("Enter 1 To Start again = ")

if __name__ == "__main__":
    ch=1
    while(ch==1):
        play_hangman()
