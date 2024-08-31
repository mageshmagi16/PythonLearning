from math import pi


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)


def print_area(shape):
    print(f"The area is: {shape.area()}")

# Create instances
rect = Rectangle(5, 3)
circ = Circle(4)


print_area(rect)  
print_area(circ) 
