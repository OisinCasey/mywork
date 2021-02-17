# This program reads in a string and strips any leading
# or trailing spaces. It also converts all letters to 
# lower case. This program also outputs the length of
# the original string and the normalised one
# Author: Oisin Casey

rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower() # this strips and spacecs and converts result to lower case

lengthOfRawString = len(rawString) # shows length of string as an int
lengthOfNormalised = len(normalisedString)

print("That string normalised is: {}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(lengthOfRawString, lengthOfNormalised))