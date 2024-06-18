class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be an integer")
        if value < 0:
            raise ValueError("age must be a positive integer")
        self._age = value

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})"


p = Person("John", 30)
print(p)
print(vars(p))
print(p.__dict__)