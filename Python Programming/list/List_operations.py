x = [1,2,3,4,5,6]
y = ['a','f','g','h','y','u','u','u']

z = [20,30,40,50,60,'apple']
z1 = []


print('x list values are \t:',x)
print('y list values are \t:',y)
print('z list values are \t:',z)


print("Append function in list:\n")
print('Empty List',z1)
x.append(y)
print('Appending y value to x ',x)

x.insert(4,100)

print('insert data to x based on index value [4]',x)

print("y's data",x[-1])


print(len(x))
print('Delete an item based on index\n')

del x[-1]

print(' del x[-1] This will delete item in position x[-1] or last position and print output',x)


x.reverse()

print('Reversed data of x',x)

x[::-1]

print("Original data Z:",z)
print("Reverse data of Z:",z[::-1])

print("Clear all the list data in x,y,z",x.clear(),y.clear(),z.clear())

print(x)



