#Task 1
favorite_fruits = ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]
word_list = favorite_fruits

#Task 2
import random

word_list = ["Apple", "Banana", "Orange", "Grapes", "Watermelon"]
random_word = random.choice(word_list)
word = random_word

#Task 3
guess = input("Enter a letter: ")
if len(guess) == 1 and guess.isalpha():
    print("You entered:", guess)
else:
    print("Please enter a valid letter.")

#Task 4
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
