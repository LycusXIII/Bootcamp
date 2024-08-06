'''
This program makes use of recursion to find the largest numbers in a list.
'''


def largest_number(integer_list, highest_number):
    '''
    This function uses recursion to find the largest number in a list
    Args:
        list_of_numbers: a list of numbers
    Returns:
        The largest number
    '''
    if len(integer_list) == 0:
        # Returns the first index if the list has only 1 number
        return highest_number
    # Creates a new list with the remaining numbers in the list
    num1 = integer_list[0]
    if highest_number < num1:
        highest_number = num1
        integer_list = integer_list[1:]
    else:
        integer_list = integer_list[1:]
    return largest_number(integer_list, highest_number)

NUMBER = 0
numbers_list = [1, 4, 5, 3]
result = largest_number(numbers_list, NUMBER)
print(f"=> {result}")

numbers_list = [3, 1, 6, 8, 2, 4, 5]
result = largest_number(numbers_list, NUMBER)
print(f"=> {result}")
