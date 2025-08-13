no_of_items = (int(input("\nEnter the number of items in your shopping cart:")))

promotional_items = 5
voucher_amount = 1500

if no_of_items >= promotional_items:
                   print("\nCongrulations , you are qualified for the promotional offer")
                   print("As a special offer you will receive a voucher value of amount Rs.",voucher_amount)
else:
    print("\nSorry , you need to add atleast 5 items into your shopping cart to elegible for promotional offer ")
    print("Consider adding more items in your shopping cart")
