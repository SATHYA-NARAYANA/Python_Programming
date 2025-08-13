# in herw we are tring to access publivc and Private member of nsr_bankfrom outside class

class bank():
    def __init(self,account_no,balance = 0):
        self.__account_no = account_no
        self.__balance = balance
        self.b = 'This is a public variable'

    def __get_account_number(self):#private function
        return self.__account_no
    def __get_balance(self):# private function
        return self.__balance
    def get_account_details(self):
        print('Account number',self.__get_account_number())
        print('Balance',self.__get_balance())

class nsr(bank):
    print('This is testing sstage of access private member from another class')


obj_nsr = nsr("8989898765", 35000)
obj_nsr.get_account_details()

# trying to call privete member outside class
#obj_nsr.__get_account_number()
#obj_nsr.__get_balance()
