valid = False
while not valid:
    password = input("Please enter your password")
    if len(password) <6:
        valid = False
    else:
        valid = True
        for char in range (0, len(password)):
            print("*", end=' ')

