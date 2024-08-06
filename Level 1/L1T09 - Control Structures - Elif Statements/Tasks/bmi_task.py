# Ask the user to input their height and weight
height, weight = input("Please enter your height in meters and weight in killograms separated by a space (Example 1.7 85)\n").split(" ")

# Calculates the BMI using the BMI = (weight in kg) / ((height in m)*(height in m)) and rounds to 2 decimals
bmi = round(float(weight) / float(height) ** 2, 2)

# Checks the users BMI to see if they are obese, slightly overweight, normal weight or underweight
if bmi >= 30:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 25:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")