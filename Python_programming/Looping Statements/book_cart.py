Books = {"Etl Testing" : 300,
         "Hadoop Testing" : 400,
         "Python Testing" : 700,
         "Automation Testing": 350,
         "Manual Testing" : 600
    }
for book, price in Books.items():
    print(f"{book} Book price: Rs.{price}")

totalcost = 0
discount_percentage = 10
shoppingcart = []

while True:
    selected_book = input("\nPlease select a book to purchase (or )type 'Done' to exit").title()
    if selected_book == 'Done':
        break
    if selected_book in Books:
        totalcost = totalcost + Books[selected_book]
        shoppingcart.append(selected_book)
        print(f"{selected_book} book added to cart.")

    else:
        print(f"Sorry the {selected_book} is not available in the store.")

if len(shoppingcart) > 2:
    discount = totalcost * discount_percentage/100
    Final_cost = totalcost - discount
    print(f"your total ordered amount is Rs.{totalcost}")
    print(f"Discount applies Rs .{discount}")
    print(f"Total Cost after discount: Rs. {Final_cost}")
else:
    print(f"Total Cost of the order: Rs {totalcost}")

print("\nThank you for shopping with us!, visit again! ")
    
