def outer():
    x = 10

    def inner():
        nonlocal x
        x += 1
        print("x =", x)

    return inner


f = outer()
f()
f()
f()
