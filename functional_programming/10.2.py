# 2. Use `map()` to convert all strings in a list to uppercase.

# List of lowercase strings
words = ["nucleusteq", "indore", "python", "saket","java"]

# Use map() with lambda to convert each string to uppercase
uppercase_words = list(map(lambda s: s.upper(), words))

# Output the result
print(uppercase_words)
