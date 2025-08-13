order_price = float(input("Enter your order price (Rs): "))
discount_percent = 0

if order_price >= 10000:
    discount_percent = 10
elif order_price >= 8000:
    discount_percent = 8
elif order_price >= 5000:
    discount_percent = 5
elif order_price >= 3000:
    discount_percent = 3
else:
    discount_percent = 0

discount_amount = (discount_percent / 100) * order_price
final_price = order_price - discount_amount

 
