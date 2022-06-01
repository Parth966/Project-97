from importlib import import_module
from random import random


randNumber = print(random.randint(1,9))
chancesRemaining = 5
guess = input("Enter your guess here...")
while chancesRemaining > 0:
    if guess == randNumber:
        chancesRemaining = chancesRemaining - 1
        print("You win")
    elif guess > randNumber:
        chancesRemaining = chancesRemaining - 1
        print("Your guess is too high")
    elif guess < randNumber:
        chancesRemaining = chancesRemaining - 1
        print("Your guess is too low")

    if chancesRemaining == 0:
        print("You ran out of chances. You lost")
