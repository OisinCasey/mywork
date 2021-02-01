height = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))
bmi = weight / height
formattedBmi = "{:.2f}".format(bmi)
print ("BMI is: " + formattedBmi + ".")