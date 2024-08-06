# Asks for user input and set it as a float type
distance = float(input("How far will the package be sent in kilometers ?\n"))

# Asks the user for the type of transport
freight_Type = input("Which transport method would you like by Air at R0.36 per km or by Land at R0.25 per km (please type 'Air' or 'Land')\n").lower()

# sets freight to the correct value based on user input
if freight_Type == "air":
    freight = distance * 0.36
elif freight_Type == "land":
    freight = distance * 0.25

# Asks the user for the type of insurance
insurance_type = input("Would that be with Full insurance at R50.00 or Limited insurance at R25.00 (please type 'Full' or 'Limited')\n").lower()

# sets insurance to the correct value based on user input
if insurance_type == "full":
    insurance = 50.00
elif insurance_type == "limited":
    insurance = 25.00

# Asks the user if they want a gift cover or not
gift_type = input("With a Gift cover at R15.00 or without a gift cover (please type 'Yes' or 'No')\n").lower()

# sets gift to the correct value based on user input
if gift_type == "yes":
    gift = 15.00
elif gift_type == "no":
    gift = 0.00

# Asks the user if they want priority deliver or just the standard delivery
priority_type = input("Should that be Priority delivery at R100.00 or Standard delivery at R20.00 (please type 'Priority' or 'Standard')\n").lower()

# sets priority to the correct value based on user input
if priority_type == "priority":
    priority = 100.00
elif priority_type == "standard":
    priority = 20.00

# Asks the user if they want a postage sleeve or box
parcel_type = input("Would you like a postage sleeve at R100.00 or a box at R150.00 (please type 'Sleeve' or 'Box')\n").lower()

# sets parcel to the correct value based on user input
if parcel_type == "sleeve":
    parcel = 100.00
elif parcel_type == "box":
    parcel = 150.00

# Calcualtes the total cost and prints the results
total_cost = freight + insurance + gift + priority + parcel
print(f"The total cost for your delivery is R{total_cost}")