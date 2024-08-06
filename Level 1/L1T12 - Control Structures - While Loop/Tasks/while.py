def func():
    """
    Calculates the average of a series of numbers entered by the user.
    The user is prompted to enter numbers one at a time until they enter -1 to stop
    Returns:
        The average of the numbers as a float or "No numbers were entered!"
    Raises:
        ValueError: If the user enters a non-numeric value.
    """

print(func.__doc__)  #Testing docstring

# Declares and sets values to 0 to ensure valid calculations.
amount_of_numbers = 0
sum_of_numbers = 0

# The try: except ValueError: code was found at the link below.
# https://docs.python.org/3/tutorial/errors.html
while True:
    try:
        # Gets the initial value from the user
        numbers = float(input("Please enter a number (type -1 to stop): "))

        # Used to stop the program and break out of the while loop.
        if numbers == -1:  
            break
        sum_of_numbers += numbers
        amount_of_numbers += 1

    # Catches any ValueError which is data types other than floats/integers
    except ValueError:  
        print("Invalid input. Please enter a valid number.")

# Check if at least one valid number was entered
if amount_of_numbers > 0:  
    average = sum_of_numbers / amount_of_numbers
    print(f"The average of the numbers entered is {average:.2f}")
else:
    print("No numbers were entered!")