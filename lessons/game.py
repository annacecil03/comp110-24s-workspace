"""number guessing game."""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False

while not correct: #correct == False
    guess: int = int(input("guess a number: "))
    if guess == SECRET:
        print(f"Correct! {guess} is the number!")
        #something to help us exit
        correct = True
    elif guess > SECRET:
        print("Choice too high. Guess again!")
    else:
        print("Choice too low. Guess again.")
