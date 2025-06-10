# 4. Implement a custom iterable class for iterating characters of a string.

class CharIterator:
    """
    Custom iterable class to iterate over characters in a string.
    """

    def __init__(self, text):
        self.text = text      # The input string
        self.index = 0        # Current index in the string

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        char = self.text[self.index]
        self.index += 1
        return char

word = CharIterator("NucleusTeq!!")

for ch in word:
    print(ch)
