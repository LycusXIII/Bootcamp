# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"               # Runtime error: Missing "" while assigning Lion to variable animal.
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"  # Logical error: Missing the f-string infront of the string, swapping number_of_teeth and animal_type for the correct desired output.

print(full_spec)             # Syntax error: Missing () for the print() function.

