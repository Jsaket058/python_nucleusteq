# 1. Implement a function to reverse a list without using built-in reverse().

def reverse_list(list1):
    reversed_list1 = []
    for item in list1:
        reversed_list1 = [item] + reversed_list1  # Prepend current item
    return reversed_list1

my_list = [1, 2, 3, 4, 5]
print(reverse_list(my_list))
