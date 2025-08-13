non = ['eggs', 'Fish']
veg = ['apple', 'mango', 'Grapes', 'Onion']

item = input("Enter an item:\n")

if item in non:
    print(f"{item} is a non-veg item.")
elif item in veg:
    print(f"{item} is a veg item.")
else:
    print(f"{item} is not found in the list.")
