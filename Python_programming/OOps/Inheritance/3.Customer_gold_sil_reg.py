class customer():

    def __init__ (self,cid,cname,cpur_amt):
        self.id = cid
        self.name = cname
        self.pur_amt = cpur_amt

    def display_customer(self):
        print(f"\nYour Customer ID:{self.id}\nYour name :{self.name}\nYour Purchase Amount :{self.pur_amt}")

class prefered_customer(customer):

    def gold_customer(self):
        discount = self.pur_amt * 15/100
        final_amt = self.pur_amt - discount
        #obj_preferred_customer.display_customer()
        super().display_customer()
        print(f"Discount:{discount}\nFinal Amount : {final_amt} \n\n\n \t\t\t\t\t  Thank you for shopping with Us !!!")
        print("You are a valued gold customer and you have received \nA 15% discount based on your purchase!!!!")

    def silver_customer(self):
        discount = self.pur_amt * 10/100
        final_amt = self.pur_amt - discount
        #obj_preferred_customer.display_customer()
        super().display_customer()
        print(f"Discount:{discount}\n Final Amount : {final_amt} \n  Thank you for shopping with Us !!!")
        print("You are a valued silver customer and you have received a 10% discount based on your purchase!!!!")

    def regular_customer(self):
        discount = self.pur_amt * 5/100
        final_amt = self.pur_amt - discount
        #obj_preferred_customer.display_customer()
        super().display_customer()
        print(f"Discount:{discount}\n Final Amount : {final_amt} \n  Thank you for shopping with Us !!!")
        print("You are a valued regular customer and you have received a 5% discount \n Based on your purchase amount!!!!")

#___________________________ Above code is a blue print for customer_____________________________________

cid = input("Enter Customer ID:")
cname = input("Enter Customer name:")
purchase_amount = int(input("Enter customer total purchase amount:"))

obj_prefered_customer = prefered_customer(cid,cname,purchase_amount)

# Gold Cust

if purchase_amount >= 10000:
    obj_prefered_customer.gold_customer()

# Silver Cust

elif purchase_amount >= 5000 and purchase_amount < 10000:
    obj_prefered_customer.silver_customer()
    # Normal Customer
else:
    obj_prefered_customer.regular_customer()
    
    















     
        
