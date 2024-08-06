def stock_value():
    '''
    The following programs takes the list and dictionaries provided to calculate the 
    current stock value.
    Args:
        List and dictionaries provided.
    Returns:
        The total stock value.
    '''

menu = ["Scrambled eggs", "Avo toast", "Coffee", "Tea", "Hot chocolate"]
stock = {'Scrambled eggs' : 15, 'Avo toast': 16, 'Coffee' : 22, 'Tea': 14, 'Hot chocolate':18}
price = {'Scrambled eggs' : 29.50, 'Avo toast': 18.50, 'Coffee' : 25.00, 'Tea': 20.50,
        'Hot chocolate': 23.00}

# Sets the total stock value to zero.
total_stock = 0

# Iterates through the list
for item in menu:
    # Calculates the total stock by getting the values from the the dictionaries
    # where the key is the same as item
    total_stock += stock[item] * price[item]

# Outputs the calculation and rounds to 2 decimals.
print(f"The total stock value is R{total_stock:.2f}")