# 9. Develop a function that finds the longest palindromic substring.

def longest_palindromic_substring(s):
    """
    Find and return the longest palindromic substring in the given string.

    Args:
        s (str): The input string.

    Returns:
        str: The longest palindromic substring.
    """
    if not s or len(s) == 1:
        return s

    start = 0
    max_length = 1

    # Helper function to expand around the center
    def expand_around_center(left, right):
        nonlocal start, max_length
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
                start = left
            left -= 1
            right += 1

    for i in range(len(s)):
        # Odd length palindromes (centered at i)
        expand_around_center(i, i)
        # Even length palindromes (centered between i and i+1)
        expand_around_center(i, i + 1)

    return s[start:start + max_length]

text = "babad"
result = longest_palindromic_substring(text)
print(result)  # Output: "bab" or "aba" (both are valid)

text2 = "cbbd"
print(longest_palindromic_substring(text2))  # Output: "bb"
