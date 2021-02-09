# This program prints out a random fruit from a list
# Author: Oisin Casey

import random # python library import

fruits = ['Apple', 'Banana', 'Mango', 'Orange', 'Pear', 'Plum']

# choose a number between zero (first in an array) and length-1 (the last in the array)

index = random.randint(0, len(fruits)-1)

fruit = fruits[index]
print("A random fruit: {}".format(fruit))