"""
PROMPT "Enter your 3 favourite foods"
SET item1 to users first INPUT
SET item2 to users second INPUT
SET item3 to users third INPUT
PRINT item1
PRINT item2
PRINT item3
"""
print("Enter your 3 favourite foods from the menu items (press enter after each item)\n")
item1 = input()
item2 = input()
item3 = input()

print("Order confirmation! You have ordered:")
print(f"{item1} \n{item2} \n{item3}")