# This gives the answers to q7 of week 3 lab
# Author: Oisin Casey

#Q7
##message = 'I have eaten ' + 99 + ' burritos.'
##print(message)

##The above doesnt work as you cannot concatenate int
# and strings in python. You must first cast or convert
# one to the other like this:

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# Q8 'egg' is a valid variable name as it starts with a character
# variable names cannot lead with a number

#Q9 int(), float(), str()

