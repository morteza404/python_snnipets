def quadratic(a, b, c):
    def inner(x):
        return a * x**2 + b * x + c

    return inner


q = quadratic(1, 2, 3)
print(q(0))
print(q(1))
print(q(2))
print(q(3))
