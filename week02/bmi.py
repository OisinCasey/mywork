height = int(input("Please enter your height in cm: "))
weight = int(input("Please enter your weight in kg: "))
bmi = weight / height
#next line allows formatting of output to a string with two figures after the decimal point
formattedBmi = "{:.2f}".format(bmi)
print ("BMI is: " + formattedBmi + ".")