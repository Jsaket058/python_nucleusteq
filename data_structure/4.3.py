# 3. Develop a function that removes duplicate elements from a list.

def remove_duplicates(list1):
    unique = []
    seen = set()
    for item in list1:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique

numbers = [1, 2, 2, 3, 4, 1, 5, 3]
result = remove_duplicates(numbers)
print(result)
