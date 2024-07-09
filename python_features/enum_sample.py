from enum import Enum, auto


class Color(Enum):
    RED = 1
    GREEN = auto()
    BLUE = 3


print(f"color is: {Color.RED}")
print(f"color is: {Color.GREEN}")
print(f"color is: {Color.BLUE}")
