# Asks the user for an number
number = int(input("Please enter a number with no decimals.\n"))

# Makes use of the Modulo operator which returns the remainder after dividing number with 2
if (number % 2) == 0:
    print(f"This {number} is an even number.")

# If the remainder is not eqaul to 0 the number is then odd
else:
    print(f"This {number} is an odd number")