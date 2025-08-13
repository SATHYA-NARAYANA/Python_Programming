class car():
    nsr = "\nWelcome to NSR Car showroom"

    def __init__(self,model,year):
        self.m = model
        self.y = year
    def display(self):
        print(self.nsr)
        print(f"My car name is:{self.m} \nYear of model is:{self.y}")
        print("-------------------")

obj1_car = car("BMW", 2022)
obj1_car.display()


obj2_car = car("Maruti Suzuki", 2024)
obj2_car.display()

