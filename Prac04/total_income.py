"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes_list = []
    months_count = int(input("How many months? "))

    for month in range(1, months_count + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes_list.append(income)
    print(report(incomes_list))


def report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for month, income in enumerate(incomes):
        total += income
        print("Month {:2} - Income: ${:8.2f} Total: ${:10.2f}".format(month + 1, income, total))


main()