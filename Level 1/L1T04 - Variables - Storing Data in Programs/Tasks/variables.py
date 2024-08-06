# SET my_string to "Hello World!"
# SET my_char to "A"
# SET my_integer to 86
# SET my_Float to 7.89
# PRINT f-string "{my_string} \n {my_char} \n {my_integer} \n {my_float}"
# note: the above by making use of the f-string adding variables with differente types 
# together without the need for type conversion and using the \n inside a string forces 
# the string to be split on a new line

my_string = "Hello World!"
my_char = "A"
my_integer = 86
my_float = 7.89

print(f"{my_string}\n{my_char}\n{my_integer}\n{my_float}")