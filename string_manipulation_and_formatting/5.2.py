# 2. Create a program that finds all substrings of a given string.

def find_all_substrings(s):
    """
    Generate all possible substrings of the input string.

    Args:
        s (str): The input string.

    Returns:
        list: A list containing all substrings.
    """
    substrings = []
    length = len(s)

    for start in range(length):
        for end in range(start + 1, length + 1):
            substr = s[start:end]
            substrings.append(substr)
    return substrings

input_str = "abc"
all_substrings = find_all_substrings(input_str)
print(all_substrings)
