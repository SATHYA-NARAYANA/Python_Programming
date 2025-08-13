
purchase_amt = float(input("\nEnter your purchase amount:"))

Qualified_discount = 1000

if purchase_amt >= Qualified_discount:
    discount = purchase_amt * 0.1
    final_amount = purchase_amt - discount

    print("Congrulations !! you have got 10% discount on your purchase")
    print("Your purchase amount is:", purchase_amt)
    print("Discounted amount is:", discount)
    print("Final amount is:", final_amount)
else:
    print("\nSorry you are not elegible for discount")
    print("your final order amount is :", purchase_amt)
