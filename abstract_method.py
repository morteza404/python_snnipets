from abc import ABC, abstractmethod


class Base(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass


class Concreate(Base):
    def foo(self):
        print("foo")

    def bar(self):
        print("bar")

    # can define extra methods
    def baz(self):
        print("baz")


b = Base()  # TypeError: Can't instantiate abstract class Base with abstract methods foo
c = Concreate()
c.foo()
c.bar()
c.baz()
