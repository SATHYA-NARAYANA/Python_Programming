
# super() is a build in function that allows us to call method of super class in a sub-calss(Child class)
# in child class its is useful if we particullary invoke a method of parent class, from parent class within the child class


class customer():

    def __init__ (self,cid,cname,cpur_amt):
        self.id = cid
        self.name = cname
        self.pur_amt = cpur_amt

    def customer_details(self):
        print(f"\nCustomer ID:{self.id}\nCustomer name : {self.name} \n Purchase Amount : {self.pur_amt}")

class discount(customer):

    def apply_dis(self):
        discount = self.pur_amt * 10/100
        final_amt = self.pur_amt - discount
        #obj_discount.customer_details()
        super().customer_details
        print(f"\nDiscount: {discount}\nFinal Amount: {final_amt}")

cid = input("Enter Customer Id:")
cname = input("Enter Customer name:")
purchase_amt = int(input("Enter customer total purchase amount:"))

obj_discount = discount(cid,cname,purchase_amt)
obj_discount.apply_dis()



