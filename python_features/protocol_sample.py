from typing import Protocol


class AreaProtocol(Protocol):
    def area(self) -> int: ...


class Circle(AreaProtocol):
    def __init__(self, radius: int):
        self.radius = radius

    def area(self) -> int:
        return self.radius**2 * 3.14


class Square(AreaProtocol):
    def __init__(self, length: int):
        self.length = length

    def area(self) -> int:
        return self.length**2


if __name__ == "__main__":
    circle = Circle(5)
    print(circle.area())
    square = Square(5)
    print(square.area())
