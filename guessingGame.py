from ast import Break
from importlib import import_module
from random import random
import random


randNumber = random.randint(1,9)
chancesRemaining = 5
guess = input("Enter your guess here...")
while chancesRemaining < 6:    
    if int(guess) == randNumber:
        chancesRemaining = chancesRemaining - 1
        print("You win")
        break
    elif int(guess) > randNumber:
        chancesRemaining = chancesRemaining - 1
        print("Your guess is too high")
        guess = input("Enter your guess here...")
    elif int(guess) < randNumber:
        chancesRemaining = chancesRemaining - 1
        print("Your guess is too low")
        guess = input("Enter your guess here...")
    if chancesRemaining == 0:
        print("You ran out of chances. You lost")
