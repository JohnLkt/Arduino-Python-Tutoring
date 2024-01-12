# Functions and Arguments

## ----------------------------------------------------- Functions -----------------------------------------------------

# Functions in Python are blocks of reusable code that perform a specific task. They are defined using the 'def' keyword.

# Basic function without parameters
def greet():
    print("Hello, welcome!")

# Calling the function
greet()

# Function with parameters
def greet_user(name):
    print(f"Hello, {name}!")

# Calling the function with an argument
greet_user("Alice")

# Functions can have multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is: {result}")

# Calling the function with arguments
add_numbers(3, 5)
add_numbers(10, -2)

# Functions can return values using the 'return' keyword
def multiply_numbers(x, y):
    product = x * y
    return product

# Calling the function and storing the result
result = multiply_numbers(4, 7)
print(f"The product is: {result}")

## ----------------------------------------------------- Functions -----------------------------------------------------

## ----------------------------------------------------- Arguments -----------------------------------------------------

# Arguments in functions are the values passed to the function when it is called. They match the parameters defined in the function.

# Positional arguments (order matters)
def full_name(first_name, last_name):
    print(f"Full name: {first_name} {last_name}")

full_name("John", "Doe")
full_name("Doe", "John")

# Keyword arguments (order doesn't matter)
full_name(last_name="Smith", first_name="Alice")

# Default values for parameters
def greet_with_message(name, message="Welcome to the program!"):
    print(f"Hello, {name}! {message}")

greet_with_message("Bob")
greet_with_message("Charlie", "Have a great day!")

# Variable number of arguments (*args and **kwargs)
def add_all(*args):
    total = sum(args)
    print(f"The sum is: {total}")
add_all(1, 2, 3)
add_all(4, 5, 6, 7)

## ----------------------------------------------------- Arguments -----------------------------------------------------
