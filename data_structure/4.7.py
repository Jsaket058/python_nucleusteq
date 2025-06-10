# 7. Create a queue using collections.deque and implement enqueue and dequeue.

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            print("Queue is empty. Cannot dequeue.")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty. Nothing to peek.")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"Queue (front -> rear): {list(self.items)}"

q = Queue()

q.enqueue('A')
q.enqueue('B')
q.enqueue('C')

print("Front item:", q.peek())        
print("Dequeued item:", q.dequeue())  
print("Front now:", q.peek())         
print("Is empty?", q.is_empty())      
print("Size:", q.size())              

print(q)