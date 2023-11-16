#Task 1
while True:
    guess = input("Guess a letter: ")
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

print("You guessed:", guess)

#Task 2
import random

word_list = ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]
secret_word = random.choice(word_list)

if guess in secret_word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")

#Task 3
def check_guess(guess):
    guess = guess.lower()
    
    if guess in secret_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")
        
        if guess.isalpha() and len(guess) == 1:
            check_guess(guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()
