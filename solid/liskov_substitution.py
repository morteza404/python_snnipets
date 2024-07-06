from typing import Protocol

# before

"""
اگر کلاس ب  فرزند کلاس آ باشد باید بتوان اشیای کلاس ب را با اشیای کلاس آ جایگزین کنیم
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side


def print_area(rectangle):
    area = rectangle.get_area()
    print(f"The area is: {area}")


rectangle = Rectangle(4, 5)
square = Square(5)

print_area(rectangle)  # Output: The area is: 20
print_area(square)  # Output: The area is: 25


# after

class Shape(Protocol):
    def get_area(self):
        pass


class Rectangle2(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square2(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2


def print_area(shape):
    area = shape.get_area()
    print(f"The area is: {area}")


rectangle = Rectangle2(4, 5)
square = Square2(5)

print_area(rectangle)  # Output: The area is: 20
print_area(square)  # Output: The area is: 25
