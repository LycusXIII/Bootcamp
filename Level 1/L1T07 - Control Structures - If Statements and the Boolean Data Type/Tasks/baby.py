# Asks the user for an input and converts the intput to an integer
year_of_birth = int(input("What year were you born in ? (example 1990)\n"))

# Calculates the age of the user by taking the current year 2024 and subtracts it from the users input
age = 2024 - year_of_birth

# Uses an if else block to test the age of the user to allow or deny entry to the party
if age >= 18:
    print("Congrats you are old enough.")

# If all the other If statment checks doesnt catch anything the else: will execute 
else:
    print("You're not old enough to enter.")