purchase_amount = float(input("Please enter your shopping purchase amount (Rs):"))
base_discount = 0
if purchase_amount >= 10000 :
    base_discount = 10
elif purchase_amount >= 8000 :
    base_discount = 8
elif purchase_amount >= 5000 :
    base_discount = 5
elif purchase_amount >= 3000 :
    base_discount = 3
else:
    base_discount = 0
    base_discount = 0
    

discount_amount = (base_discount / 100) * purchase_amount
final_amount = purchase_amount - discount_amount

if purchase_amount >= 3000:
    print(f"\nCongratulations! You have received a {base_discount}% discount.")
    print("Your original purchase amount is:", purchase_amount)
    print("Discounted amount is:", discount_amount)
    print("Final amount after discount is:", final_amount)
else:
    print("\nSorry, you are not eligible for a discount.")
    print("Your final order amount is:", final_amount)

