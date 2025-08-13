class room():
    length = 0
    width = 0
# method for calculate
    def area(self):
        print ("Area =",self.length * self.width, "sq ft")

# create obj room
study = room()
classroom = room()
library = room()

# assign value

study.length = 30
study.width = 40

print("\nStudy Room:")
study.area()

classroom.length = 50
classroom.width = 60

print("\nClass Room:")
classroom.area()

library.length = 100
library.width = 50

print("\nLibrary room:")
library.area()


