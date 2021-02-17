# takes in decimal dollar values both
# negative and positive an outputs
# an absolute value in cents
# Author: Oisin Casey

dollarAmount = float(input("Please enter amount:"))
absoluteCents = int(abs(dollarAmount*100))

print("The amount in cent is: " + str(absoluteCents))