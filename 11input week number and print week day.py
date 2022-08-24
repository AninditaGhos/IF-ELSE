#Write a python program to input week number and print week day.
week_num=int(input("Enter the week number:- "))
if week_num==1:
    print("Monday")
elif week_num==2:
    print("Tuesday")
elif week_num==3:
    print("Wednesday")
elif week_num==4:
    print("Thursday")
elif week_num==5:
    print("Friday")
elif week_num==6:
    print("Saturday")
elif week_num==7:
    print("Sunday")
else:
    print(week_num,"is not a week_num")