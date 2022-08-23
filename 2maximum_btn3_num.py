#Write a python program to find a maximum between three numbers.
num1=int(input("Enter the number:- "))
num2=int(input("Enter the number:- "))
num3=int(input("Enter the number:- "))
if num2<num1>num3:
    print(num1,"num1 is maximum")
elif num1<num2>num3:
    print(num1,"num2 is maximum")
elif num1<num3>num2:
    print(num2,"num3 is maximum")
else:
    print("no maximum number")