#Write a python program to input the month number and print the number of days in that month.
month_number=int(input("Enter the month number:- "))
a=1, 3,5,7,9,11
b=4,6,8,10,12
if month_number in a:
    print("month number",month_number,"has 30 numbers of day")
elif month_number in b:
    print("month number",month_number,"has 31 numbers of day")
else:
    print(" month number",month_number,"has 28numbers of day and in leap year 29 days")