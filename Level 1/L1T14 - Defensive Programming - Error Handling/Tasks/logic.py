def func():
    """
    Checks the users age and determines whether they are eligible for a discount.
    If the user is over 60 they get 20% discount.
    If the user is 50 to 60 they get 10% discount.
    If the user is 18 to 49 they get no discount.
    If the user is 13 to 17 they get 5% discount.
    If the use is younger then 13 they are to young for a discount.
    """
# Checks and see if the user entered the correct data type.
try:
    age = int(input("Please enter your age: (e.g 35)\n"))
except ValueError:
    print("Invalid input. Please enter your age with only numerical digits.")

if age > 60:
    print("You are eligible for a discount of 20%.")
elif 50 < age <= 60:
    print("You are eligible for a discount of 10%")
elif 18 <= age < 50:
    print("You are not eligible for a discount.")
elif 13 <= age < 18:
    print("You are eligible for a discount of 5%")
else:
    print("You are not eligibel for a discount yet.")


# Logical error on line 18 which does not include if age = 50
# elif 50 <= age <= 60: (corrected code)