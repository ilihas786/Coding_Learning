'''In Python, abstraction is typically implemented using abstract base classes (ABCs) from the abc module. Here is an example involving an abstract class for shapes:'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# Using abstraction
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area()}")       # Calculate and print area
    print(f"Perimeter: {shape.perimeter()}") # Calculate and print perimeter
