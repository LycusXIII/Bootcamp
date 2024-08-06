# Asks the user to input their full name separated by a space
full_name = input("Please enter your full name separated by a space.\n")

# Tests to see if full_name empty
if full_name == "":
    print("You haven't entered anything. Please enter your full name.")
# Tests to see if full_name is less then 4 characters long (the replace() function counts spaces as well, that is why the replace() function is used)
elif len(full_name.replace(" ","")) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
# Tests to see if full_name is greater then 25 characters long (the replace() function counts spaces as well, that is why the replace() function is used)
elif len(full_name.replace(" ","")) > 25:
    print("“You have entered more than 25 characters. Please make sure that you have only entered your full name.")
# If all the other If statement  checks doesnt catch anything the else: will execute 
else:
    print("Thank you for entering your name.")