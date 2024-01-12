# Basic Python:
# Variables & Types
# String Methods
# Operators
# Typecasting

## ----------------------------------------------------- variables & types -----------------------------------------------------

# In Python, variables are declared using | name = value (optional) | like so:

x = 1

# Variables in python are infered, and not statically typed. This means that it's data type can change dynamically:
print('old x value:')
print(x)

x = 'Hello World'

print('new x value:')
print(x)

# The common data basic types in python are int (integer), float (floating point number), String, and Booleans

## ----------------------------------------------------- variables & types -----------------------------------------------------
# ----------------------------------------------------- String Methods -----------------------------------------------------
# String Methods are ways to modify, insert, or check data within strings.
# Basic examples include:

# string concatination
firstString = "Hello"
secondString = "World"

concatString = firstString + secondString
print(concatString)

# or

print(firstString + ' ' + secondString)

# string formatting & input

print("Type a search term: ")
# input() is used to get user input from the console
word = input()
otherWord = input()
searchURL = f'https://www.merriam-webster.com/dictionary/{word}/{otherWord}'
print("Output String: " + searchURL)

# ----------------------------------------------------- String Methods -----------------------------------------------------
## ----------------------------------------------------- Operators -----------------------------------------------------
# are the basic logical steps for code like arithmatic or comparisons

a = 1
b = 5

c = a + b
print(f"C's value is: {c}")

d = c/2
print(f"D's value is: {d}")

print(f"is C smaller than D: {c < d}")

# notice that we use string formatting because c and d are not strings, therefore cannot be concatinated with +
## ----------------------------------------------------- Operators -----------------------------------------------------
## ----------------------------------------------------- Typecasting -----------------------------------------------------
# cast int to string

print("test casting" + str(c))

# common usecase is to make sure user input is the correct type

string = input()
print(type(string))
integer = int(input())
print(type(integer))