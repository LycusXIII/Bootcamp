def func():
    """
    The following program prompts the user for names until "John" is entered.
    Prints all incorrect names entered before "John".
    Args:
        User inputs.
    Returns:
        List of names that are incorrect.
    """
print(func.__doc__)  #Testing docstring

# Declares and Sets an empty list
incorrect_names = []

while True:
    names = input("Enter your name: ")

    # Checks to see if user input stored in names are alphabet letters (a-z)
    # https://www.w3schools.com/python/ref_string_isalpha.asp
    if names.isalpha(): 
        if names.lower() == "john":
            # Checks to see if list called incorrect_names is empty
            if not incorrect_names:
                print("No incorrect names were entered.")
            else:
                print(f"Incorrect names: {incorrect_names}")
            break
        else:
            # Adds user inputs stored in names to the end of the list called incorrect_names
            incorrect_names.append(names)
    else:
        print("Invalid input. Please enter a valid name (e.g. Smith)")