# 7. Write a generator expression to filter out palindromes from a list of words.

words = ["Madam", "Racecar", "Hello", "World", "Level", "Python"]

palindromes = (word for word in words if word.lower() == word.lower()[::-1])

for p in palindromes:
    print(p)
