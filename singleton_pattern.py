from functools import wraps


def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        nonlocal instances
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance


@singleton
class MyClass:
    def __init__(self, value):
        self.value = value

    def some_method(self):
        print(f"Value: {self.value}")


obj1 = MyClass(10)
obj2 = MyClass(20)
obj3 = MyClass(30)

print(obj1 is obj2)
print(obj1 is obj3)
