# Program takes in a number from user and 
# evaluates if it is odd or even using an
# if else statement
# Auhor: Oisin Casey

number = int(input("Enter an integer:"))

if (number % 2) == 0:
    print("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))