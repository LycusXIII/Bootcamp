# PROMPT Enter your name, age, house number, street name sperated by a ', ' with the space
# SET name to user INPUT
# SET age to user INPUT
# SET house_number to user INPUT
# SET street_name to user INPUT
# 
# PRINT f-string "This is {name}. He is {age} and lives at house number {house_number} on {street_name}"
# note the above by making use of the f-string adding variables with differente types together without the need for type conversion 

name, age, house_number, street_name = input("Please enter you name, age, house number and street name sperated by ', '\n").split(", ")

print(f"This is {name}. He is {age} and lives at house number {house_number} on {street_name}")