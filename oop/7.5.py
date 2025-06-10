# 5. Write a class with a class variable shared among all instances.

class Counter:
    """
    A class with a class variable to count how many instances were created.
    """

    count = 0  # Class variable (shared across all instances)

    def __init__(self):
        Counter.count += 1

    def get_instance_number(self):
        return Counter.count

a = Counter()
b = Counter()
c = Counter()

print(f"Total instances created: {Counter.count}")
print(f"a's count: {a.get_instance_number()}")
print(f"b's count: {b.get_instance_number()}")
