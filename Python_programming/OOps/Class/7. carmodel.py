class car:

    def __init__(self,model,year,price):
        self.m = model
        self.y = year
        self.p = price

obj_car0 = car("Maruti",2015,60000)
print(f"\n car name:{obj_car0.m} \n Model : {obj_car0.y} \n Price : {obj_car0.p}")


obj_car1 = car("SKODA",2018,750000)
print(f"\n car name:{obj_car1.m} \n Model : {obj_car1.y} \n Price : {obj_car1.p}")
