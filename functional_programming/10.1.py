# 1. Write a lambda function to compute the square of a number and use it in a list comprehension.

# Lambda function to compute the square of a number
square = lambda x: x ** 2

# List of input numbers
numbers = [1, 2, 3, 4, 5]

# Using list comprehension with the lambda function
squares = [square(num) for num in numbers]

# Output the result
print(squares)
