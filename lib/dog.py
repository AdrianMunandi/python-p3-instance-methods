#!/usr/bin/env python3
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting.")

# Creating an instance of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")

# Calling the methods
my_dog.bark()
my_dog.sit()
