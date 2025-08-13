# Perform all list Operations
# 1. Take input from user
# 2. Store it in a variable
# 3. Perform action based on condition

#main.py
print('\t\t*********\tWelcome\t\t*********')

def List_operations():
    
    op1 = int(input("Enter your choice to perform list operations or (Type Exit)"))

    for op in op1:
        if op1 == "Exit":
            break

    if op1 == 1:
        list_append()

    #append data to list
    def list_append():
        pass
    # Insert data in a position
    def insert_data():
        pass

    # Clear all data in list
    def clear_list():
        pass

    # delete an item from list
    def del_an_item():
        pass

    #


List_operation = List_operations()

list_operation()
    
