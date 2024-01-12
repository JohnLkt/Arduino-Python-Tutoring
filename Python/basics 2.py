# Basic Python:
# If Statements
# Lists
# Loops
# dictionaries
# in operator

## ----------------------------------------------------- If Statements -----------------------------------------------------

# If statements are used to make decisions in code. The basic syntax is as follows:

age = 18

if age >= 18:
    if age < 21:
        print("not over 21")
    else:
        print("You are eligible to vote.")
elif age != 10:
    print("not 10")
else:
    print("You are not eligible to vote yet.")

# In this example, if the variable 'age' is greater than or equal to 18, it will print the first message. 
# Otherwise, it will print the second message.

## ----------------------------------------------------- If Statements -----------------------------------------------------

## ----------------------------------------------------- Lists -----------------------------------------------------

# Lists in Python are used to store multiple items in a single variable. 
# They are ordered, mutable, and can contain elements of different data types.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# Accessing elements in a list
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Modifying elements in a list
fruits[1] = "orange"
print("Modified list:", fruits)

# Adding elements to a list
fruits.append("grape")
fruits.insert(1, "durian")
print("After adding grape:", fruits)

# Removing elements from a list
fruits.remove("apple")
fruits.pop()
print("After removing apple:", fruits)

print(fruits)
temp = fruits[0]
fruits[0] = fruits[1]
fruits[1] = temp

print(fruits)

## ----------------------------------------------------- Lists -----------------------------------------------------

## ----------------------------------------------------- Loops -----------------------------------------------------

# Loops are used to iterate over a sequence (e.g., list, string) and execute a block of code repeatedly.

# For loop example
numbers = [6, 2, 4 ,1, 2, 6]

for i in range(0, 10):
    numbers.append(input("input number: "))
    # print(i)

for x in numbers:
    print(x)

# While loop example
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

## ----------------------------------------------------- Loops -----------------------------------------------------
## ----------------------------------------------------- Dictionaries -----------------------------------------------------

# Dictionaries in Python are used to store key-value pairs. They are unordered, mutable, and can contain elements of different data types.

# Creating a dictionary
person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print("Person dictionary:", person)

# Accessing values using keys
print("Name:", person["name"])
print("Age:", person["age"])

# Modifying values
person["age"] = 26
print("Modified age:", person["age"])

# Adding new key-value pairs
person["occupation"] = "Engineer"
print("After adding occupation:", person)
print("Occupation: ", person["occupation"])

# Removing a key-value pair
del person["city"]
print("After removing city:", person)

# example usage of dictionaries

kalimat = "ajdsfaeuhfpoawdjf;klajnwepfawpofehja"

kumpulanHuruf = {}

for huruf in kalimat:
    if huruf in kumpulanHuruf:
        kumpulanHuruf[huruf] += 1
    else:
        kumpulanHuruf[huruf] = 1

print(kumpulanHuruf)

## ----------------------------------------------------- Dictionaries -----------------------------------------------------

## ----------------------------------------------------- Examples of the 'in' Operator -----------------------------------------------------
# The 'in' operator is used to check if a value exists in a sequence (e.g., string, list, dictionary).

# Example with a list
fruits = ["apple", "banana", "cherry"]
print("Is 'banana' in fruits?", "banana" in fruits)
print("Is 'grape' in fruits?", "grape" in fruits)

# Example with a string
message = "Hello, World!"
print("Is 'Hello' in message?", "Hello" in message)
print("Is 'Python' in message?", "Python" in message)

# Example with a dictionary (checking keys)
print("Is 'age' a key in person dictionary?", "age" in person)
print("Is 'gender' a key in person dictionary?", "gender" in person)

## ----------------------------------------------------- Examples of the 'in' Operator -----------------------------------------------------