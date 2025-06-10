def greet_user() -> None:
    """
    Accepts user's name and age, and prints a personalized greeting.
    """
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    print(f"Hello, {name}! You are {age} years old.")

greet_user()
