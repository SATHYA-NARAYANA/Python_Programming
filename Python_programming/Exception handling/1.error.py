try:

    product_id = input("Please enter your product id:")
    quantity = int(input("Please enter your product Quantity:"))
    price = float(input("Please enter the price per unit:"))

    total_amount = quantity * price
    print(f"\nTotal order amount for product id:{product_id}:{quantity:.2f}")

except ValueError:
    print("\n Quantity and price must be an intiger and price must be an numberic value")
