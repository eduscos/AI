# Q.1) Write a program to implement Hangman game using python. Hangman is a
# classic word-guessing game. The user should guess the word correctly by
# entering alphabets of the user choice. The Program will get input as single
# alphabet from the user and it will matchmaking with the alphabets in the original
# word.
# Ans:-

import random
def choose_word():
    words = ["python", "hangman", "programming", "developer", "computer"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word_to_guess = choose_word().lower()
    guessed_letters = set()
    attempts_left = 6
    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))
    while attempts_left > 0:
        user_guess = input("Enter a letter: ").lower()
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        if user_guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
            guessed_letters.add(user_guess)
        if user_guess not in word_to_guess:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")
        else:
            print("Correct guess!")
            print(display_word(word_to_guess, guessed_letters))
        if '_' not in display_word(word_to_guess, guessed_letters):
            print("Congratulations! You've guessed the word.")
            break
        if attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()