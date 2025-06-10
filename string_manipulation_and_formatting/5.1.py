# 1. Write a function that capitalizes the first letter of each word in a string.

def capitalize_words(sentence):
    """
    Capitalize the first letter of each word in the given string.

    Args:
        sentence (str): The input string.

    Returns:
        str: A string with each word capitalized.
    """
    # Split the sentence into words, capitalize each, and rejoin them
    return ' '.join(word.capitalize() for word in sentence.split())

text = "hello world from nucleusTeq"
result = capitalize_words(text)
print(result)  
