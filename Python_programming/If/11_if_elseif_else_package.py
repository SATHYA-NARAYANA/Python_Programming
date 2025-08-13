# A Shipping Company wanted to deliver packages to domestic and International customers
# Problem statement: Need to calculate Charges to delivery packages

destination = input ("Enter your destination package location \n")

domestic_rate = 100
international_rate_per_kg = 30

if destination == "Hyderabad":
    shipping_cost = domestic_rate

elif destination == "Chennai":
    shipping_cost = domestic_rate

else:
    weight = float(input("Enter the weight for package in Kg:"))
    shipping_cost = domestic_rate + (weight * international_rate_per_kg)

print("The shipping Cost", destination, "is: Rs.",shipping_cost)
                   
