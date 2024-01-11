# Basic Python:
# Object-Oriented Programming (OOP) in Python

## ----------------------------------------------------- Classes and Objects -----------------------------------------------------

# Classes in Python are used to create objects. An object is an instance of a class, and it can have attributes (characteristics) and methods (functions).

# Defining a simple class
class Dog:
    # Class attribute
    species = "Canis familiaris"

    # Constructor method (called when an object is created)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says woof!")

# Creating objects (instances of the Dog class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and calling methods
print(f"{dog1.name} is {dog1.age} years old.")
dog2.bark()

# another example

import datetime

class Person:

    def __init__(self, name, age, address, birthdate):
        self.name_ = name
        self.age = age
        self.address = address
        self.birth = birthdate
    
    def getName(self):
        return self.name_
    
    def bikinTua(self, ageTambah):
        self.age = self.age + ageTambah

    def getage(self):
        return datetime.datetime.now() - self.birth

person1birth = datetime.datetime(2004, 3, 12)
person1 = Person("test", 20, "test", person1birth)

print(person1.getage())

## ----------------------------------------------------- Classes and Objects -----------------------------------------------------

## ----------------------------------------------------- Inheritance -----------------------------------------------------

# Inheritance allows a class to inherit attributes and methods from another class. The new class is called a subclass, and the existing class is a superclass.

# Creating a subclass 'GoldenRetriever' that inherits from the 'Dog' class
class GoldenRetriever(Dog):
    # Additional attribute specific to Golden Retrievers
    is_good_with_kids = True

    # Overriding the bark method of the superclass
    def bark(self):
        print(f"{self.name} (Golden Retriever) says cheerful bark!")

# Creating an instance of the subclass
golden_retriever = GoldenRetriever("Charlie", 2)

# Accessing attributes and calling methods from both the superclass and subclass
print(f"{golden_retriever.name} is {golden_retriever.age} years old.")
print(f"Is {golden_retriever.name} good with kids? {golden_retriever.is_good_with_kids}")
golden_retriever.bark()

## ----------------------------------------------------- Inheritance -----------------------------------------------------

## ----------------------------------------------------- Encapsulation -----------------------------------------------------

# Encapsulation involves restricting access to certain attributes and methods to prevent unintended modifications.

# Modifying the Dog class to include private attribute and method
class DogWithEncapsulation:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self._name = name  # Single underscore indicates a protected attribute
        self._age = age

    def _private_method(self):
        print("This is a private method.")

    def public_method(self):
        print(f"{self._name} is {self._age} years old.")

# Creating an object
dog_encapsulated = DogWithEncapsulation("Rocky", 4)

# Accessing a protected attribute and calling a public method
print(f"{dog_encapsulated._name} is a {dog_encapsulated.species}.")
dog_encapsulated.public_method()

# Accessing a private method (not recommended, just for illustration)
dog_encapsulated._private_method()

## ----------------------------------------------------- Encapsulation -----------------------------------------------------

## ----------------------------------------------------- Polymorphism -----------------------------------------------------

# Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Creating a function that takes any Dog object as a parameter
def introduce_dog(dog):
    print(f"Meet {dog.name}, a {dog.species}.")

# Using the function with objects of different classes
introduce_dog(dog1)
introduce_dog(golden_retriever)

## ----------------------------------------------------- Polymorphism -----------------------------------------------------
