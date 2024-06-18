from faker import Faker
from dataclasses import dataclass

fake = Faker("en_US")
# for _ in range(10):
#     print(fake.name())

# @dataclass
# class MyClass:
#     name: str
#     address: str

# o=MyClass(fake.name(), fake.address())
# print(o)


class Person:
    def __init__(self):
        self.name = fake.name()
        self.address = fake.address()
        self.city = fake.city()
        self.date = fake.date()
        self.country = fake.country()


p = Person()
print(p.country)
