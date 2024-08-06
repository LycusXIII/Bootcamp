'''
This program makes use of recursing instead of loops to get the 
desired calculation results.
'''

def adding_up_to(num_list, index):
    '''
    This function takes a list and a number the number indicates the
    index in where the function should add all the numbers till and
    including the index position.
    Args:
        list: a list of numbers.
        number: A number that represents the index point.
    Returns:
        The sum of all the numbers 
    '''
    if index >= 0:
        # Recursively calls the function till index is less then 0
        return num_list[index] + adding_up_to(num_list, index - 1)
    return 0


def printing_output(list_numbers, index_num, results):
    '''
    This function takes 3 args then prints out the results in a readable
    format.
    Args:
        list_numbers: a list of integers.
        index_num: a number that represents the index point.
        results: the result after the calculations from adding_up_to()
        function.
    Returns:
        None
    '''
    # Prints out desired output in a readable format.
    print(f"=> {results}")
    print(f"=> adding numbers all the way up to index {index_num} "
      + f"{list_numbers[:index_num + 1]}")


list_of_integers = [1, 4, 5, 3, 12, 16]
INDEX_NUMBER = 4
total = adding_up_to(list_of_integers, INDEX_NUMBER)
printing_output(list_of_integers, INDEX_NUMBER, total)

list_of_integers = [4, 3, 1, 5]
INDEX_NUMBER = 1
total = adding_up_to(list_of_integers, INDEX_NUMBER)
printing_output(list_of_integers, INDEX_NUMBER, total)
