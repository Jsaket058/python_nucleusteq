# 3. Write a function that replaces all vowels in a string with '*' symbol.

def replace_vowels(text):
    """
    Replace all vowels in the input string with '*' symbol.

    Args:
        text (str): The input string.

    Returns:
        str: String with all vowels replaced by '*'.
    """
    vowels = "aeiouAEIOU"  
    result_chars = []      
    for char in text:
        if char in vowels:
           result_chars.append('*')
        else:
            result_chars.append(char)

    result = ''.join(result_chars)
    return result


input_str = "Hello World"
output_str = replace_vowels(input_str)
print(output_str)  
