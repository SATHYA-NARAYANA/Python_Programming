# poly morphism : many form

# use same function name with different functionality

# example len() function , with the same function name can perform different actions
# like find data type of string,list, tuple, set, dictionary

#There ar 2 types of polymorphism :

#    method over load
 #   method overriding


class email_notification():
    def send(self):
        print('Sending email to customer.....')

class sms_notification():
    def send(self):
        print('Sending SMS to customer.....')

class whatsapp_notification():
    def send(self):
        print('Sending whatsapp to customer.....')

email = email_notification()
sms = sms_notification()
whatsapp = whatsapp_notification()

# sms.send()
# email.send()

for msg_type in (email,sms,whatsapp):
    msg_type.send()

# we use forloop as we already know how many number of times a loop will run.
# here for loop only works with polymorphism
    
