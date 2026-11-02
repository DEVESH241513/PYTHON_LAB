
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Vector(Shape):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.magnitude() < other.magnitude()

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.area() < other.area()


# Main program
print("=== Vector Operations ===")

v1 = Vector(2, 3)
v2 = Vector(4, 5)

print("Vector 1:", v1)
print("Vector 2:", v2)

print("Addition:", v1 + v2)
print("Are vectors equal?", v1 == v2)
print("Is Vector 1 smaller?", v1 < v2)


print("\n=== Circle Operations ===")

c1 = Circle(3)
c2 = Circle(5)

print("Circle 1:", c1)
print("Circle 2:", c2)

print("Area of Circle 1:", round(c1.area(), 2))
print("Area of Circle 2:", round(c2.area(), 2))

print("Combined Circle:", c1 + c2)
print("Are circles equal?", c1 == c2)
print("Is Circle 1 smaller?", c1 < c2)
