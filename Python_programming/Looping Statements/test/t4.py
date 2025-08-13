inventory = {}

while True:
    item_name = input("\nEnter an Item or Type 'Stop': ").title()
    if item_name == 'Stop':
        break

    qty = input("Enter the quantity: ")

    if not qty.isdigit():
        print("Invalid input, please enter valid Qty")
        continue

    quantity = int(qty)

    # Add data to inventory
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

# Display the inventory
    print("\n Inventory:")
for item, qt in inventory.items():  # fixed here
    print(f"Quantity of {item}: {qt}")
