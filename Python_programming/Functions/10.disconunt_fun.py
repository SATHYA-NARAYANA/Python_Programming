products = {
    'Pen': 100,
    'T-Shirt': 1000,
    'Watch': 2000
}

quantities = {}

for item in products:
    quantities[item] = int (input(f"\nEnter quantity of {item}:"))

print(quantities)

final_amount = 0

for prod, qty in quantities.items():

    product_price = products[prod]
    total_amount = qty * product_price
    final_amount += total_amount # finalamount = finalamount +total_amount

# function for discount elegible

def get_discount(order_amt):
    if order_amt >=100 and order_amt <=1000:
        return order_amt * 0.05
    elif order_amt >1000:
        return order_amt * 0.10
    else:
        return order_amt * 0.0

# calling function
discount = get_discount(final_amount)

#final Display result
print(f"\nTotal product price is Rs: {final_amount:.2f}")
print(f"Discount: Rs {discount:.2f}")
print(f"Final price after discount :Rs. {final_amount -discount:.2f}")

    
