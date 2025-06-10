# 5. Write a program to sort a list of tuples based on the second element.

def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

data = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_data = sort_by_second_element(data)
print(sorted_data)
