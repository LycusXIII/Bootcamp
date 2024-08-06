# SET num1 to 99.23
# SET num2 to 23
# SET num3 to 150
# SET string1 to "100"
# PRINT f-string "{num1} \n {num2} \n {num3} \n {string1}"
# note: the above by making use of the f-string adding variables with differente types 
# together without the need for type conversion and using the \n inside a string forces 
# the string to be split on a new line

num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)

print(f"{num1}\n{num2}\n{num3}\n{string1}")