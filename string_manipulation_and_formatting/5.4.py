# 4. Develop a function that counts words, characters, and lines in a string.

def count_text_stats(text):
    """
    Count the number of words, characters, and lines in the input string.

    Args:
        text (str): The input string.

    Returns:
        dict: A dictionary with counts of 'words', 'characters', and 'lines'.
    """
    num_characters = len(text)

    words = text.split()
    num_words = len(words)

    lines = text.splitlines()
    num_lines = len(lines)

    return {
        'words': num_words,
        'characters': num_characters,
        'lines': num_lines
    }

sample_text = """Hello world!
Blag Blah ok okay.
It has many lines to work with."""

stats = count_text_stats(sample_text)
print(stats)
