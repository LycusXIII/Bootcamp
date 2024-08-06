star = ""

for i in range (1, 8):
    if i == 1 or i == 7:
        star = "*" * 5
        print(star)
    else:
        star = (" " * (6 - i)) + "*"
        print(star)
        