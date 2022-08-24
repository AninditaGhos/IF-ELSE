#. Write a python program to calculate profit or loss.
actual_price=int(input("Enter the a_price:- "))
selling_price=int(input("Enter the s_price:_ "))
if actual_price < selling_price :
    print("PROFIT")
elif actual_price > selling_price :
    print("LOSS")
else:
    print("NO PROFIT NO LOSS")