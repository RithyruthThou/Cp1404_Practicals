item = int(input("Enter your number of items"))
total = 0
for i in range (1, item+1):
    price = int(input("Price of Item"))
    total += price
print("Total price is {}".format("$"), total)
if total > 100:
    total = total - (total*0.1)
    print("After discount is {}".format("$"), total)