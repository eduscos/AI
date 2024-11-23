# Q.1)Write a program to implement Hangman game using python.
# Description:
# Hangman is a classic word-guessing game. The user should guess the word
# correctly by entering alphabets of the user choice. The Program will get input as
# single alphabet from the user and it will matchmaking with the alphabets in the
# original
# Ans:-

import random

def choose_word():
    return random.choice(["python", "hangman", "programming", "code", "computer",
    "algorithm"])

def display_word(word, guessed):
    return ' '.join(letter if letter in guessed else '_' for letter in word)

def hangman():
    word, guessed, attempts = choose_word(), set(), 6
    print("Welcome to Hangman!")
    while attempts > 0:
        print(display_word(word, guessed))
        guess = input("Enter a letter: ").lower()
        if guess.isalpha() and len(guess) == 1:
            guessed.add(guess)
            if guess not in word:
                attempts -= 1
                print(f"Wrong guess! Attempts left: {attempts}")
            elif all(letter in guessed for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
            break
        else:
            print("Please enter a single alphabet.")
    if attempts == 0:
    print(f"Sorry, you're out of attempts. The word was: {word}")
    
if __name__ == "__main__":
    hangman()