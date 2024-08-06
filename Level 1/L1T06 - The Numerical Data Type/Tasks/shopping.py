products = list(map(str, input("Enter the names of 3 products, separated by a space\n").split(" ")))
prices = list(map(float, input("Enter the prices of the 3 products with the 2 decimal values, separated by a space\n").split(" ")))

average_price = round(sum(prices) / len(prices), 2)
print(f"The Total of {products[0]}, {products[1]}, {products[2]} is R{sum(prices)} and the average price of the items is R{average_price}")