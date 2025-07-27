print ("What other data types are there in Python ?")



# String Data Type
x = "Sathya Narayana"
y = 'Loves'
z = 'Ansible'

print(type(x))
print(type(y))
print(type(z))


# We can store data, but if we to store multiple data typea nd need to organiuze data for this we have to use Data Structures.

# List Data Structure: type of data structure supported in python to organize and access data in order

example = [1,2,3,4,5]

print(type(example))

example2 = ["Sathya", "Ansible", "Python", 1, 2, 3]
print(type(example2))

# Tuple Data Structure: Similar to List, but it is immutable (cannot be changed after creation)

example_tuple = (1, 2, 3, 4, 5)
print(type(example_tuple))      

example_tuple2 = ("Sathya", "Ansible", "Python", 1, 2, 3)
print(type(example_tuple2))                 

# Dictionary Data Structure: Key-value pairs to store data in a structured way
example_dict = {
    "name": "Sathya",
    "age": 30,
    "skills": ["Ansible", "Python"]
}       

print(type(example_dict))  

example_dict2 = {
    "name": "Sathya", 
    "course": "Ansible",
    "language": "Python",
    "mentoring": True,
    'learning': True
}

print(dict(example_dict2))  # This will convert the dictionary to a dict object
print(type(example_dict2))  # This will show the type of the dictionary 

# Set Data Structure: Unordered collection of unique elements
example_set = {1, 2, 3, 4, 5}               
print(type(example_set))

example_set2 = {"Sathya", "Ansible", "Python"}
print(type(example_set2))  
print(set(example_set2))  # This will remove duplicates and show unique elements  


example_set3 = {1, 2, 3, 4, 5, "Sathya", "Ansible", "Python",1,2,3,4,5, "Sathya", "Ansible", "Python",2,3,4,5, "Sathya", "Ansible", "Python"}
print(type(example_set3))
print(set(example_set3))  # This will remove duplicates and show unique elements
