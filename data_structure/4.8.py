# 8. Write a function to find the intersection of two lists.

def list_intersection(list1, list2):
    ans = list()
    for item in list1:
        if item in list2:
            ans.append(item)
    # return [item for item in list1 if item in list2]
    return ans
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]

result = list_intersection(a, b)
print(result)