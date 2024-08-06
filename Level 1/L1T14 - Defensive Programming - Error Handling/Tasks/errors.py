# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program")   # Syntax error: Missing () for the print() function.
print("\n")                             # Syntax error: Incorrect indentation and missing () for the print() function.

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                      # Syntax error: Incorrect indentation. Runtime error: Trying to use == to assign a value to a variable.
age = int(age_Str)                  # Syntax error: Incorrect indentation. Runtime error: Trying to change the data type of a string to an integer when the string contains letters. (A-Z)
print("I'm " + str(age) + " years old.")   # Syntax error: Incorrect indentation. Runtime error: Cant concatenate with an integer variable inside a string. (also added some spaces for better readability)

    # Variables declaring additional years and printing the total years of age
years_from_now = "3"                # Syntax error: Incorrect indentation.
total_years = age + int(years_from_now)  # Syntax error: Incorrect indentation # Runtime error cant add a string to an int.

print("The total number of years:" + str(total_years))    # Syntax error: Missing () for the print() function. # Logical error: Trying to concatenate an undefined variable inside "" making it a string.

# # Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12   #Runtime error using an undefined varialbe.
print("In 3 years and 6 months, I'll be " + str(total_months + 6) + " months old")    # Syntax error: Missing () for the print() function. Runtime error: cant concatenat a string with an integer. #Logical error: Did not account for the 6 months during calculations

# #HINT, 330 months is the correct answer