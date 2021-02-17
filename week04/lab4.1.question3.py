# i can use the round function to round the percentage used
# for calculation to the nearest int
# another method would be to set the pass leveles to lower criteria
# e.g. elif percentage < 69.5:

percentage = float(input("Enter the percentage: "))

roundedPercentage = round(percentage)

if roundedPercentage <0 or roundedPercentage > 100:
    print ("Please enter a number between 0 and 100")
elif roundedPercentage < 40:
    print ("Fail")
elif roundedPercentage < 50:
    print("Pass")
elif roundedPercentage < 60:
    print("Merit 1")
elif roundedPercentage < 70:
    print("Merit 2")
else:
    print("Distinction")           