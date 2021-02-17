# program asks user for number between -10 and 10 and 
# will not end until the user inputs -1 as the answer


# Auhor: Oisin Casey

number = int(input("Guess the integer between -10 and 10:"))

while number != -1:
    number = int(input("Incorrect! Guess the integer between -10 and 10:"))
else:
     print("Correct!")