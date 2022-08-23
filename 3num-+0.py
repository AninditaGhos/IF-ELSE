#Write a python program to check whether a number is negative, positive or zero.
num=int(input("Enter the number:- "))
if num>0:
    print(num,"is a positive number")
elif num<0:
    print(num,"is a negative number")
elif num==0:
    print(num,"is zero")
else:
    print(num,"didnot match")