# Altered version of simple number guessing game
# to tell the user if guess is high or low
# also chooses a ranom into between 0 - 100 
# for the number to guess
# Author: Oisin Casey
import random

numberToGuess = random.randint(0, 100)

guess = int(input("Please guess the number between 0 and 100:"))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low!")
    else:
        print("Too high!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes, the number was", numberToGuess)    