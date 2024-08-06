'''This program uses different searching algorithm to display the results
using the given array: [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]'''


def sequential_search(item, arr):
    '''
    Performs the sequential search on the given array
    to find the index of the item
    Args:
        item: The target of the search
        arr: the array to search in
    Returns:
        The index location of the item in the array.'''
    # If item is not found, return None
    # Iterate over list. If we find our item, break loop
    # and return index
    for i in range(len(arr)):
        if arr[i] == item:
            return i


# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# https://www.programiz.com/dsa/insertion-sort
# Used the geeksforgeeks insertionSort method
def insertionSort(arr):
    '''
    Sorts the given array using the insertion sort algorithm
    Args:
        arr: The array to be sorted'''
    n = len(arr)
    if n <= 1:
        return
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def binary_search(item, arr):
    '''
    Preforms the binary search on the array to find the index of the item
    Args:
        item: The target of the search
        arr: the array to search in
    Returns:
        The index location of the item in the array. '''
    low, high = 0, len(arr) - 1

    # Keep iterating until low and high cross
    # Returns None if item not found
    while high >= low:
        # Find midpoint
        mid = (low + high) // 2

        # If item is found at midpoint, return
        if arr[mid] == item:
            # print(arr[mid])
            return mid
        # Else, if item at midpoint is less than item,
        # search the second half of the list
        elif arr[mid] < item:
            low = mid + 1
        # Else, search first half
        else:
            high = mid - 1


array = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]

# Since the array is an unordered list the linear search is the best
# for finding the desired items index
linear_index = sequential_search(9, array)
print(f"Results of the linear search:\n{linear_index}")

insertionSort(array)
print(f"Results of the insertion sort:\n{array}")

# Searching for specific words in a sorted dictionary.
binary_index = binary_search(9, array)
print(f"Results of the binary search:\n{binary_index}")
