# 3. Use `filter()` to remove empty strings from a list.

# List with some empty and non-empty strings
strings = ["sagar", "", "rohit", "ravi", "", ""]

# Use filter() with lambda to remove empty strings
non_empty_strings = list(filter(lambda s: s != "", strings))

# Output the result
print(non_empty_strings)
