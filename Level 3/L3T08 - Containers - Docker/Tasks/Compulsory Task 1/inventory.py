'''
The following program takes data from 'inventory.txt' to populate a list
of objects made using the Shoe class the program offers a wide variety
of options via its menu for the user to use.
'''
import sys
import os
from tabulate import tabulate


# ==== The beginning of the class ====
class Shoe:
    '''
    This class represents attributes of a shoe.
    '''
    def __init__(self, country, code, product, cost, quantity):
        '''
        Initializes an object with these attributes.
        '''
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        '''
        Returns the cost of the object.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Returns the quantity of the object.
        '''
        return self.quantity

    def __str__(self):
        '''
        Returns each attribute of the object as a list of strings.
        '''
        return [self.country, self.code, self.product, str(self.cost),
                str(self.quantity)]


# ==== Shoe list ====
shoe_list = []


# ==== Functions outside the class ====
def read_shoes_data():
    '''
    Reads from 'inventory.txt' and creates Shoe objects using
    the Shoe Class. Checks if file exists otherwise closes the program.
    Args:
        None
    Returns:
        shoes_data: a list containing Shoe objects created from the
        'inventory.txt' file.
    '''
    file_exist()
    shoes_data = []
    with open('inventory.txt', 'r', encoding='utf-8') as file:
        # Skips the first line by moving onto the 'next' line
        next(file)
        for line in file:
            data = line.strip().split(',')
            try:
                country, code, product, cost, quantity = data
                shoe_object = Shoe(country, code, product, cost, quantity)
                shoes_data.append(shoe_object)
            except ValueError:
                print(f"Error converting data in line: {line}")
    return shoes_data


def capture_shoes(shoe_list):
    '''
    This functions allows a user to store data about a shoe and create a
    shoe object with the data then appends it to the shoe_list.
    Also does a validation check based on the code of the shoe to ensure
    no duplicates will be added.
    Args:
        shoe_list: a list containing shoe objects.
    '''
    while True:
        try:
            product = input("Enter the product name:  ")
            # Removes leading/trailing whitespaces (.strip())
            product = product.strip()
            if not product:
                raise ValueError("Product name cannot be empty.")

            code = input("Enter the products code:  ")
            code = code.strip()
            if not code:
                raise ValueError("Product code cannot be empty.")
            country = input("Enter the country of origin:  ")
            country = country.strip()
            if not country:
                raise ValueError("Product country cannot be empty.")
            cost = int(input("Enter the cost of the product without any "
                             "symbols:  "))
            if cost < 0:
                raise ValueError("Cost cannot be negative.")
            quantity = int(input("Enter the quantity of the shoe:  "))
            if quantity < 1:
                raise ValueError("Quantity cant be less then 1.")
            # List Comprehension https://shorturl.at/WpDti
            # If any https://shorturl.at/P3Ytg
            if any(shoe.code == code for shoe in shoe_list):
                print(f"The {product} with code {code} already exists "
                      "in die list.\n")
                continue

            shoe_object = Shoe(country, code, product, cost, quantity)
            shoe_list.append(shoe_object)
            save_shoe_list(shoe_list)
            print("Shoe successfully added to the list.")
            break
        except ValueError as error:
            if "invalid literal for int()" in str(error):
                print("\nCost and Quantity must be whole numbers.\n")
            else:
                print(f"\nInvalid input: {error}\n")


def view_all(shoe_list):
    '''
    This functions takes the shoe_list and iterates over it then prints
    out all the shoe objects in a table format
    Args:
        shoe_list: a list containing shoe objects.
    '''
    # Pythons tabulate module link below.
    # https://shorturl.at/2IJNN
    shoe_data = []
    for shoe in shoe_list:
        shoe_data.append(shoe.__str__())
    print(tabulate(shoe_data, headers=[
        "Country", "Code", "Product", "Cost", "Quantity"
        ], tablefmt='fancy_grid'))


