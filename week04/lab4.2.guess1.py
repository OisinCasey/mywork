# Simple number guessing game using while loop
# Author Oisin Casey

numberToGuess = 34

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    print("Wrong!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes, the number was", numberToGuess)    