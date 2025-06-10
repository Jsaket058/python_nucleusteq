# 9. Write a script that reads a file and counts the frequency of each character.

from collections import Counter

def count_char_frequency(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    content = content.replace(" ", "").replace("\n", "")

    frequency = Counter(content)
    # print(frequency)
    for char, count in frequency.items():
        print(f"'{char}': {count}")


count_char_frequency('file_handling/yo.txt')

