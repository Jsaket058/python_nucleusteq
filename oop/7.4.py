# 4. Implement inheritance between a base class Animal and subclasses Dog and Cat.

class Animal:
    """
    Base class for animals.
    """

    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"This is {self.name} the {self.__class__.__name__}"
    

class Dog(Animal):
    def sound(self):
        return "Woof!"


class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog)               
print(f"{dog.name} says: {dog.sound()}")   

print(cat)               
print(f"{cat.name} says: {cat.sound()}")   
