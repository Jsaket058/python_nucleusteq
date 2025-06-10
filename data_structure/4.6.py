# 6. Implement a stack using list with push, pop, and peek operations.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Nothing to peek.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Stack (top -> bottom): {self.items[::-1]}"

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Top item:", stack.peek())      
print("Popped item:", stack.pop())    
print("Top item now:", stack.peek())  

print("Is empty?", stack.is_empty())  
print("Size:", stack.size())          

print(stack)
