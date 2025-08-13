class Retail_customer():
    def generate_invoice(self,amount):
        gst = amount * 18/100
        total = amount + gst
        print("Retil Invoice:")
        print(f"Purchase amount: Rs.{amount:.2f}")
        print(f"GST (18%): Rs. {gst:.2f}")
        print(f"Total: Rs {total:.2f}")
        print("Includes GST and Standard format.")

class wholesale_customer():
    def generate_invoice(self,amount):
        discount = amount * 10/100
        discounted_amount = amount - discount
        print("\nWholesale Invoice:")
        print(f"Purchase amount: Rs.{amount:.2f}")
        print(f"Bulk discount (10%) : Rs - {discount:.2f}")
        print(f"Total: Rs {discounted_amount:.2f}")
        print("GST excepted for wholesale purchases")


# polymorpic function

def print_receipt(cust_type,amount):
    cust_type.generate_invoice(amount)

obj_retails = Retail_customer()
obj_wholesale = wholesale_customer()

print_receipt(obj_retails, 5000)
print_receipt(obj_wholesale, 25000)
            
