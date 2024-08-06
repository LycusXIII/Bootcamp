'''
This program is a simple calculator app that takes 2 numbers and a
operation (+, -, * or /) from user inputs preforms the calculation
outputs the results and also records the calculation to a text file 
called 'equations.txt'
'''
import sys
import os


def calculations():
    '''
    This function asks the user for 3 inputs 2 numbers and an operator
    Args:
        None
    Returns:
        Returns the results of the calculation and also records it to a 
        text file called 'equations.txt'
    '''
    list_operators = ["+", "-", "*", "/"]
    while True:
        try:
            first_number = float(input("Enter your first number: "))
            operator = input("Choose an operator (+, -, *, /): ")
            # Checks if users input (operator) is part of the list
            if operator in list_operators:
                second_number = float(input("Enter your second number: "))
                if operator == "+":
                    answer = first_number + second_number
                elif operator == "-":
                    answer = first_number - second_number
                elif operator == "*":
                    answer = first_number * second_number
                elif operator == "/":
                    if second_number == 0:
                        raise ZeroDivisionError
                    answer = first_number / second_number
            elif operator not in list_operators:
                raise ValueError
            return first_number, operator, second_number, answer
        except ValueError:
            print("Invalid input please try again.")
            continue
        except ZeroDivisionError:
            print("Can't divide by zero please try again.")
            continue


def record_equations(equation):
    '''
    This function writes the equation the user preformed to the 
    'equations.txt' file.
    Args:
        equation: a string that contains the user choice of 2 numbers 
        and the operator use as well as the result of the calculation.
    Returns:
        None
    '''
    # Opens the file to write data to the file
    # If the file doesn't exit one will be created.
    with open('equations.txt', 'a+', encoding='utf-8') as file:
        file.writelines(equation + "\n")


while True:
    try:
        user_choice = int(input(
            "Please select 1 or 2 or if you want exit type -1.\n"
            + "1. Perform calculations ?\n"
            + "2. Display all recorded calculations.\n"))
        if user_choice == -1:
            sys.exit(0)
        if 1 != user_choice != 2:
            raise ValueError
        if user_choice == 1:
            number_1, operator_choice, number_2, result = calculations()
            output = f"{number_1} {operator_choice} {number_2} = {result}"
            record_equations(output)
            print(output + "\n")
            continue
        if user_choice == 2:
            # Checks if the file exists
            if not os.path.exists('equations.txt'):
                raise FileNotFoundError
            with open('equations.txt', 'r+', encoding='utf-8') as read_file:
                for line in read_file:
                    # strips unnecessary blank lines
                    print(line.rstrip())
                # Creates an empty line for more readability
                print()
    except ValueError:
        print("Invalid input please try again.")
        continue
    except FileNotFoundError:
        print("No previous equations has been stored.\n"
              +"Please preform some calculations and try again.\n")
        continue
