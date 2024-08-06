'''This program uses a modified Merge sort algorithm to order a list of
strings by string length from longest to shortest string'''


def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1

    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2
    return items


def merge(items, sections, temporary_storage):
    (start_1, end_1), (start_2, end_2) = sections
    i_1 = start_1
    i_2 = start_2
    i_t = 0

    while i_1 < end_1 or i_2 < end_2:
        if i_1 < end_1 and i_2 < end_2:
            # Added the len() to count the length of the string
            # and changed the < to >. (longest to the shortest string)
            if len(items[i_1]) > len(items[i_2]):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
            else:  # the_list[i_2] >= items[i_1]
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
            i_t += 1
        elif i_1 < end_1:
            for i in range(i_1, end_1):
                temporary_storage[i_t] = items[i_1]
                i_1 += 1
                i_t += 1
        else:  # i_2 < end_2
            for i in range(i_2, end_2):
                temporary_storage[i_t] = items[i_2]
                i_2 += 1
                i_t += 1
    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]


fruits = ["banana", "orange", "watermelon", "strawberry", "mango",
          "pineapple", "blueberry", "kiwi", "grape", "apple"]

vegetables = ["potato", "celery", "carrot", "broccoli", "cucumber",
              "spinach", "onion", "tomato", "beans", "cauliflower"]

months = ["January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October",
          "November", "December"]

sorted_fruits = merge_sort(fruits)
print(f"Sorted fruits:\n {sorted_fruits}")

sorted_vegetables = merge_sort(vegetables)
print(f"\nSorted vegetables:\n {sorted_vegetables}")

sorted_months = merge_sort(months)
print(f"\nSorted months:\n {sorted_months}")
