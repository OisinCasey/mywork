#program that reads in two numbers and outputs
#the integer andswer and remainder
# Author: Oisin Casey


x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = int (x//y) #gives the int division, not float
remainder = x%y # gives the remainder


print("{} divided by {} is {} with remainder {}".format(x, y, answer, remainder))