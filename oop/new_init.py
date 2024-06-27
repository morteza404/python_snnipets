class Person:
    def __new__(cls, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        return super().__new__(cls)
    def __init__(self, name):
        self.name = name

# p1 = Person(123)
# print(p1.name)
p2 = Person("mshahbazi")
print(p2.name)