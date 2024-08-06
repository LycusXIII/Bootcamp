def func(): 
    """
    The following program uses a for loop and a if loop to print out the specific pattern of asteriks(*).
    It starts with one * and iterates up to five, then back down to one.
    """
# print(func.__doc__)  #Testing docstring

# Initialize an empty string for storing the pattern.
star = ""  

for i in range (1, 10):
    if i < 6:   
        star += "*"  
        print(star) 
    else:
        star = star[:-1]    # Removes the last character in the string
        print(star)