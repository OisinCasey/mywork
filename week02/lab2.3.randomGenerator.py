# program that prints a random number between 1 and 10

import random #imports a built in library for random number selection in python

low = int(input("Please input lower range: "))

high = int(input("Please input higher range: "))

number = random.randint(low, high)

print("here is a random number between {} and {}: {}".format(low, high, number))