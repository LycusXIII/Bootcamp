import math
# import statistics

# None of the built in functions used requires the math module for this task
# I found a module to give a built in functions for getting the median is the 'statistics' module.
# (decided not to use this module.)
# https://www.w3schools.com/python/ref_stat_median.asp#:~:text=The%20statistics.,in%20a%20set%20of%20data.

def built_in():
    '''
    Asks the user for 10 float numbers then calculates the total, maximum, minimum, 
    average and the median.
    Args:
        User input of 10 numbers.
    Returns
        The results of the calculations.
    '''

number_list = []
start = 1

while start <= 10:
    try:
        user_input = float(input(f"Please enter a number: ({start} of 10)    "))
        start += 1
        number_list.append(user_input)
    except ValueError:
        print("Please enter only numbers (e.g. 55.6, 100)")

print(f"The total of all the numbers is: {sum(number_list)}")   # Calculates the sum of all the numbers
print(f"The index of the maximum is: {number_list.index(max(number_list))}")    # Calculates the maximum
print(f"The index of the minimum is: {number_list.index(min(number_list))}")    # Calculates the minimum

average = round(sum(number_list)/len(number_list), 2)
print(f"The average of all the numbers is: {average}")

# Found out how to get the median of a list here.
# https://www.geeksforgeeks.org/find-median-of-list-in-python/
# Found no math module built in functions that can do this. 
# (also shows the statistics module in the link above)

number_list.sort()  # sorts the list in ascending order
middle_index = len(number_list) // 2 # // performs integer division and discards any remainder
result = (number_list[middle_index] + number_list[middle_index - 1]) / 2  # Calculates the median

# Using the statistic module.
# median = statistics.median(number_list)
# print(f"The median for the list is: {median}")

print(f"The median for the list of numbers is: {result}")