# this program reads in numbers until the user
# enters zero and then it prints them and the average of
# the numbers previously entered
# Author : Oisin Casey

numbers = []

number = int(input("Enter number (or 0 to quit): "))

while number !=0:
    numbers.append(number)

    number = int(input("Enter another number (or 0 to quit): "))
for value in numbers:
    print(value)

average = float(sum(numbers)) / len(numbers)
print( "The average is {}".format(average))