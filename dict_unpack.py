def show(name, age):
    print(f"{name=}, {age=}")


if __name__ == "__main__":
    d = {"name": "John", "age": 30}
    show(**d)
    show(name="reza", age=20)
