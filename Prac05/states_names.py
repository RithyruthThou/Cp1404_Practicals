"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_NAMES)

state = input("Enter short state: ").upper()
while state != "":
    if state in STATE_NAMES:
        print(state, "is", STATE_NAMES[state])
        break
    else:
        print("Invalid short state")
        state = input("Enter short state: ").upper()

for key, long_state in STATE_NAMES.items():
    print("{:3} is {:3}".format(key, long_state))
#inname_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
#name = input("Enter Your Name")
#age = int(input("Enter Your Age"))
#name_to_age.update({name:age})
#for key,value in name_to_age.items():
#    print("{:10}-{:>10}".format(key,value))