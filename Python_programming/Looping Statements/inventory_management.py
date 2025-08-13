inventory = {}

while True:
    item_name = input("\nEnter an Item or Type Stop:").title()
    if item_name == 'Stop':
        break
    qty = input("Enter the quantity:")

    if not qty.isdigit():
        print("Invalid input, please enter valid Qty")
        continue

    quantity = int(qty)

    # add data to invent
    if item_name in inventory:
        inventory[item_name] = inventory[item_name] + quantity
    else:
        inventory[item_name] = quantity
#display the user inventory if user enter Stop
print("\nInventory:")

for item, qt in inventory.items():
    print(f"Quantity of {item}:{qty}")
