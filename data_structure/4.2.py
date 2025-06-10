# 2. Write a function to merge two dictionaries.

def merge_dicts(dict1, dict2):
    merged = {}
    for key in dict1:
        merged[key] = dict1[key]
    for key in dict2:
        merged[key] = dict2[key]
    return merged

dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}

result = merge_dicts(dict_a, dict_b)
print(result)  
