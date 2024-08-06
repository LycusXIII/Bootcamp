num1, num2 = input("Enter any 2 numbers separated by a space\n").split()

print(f"Values before swap {num1} {num2}")
num1, num2, = num2, num1
print(f"Values after swap {num1} {num2}")