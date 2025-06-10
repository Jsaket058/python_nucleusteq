# 10. Implement a function to check if a list is a palindrome.

def is_palindrome(lst):
    # Compare the list with its reversed version
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))  # True
print(is_palindrome(['a', 'b', 'a']))  # True
print(is_palindrome([1, 2, 3]))        # False
