

x = [6,4,8,9]

y = ["APples",'Mangoes',"Grapes"]

#print(x[0])

#print(y[2:3])


z = x + y

#print(z)

z1 = y + z


#print(z1)

item = input("Enter an item name")

for item in z1:
    if item in z1:
        print("Item Found")
        break
    else:
        print("Item not Found")
print(item)
    



