#Ask the user if they are a Salesperson or a Manager
employee_type = input("Are you a salesperson or a manager (please type 'Salesperson' or 'Manager')\n").lower()

#Checks if the employee is a salesperson
if employee_type == "salesperson":
    #Ask the user for their gross sales for this month
    gross_sales = float(input("Enter gross sales for the month: (exmaple 10.00)\n"))
    #Calculates the commision they earned for this month
    commision = gross_sales * 0.08
    #Calculates the monthly wages
    monthly_wage = round(commision + 2000.00, 2)
    #Prints out the results
    print(f"The monthly wage for the Salesperson is R{monthly_wage}")

elif employee_type == "manager":
    #Ask the user for how many hours they worked this month
    hours_worked = float(input("Enter number of hours worked for this month: (example 160)\n"))
    #Calculates the monthly wages
    monthly_wage = hours_worked * 40.00
    #Prints out the results
    print(f"The monthly wage for the Manager is R{monthly_wage}")

# if not employee type was selected
else:
    print("No employee type was seleceted")