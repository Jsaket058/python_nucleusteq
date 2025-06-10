# 7. Implement method overriding in a subclass.

class Vehicle:
    """
    Base class for all vehicles.
    """

    def start(self):
        print("Starting the vehicle...")

class Car(Vehicle):
    """
    Car class that overrides the start method.
    """

    def start(self):
        print("Starting the car engine with key or push button...")

v = Vehicle()
v.start()  

c = Car()
c.start()  