import math

"""
The following program calculates investment or bond depending on the user's input
and outputs the results of either an investment or a bond.
"""

print("investment   - to calculate the amount of interest you'll earn on your investment")
print("bond         - to calculate the amount you'll have to pay on a home loan")

# Ask the user to choose between investments or bond
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:\n").lower()

# If the user chooses investment the following code will run
# which asks the user for a variety of information
# The amount of money the user wants to deposit
# the interest rate for the investment
# and for how long the investment will last
# then calculates the total amount for either a simple investment or a compound investment

if user_choice == "investment":
    deposit = float(input("The amount of money you are depositing ? (e.g. 10000)\n"))
    interest_rate = float(input("The interest rate ? (as percentage without the '%', e.g. 8)\n"))
    interest_rate = interest_rate / 100 # Changes user input to a % value e.g. 8 = 0.08
    years = int(input("Number of years you plan to invest ? (e.g. 20)\n"))
    interest = input("Would that be 'simple' or 'compound' interest ?\n").lower()

    if interest == "simple":
        total_amount = deposit * (1 + interest_rate * years)
        print(f"The totatl amount would be R{total_amount} after {years} years with simple interest.")
    
    elif interest == "compound":
        total_amount = round(deposit * math.pow((1 + interest_rate), years), 2)
        print(f"The totatl amount would be R{total_amount} after {years} years with compound interest.")
    
    else:
        print("Invalid choice was given the only 2 options are 'simple' or 'compound'")

# If the user chooses bond the following code will run
# which asks the user for a variety of information
# the current value of the house
# the interest rate of the bond
# The length of time you want to pay back the bond
# then calculates and outputs the total amount you need to repay each month

elif user_choice == "bond":
    house_value = float(input("What is the present value of the house ? (e.g. 100000)\n"))
    interest_rate = float(input("The interest rate ? (as percentage without the '%', e.g. 8\n"))
    # Changes user input to a % value e.g. 8 = 0.08
    # Changes the interest rate from annual  to monthly
    interest_rate = interest_rate / 100 / 12
    months = int(input("The number of months you plan to repay the bond ? (e.g. 120)\n"))
    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-months))

    print(f"The total amount you must repay each month is R{repayment:.2f}")
    # found an interesting way of rounding the decimals inside an f-string (used in the line above)
    # https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings

else:
    print("Invalid choice was given the only 2 options are 'investment' or 'bond'")