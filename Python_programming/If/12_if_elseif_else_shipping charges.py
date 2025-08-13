I = Indian_Cities = ["Hyderabad","Chennai","Bangalore","Delhi"]

E = Europe_Countries = ['England','Ireland','Italy', "Paris"]

A = Asian_Countries = ["Malaysia", 'Singapore', 'Dubai']

print("\nOur services in India:",Indian_Cities)
print("\nOur services in Europe Countries:",Europe_Countries)
print("\nOur services in Asian Countries:",Asian_Countries)

destination = input("Enter the destination location:\n").title()
# 100 flast rate for domestic shippings
Domestic_dest_amt = 100
# 20 addiditional charges per kg for Asian Countries
Asian_dest_rate_per_kg = 20

Europe_dest_rate_per_kg = 30

if destination in I:
    shipping_cost = Domestic_dest_amt
    print("The shipping cost to",destination, "is: RS",Domestic_dest_amt)

elif destination in A:
    weight = float(input("Enter the weight of the package in kg:"))
    shipping_cost = Domestic_dest_amt + (weight * Asian_dest_rate_per_kg)
    print(f("The shipping cost to,destination is: RS",shipping_cost))

elif destination in E:
    weight = float(input("Enter the weight of the package in kg:"))
    shipping_cost = Domestic_dest_amt + (weight * Europe_dest_rate_per_kg)
    print("The shipping cost to",destination, "is: RS",shipping_cost)

else:
    print("Sorry",destination, "not available at the movement")
