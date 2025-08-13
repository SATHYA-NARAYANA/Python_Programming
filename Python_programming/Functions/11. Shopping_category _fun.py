category = input("\nEnter Product category:").title()
amount = float(input("Enter the order amount:"))

# define the function for discount
def discount_calc(category,ord_amt):
    dis_per = 0
    dis_amt = 0

    if category == "Food":
        dis_per = (10/100)
    elif category == "Electronics":
        dis_per = (15/100)
    elif category == "Clothing":
        dis_per = (20/100)

    dis_amt = ord_amt * dis_per
    after_dis_price = ord_amt - dis_amt
    return after_dis_price

final_price = discount_calc(category,amount)

print(f"\nOrder total after {category}: Rs.{final_price}")
        
        
