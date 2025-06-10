# 8. Create a class with private attributes and getter/setter methods.

class Person:
    """
    Class with private attributes and getter/setter methods.
    """

    def __init__(self, name, age):
        self.__name = name    
        self.__age = age      

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            print("Invalid name")

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age > 0:
            self.__age = new_age
        else:
            print("Invalid age")

person = Person("Saket", 22)

print(person.get_name())  
print(person.get_age())   

person.set_name("Vaseem")
person.set_age(23)

print(person.get_name())  
print(person.get_age())   

person.set_name("")       # Invalid name
person.set_age(-5)        # Invalid age

