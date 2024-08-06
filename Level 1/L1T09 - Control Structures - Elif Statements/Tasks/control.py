# Ask the user their age and stores it as an int in variable age
age = int(input("What is your age ? (example 18)\n"))

# Checks if age is greater or equal to 18
if age >= 18:
    print("You are old enough!")
# Checks if age is greater then 16 and less then 18. 
# elif age == 17 as an alernative to the solution below.
elif age > 16 and age < 18:
    print("Almost there.")
# If the if or elfi statements doesnt catch anything else is executed
else:
    print("You're just to young!")