def re_stock(shoe_list):
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    Args:
        shoe_list: a list containing shoe objects.
    '''
    low_stock_data = []
    # Using list Comprehension and the min() to find the lowest quantity
    lowest_quantity = min(shoe.get_quantity() for shoe in shoe_list)
    low_stock = [shoe for shoe in shoe_list
                 if shoe.get_quantity() == lowest_quantity]
    for shoe in low_stock:
        low_stock_data.append(shoe.__str__())
    print("The following table lists all the shoes with the lowest quantity.")
    print(tabulate(low_stock_data, headers=[
        "Country", "Code", "Product", "Cost", "Quantity"
        ], tablefmt='fancy_grid'))
    print()
    restocked = False
    while not restocked:
        try:
            selected_code = input("Enter the code of the shoe you want"
                                  " to re-stock or -1 to quit:  ").strip()
            if selected_code == "-1":
                break
            for shoe_data in low_stock_data:
                if selected_code in shoe_data:
                    current_quantity = int(shoe_data[-1])
                    print(f"The current stock is {current_quantity}")
                    add_quantity = int(input("Please enter the quantity to "
                                             "be restocked:  ").strip())
                    for shoe in shoe_list:
                        if shoe.code == selected_code:
                            shoe.quantity += add_quantity
                            save_shoe_list(shoe_list)
                            print(f"Product {shoe.product} has successfully "
                                  "been restocked")
                            print("Returning to main menu.")
                            restocked = True
                else:
                    print("The code you entered is invalid.")
                    continue
        except ValueError:
            print("Invalid input.")
            continue


def search_shoe(shoe_list):
    '''
    This function will search for a shoe from the list using the shoe
    code and prints object to the console.
    Args:
        shoe_list: a list containing shoe objects.
    '''
    found_shoe = False
    while not found_shoe:
        selected_code = input("Please enter the code of the shoe "
                              "you want to view or -1 to return to "
                              "main menu:\n").strip()
        searched_shoe = []
        if selected_code == "-1":
            break
        for shoe in shoe_list:
            if shoe.code == selected_code:
                searched_shoe.append(shoe.__str__())
                print(tabulate(searched_shoe, headers=[
                     "Country", "Code", "Product", "Cost", "Quantity"
                     ], tablefmt='fancy_grid'))
                found_shoe = True
                break
        else:
            print("That shoe does not exits in the inventory.")


def value_per_item(shoe_list):
    '''
    This function calculates the total value for each item,
    (value = cost * quantity) and prints using tabulate for
    better readability.
    Args:
        shoe_list: a list containing shoe objects.
    '''
    shoe_value = []
    for shoe in shoe_list:
        value = round(shoe.cost * shoe.quantity)
        shoe_value.append([shoe.country, shoe.code, shoe.product,
                           shoe.cost, shoe.quantity, value])
    print(tabulate(shoe_value, headers=[
        "Country", "Code", "Product", "Cost", "Quantity", "Total Value"
        ], tablefmt='fancy_grid'))


def highest_qty(shoe_list):
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    Args:
        shoe_list: a list containing shoe objects.
    '''
    high_stock_data = []
    # Using list Comprehension and max() to find the highest quantity
    highest_quantity = max(shoe.get_quantity() for shoe in shoe_list)
    high_stock = [shoe for shoe in shoe_list
                  if shoe.get_quantity() == highest_quantity]
    for shoe in high_stock:
        sale = "20% Off"
        high_stock_data.append([shoe.country, shoe.code, shoe.product,
                                shoe.cost, shoe.quantity, sale])
    print("The following table lists all the shoes that are currently on sale")
    print(tabulate(high_stock_data, headers=[
        "Country", "Code", "Product", "Cost", "Quantity", "Sale"
        ], tablefmt='fancy_grid'))


def file_exist():
    '''
    Checks if the file exists by using os.path.exists('inventory.txt')
    '''
    # Making use of the os module to check if the file exists.
    try:
        if not os.path.exists('inventory.txt'):
            raise FileNotFoundError
    except FileNotFoundError:
        print("File does not exists closing program.")
        sys.exit(0)


def save_shoe_list(shoe_list):
    '''
    This function writes the shoe_list to the text file 'inventory.txt'
    Args:
        shoe_list: the current shoe_list.
    '''
    file_exist()
    # Reads the first line of the text file so it wont be over written.
    with open('inventory.txt', 'r', encoding='utf-8') as read_file:
        headers = read_file.readline()

    with open('inventory.txt', 'w', encoding='utf-8') as write_file:
        write_file.write(headers)
        for shoe in shoe_list:
            str_shoe = ','.join(shoe.__str__())
            write_file.write(str_shoe + "\n")


# ==== Main Menu ====
'''
Main menu that the user uses to interact with the program
'''
while True:
    shoe_list = read_shoes_data()
    menu = input('''Select one of the following options:
c - capture shoe
v - view all shoes
r - restock shoe
s - search for a shoe
i - value per item
h - highest quantity shoe
e - exit
''').lower()

    if menu == "c":
        capture_shoes(shoe_list)
    elif menu == "v":
        view_all(shoe_list)
    elif menu == "r":
        re_stock(shoe_list)
    elif menu == "s":
        search_shoe(shoe_list)
    elif menu == "i":
        value_per_item(shoe_list)
    elif menu == "h":
        highest_qty(shoe_list)
    elif menu == "e":
        print('Goodbye!!!')
        # Stops the program.
        sys.exit(0)
    else:
        print("Invalid input please try again.")
        continue
