# Demonstrating access to public and private members in an inheritance scenario

class bank:
    def __init__(self, account_no, balance=0):
        self.__account_no = account_no          # private attribute
        self.__balance = balance                # private attribute
        self.b = 'This is a public variable'    # public attribute

    def __get_account_number(self):  # private method
        return self.__account_no

    def __get_balance(self):         # private method
        return self.__balance

    def get_account_details(self):   # public method
        print('Account number:', self.__get_account_number())
        print('Balance:', self.__get_balance())

class nsr(bank):
    def __init__(self, account_no, balance):
        super().__init__(account_no, balance)
        print('This is testing stage of accessing private members from another class')

# Create object of child class
obj_nsr = nsr("8989898765", 35000)

# Call public method that accesses private members internally
obj_nsr.get_account_details()


