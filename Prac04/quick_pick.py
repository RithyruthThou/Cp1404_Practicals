import random
minimum = 1
maximum = 45
lines = 6

picks = int(input("How many quick picks?"))
while picks <= 0:
    print("Number must be larger than 0")
    picks = int(input("How many quick picks?"))

for i in range(picks):
    lines_lists = []
    for k in range(lines):
        numbers = random.randint(minimum, maximum)
        while numbers in lines_lists:
            numbers = random.randint(minimum, maximum)
        lines_lists.append(numbers)
    lines_lists.sort()
    print(" ".join("{:2}".format(number) for number in lines_lists))



