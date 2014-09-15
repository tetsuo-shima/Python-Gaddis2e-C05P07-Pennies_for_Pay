__author__ = 'dwight'

# Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is
# one penny the first day, two pennies the second day, and continues to double each day. The program should ask the
# user for the number of days. Display a table showing what the salary was for each day, and then show the total pay at
# the end of the period. The output should be displayed in a dollar amount, not the number of pennies.


def main():
    days_worked = int(input('Enter number of days worked: '))
    print("Your pay: $",
          format(calc_pay(days_worked), ',.2f'),
          sep='')


def calc_pay(days):
    pay = 0.0
    for day in range(days):
        pay = 2 ** day
    return pay / 100


main()