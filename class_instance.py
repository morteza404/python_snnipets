# object instance
class CountInstances:
    count = 0

    def __init__(self):
        self.count += 1


print("object instance")
for _ in range(10):
    print(CountInstances().count)


# class instance
class CountInstances:
    count = 0

    def __init__(self):
        self.__class__.count += 1


print("class instance")
for _ in range(10):
    print(CountInstances().count)
