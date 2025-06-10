# 10. Implement multiple inheritance and demonstrate method resolution order.

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

# Create instance of C
obj = C()
obj.greet()

# Show method resolution order
print(C.mro())
