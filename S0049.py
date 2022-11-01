# now we use a constructor to more elegantly define the car and its properties

class Vehicle:  # this starts the definition of a class

    def __init__(self, wheels, max_speed):
        # in python the constructor of a class is always called __init__
        # a constructor creates an object of a class
        self.wheels = wheels  # wheels is called a property. A property is a variable that belongs to a class.
        self.max_speed = max_speed  # another property

    def drive(self):  # This is a method. A method is a function that belongs to a class.
        print("WROOOOOOOOM!")


car1 = Vehicle(4, 160)  # car1 is now defined as an object of type Vehicle. Also its properties are already defined.
car1.drive()  # the method drive of the class Vehicle is called on the object car1

print(1, type(car1))
print(2, car1)
print(3, "wheels", car1.wheels)
print(4, "maximum speed", car1.max_speed)