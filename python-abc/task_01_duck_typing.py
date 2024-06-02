#!/usr/bin/python3

from abc import ABC, abstractmethod
from math import pi

# Define the abstract class Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Define the concrete class Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

# Define the concrete class Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Define the shape_info function
def shape_info(shape):
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())

# Instantiate a Circle and a Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Test the shape_info function
print("Circle:")
shape_info(circle)
print("\nRectangle:")
shape_info(rectangle)

