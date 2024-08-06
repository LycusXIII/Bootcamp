# Declared 3 variables as booleans and set the as False
warm = False
weekend = False
sunny = False

# Found out about the in operator from this website https://realpython.com/python-in-operator/
# Asks user for an input, lowers all text to lowercase for ease of use
user_Input = input("Is the current temperatur above 20 Yes/No \n").lower()
warm = user_Input in ("yes", "y")

# Asks user for an input, lowers all text to lowercase for ease of use
user_Input = input("Is it the weekend Yes/No \n").lower()
weekend = user_Input in ("yes", "y")

# Asks user for an input, lowers all text to lowercase for ease of use
user_Input = input("Is it sunny outside Yes/No \n").lower()
sunny = user_Input in ("yes", "y")

# Declares and sets the users_outfit to an empty string
users_outfit = ""

# Checks if the warm variable is True or False
if warm == True:
    # adds the "short-sleaved shirt" to the variable users_outfit
    users_outfit += "short-sleeved shirt"
else:
    users_outfit += "long-sleeved shirt"
# Checks if the weekend variable is True or False
if weekend == True:
    # adds the " with shorts" to the variable users_outfit
    users_outfit += " with shorts"
else:
    users_outfit += " with jeans"
# Checks if the sunny variable is True or False
if sunny == True:
    # adds the " and a cap" to the variable users_outfit
    users_outfit += " and a cap"
else:
    users_outfit += " and a raincoat"

# Outputs what the user should wear today
print(f"Today you should wear a {users_outfit}")