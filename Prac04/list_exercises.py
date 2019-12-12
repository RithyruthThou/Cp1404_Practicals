
Number_list = []
for loop_times in range(5):
    Number = int(input("Number: "))
    Number_list.append(Number)
print("The first number is {}".format(Number_list[0]))
print("The last number is {}".format(Number_list[4]))
print("The smallest number is {}".format(min(Number_list)))
print("The largest number is {}".format(max(Number_list)))
print("The average of the numbers is {}".format(sum(Number_list)/len(Number_list)))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


valid = False
while not valid:
    name = str(input("Please enter username: "))
    if name in usernames:
        print("Access Granted")
        valid = True
    else:
        print("Access Denied")