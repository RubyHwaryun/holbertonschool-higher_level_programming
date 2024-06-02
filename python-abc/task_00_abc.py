#!/usr/bin/python3

from abc import ABC, abstractmethod

# Define the abstract class Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Define the subclass Dog
class Dog(Animal):
    def sound(self):
        return "Bark"

# Define the subclass Cat
class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage
dog = Dog()
print(dog.sound())  # Output: Bark

cat = Cat()
print(cat.sound())  # Output: Meow

