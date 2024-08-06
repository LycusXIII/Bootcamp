def alternate_cases():
    """
    Takes the sample string (that's provided) and makes each alternate character an upper case character
    and each other alternate character a lower case character
    Args:
        Sample string: sample_String = "String to be modified"
    Returns:
        A new string with alternating characters of upper case and lower case.
    """
print(alternate_cases.__doc__)  #Testing docstring

sample_string = "String to be modified"
modified_char = ""                      # Declares and sets as an empty string

for i in range(len(sample_string)):
    if i % 2 == 0:
        modified_char += sample_string[i].upper()
    else:
        modified_char += sample_string[i].lower()
print(modified_char)

def alternate_words():
    """
    Takes the sample string (that's provided) and makes each alternate word a lower case character
    and each other alternate word an upper case character
    Args:
        Sample string: sample_String = "String to be modified"
    Returns:
        A new string with alternating words of lower case and upper case.
    """
print(alternate_words.__doc__)   #Testing docstring

split_string = sample_string.split()    # Splits the sample string and convertion it into a list
modified_words = []                     # Declares and sets an empty list

for i in range(len(split_string)):
    if i % 2 == 0:
        modified_words.append(split_string[i].lower())
    else:
        modified_words.append(split_string[i].upper())

final_string = " ".join(modified_words)     # Joins the list with " " in between to make it a string variable.
print(final_string)