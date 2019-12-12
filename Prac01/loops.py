for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(11):
    print(i*10, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

num_stars = int(input("Please enter a number:"))
for i in range (0, num_stars):
    print("*", end=' ')
print("")

inc_stars = int(input("Please enter a number:"))
for i in range(0, inc_stars):
    for n in range(0, i+1):
        print("*", end=' ')
    print("\r")
while True:
    sales = float(input("Enter sales: $"))

    if 0 < sales < 1000:
        bonus = sales * 0.1
        print("The bonus is {}".format("$"), bonus)
    elif sales >= 1000:
        bonus = sales * 0.15
        print("The bonus is {}".format("$"), bonus)
    else:
        print("Invalid amount. Please enter another amount.")
