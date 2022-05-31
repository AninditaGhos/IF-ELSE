a_cost=int(input("enter amount"))
s_price=int(input("enter amount"))
if a_cost>s_price:
    print("loss")
elif s_price>a_cost:
    print("profit")
else:
    print("same price")