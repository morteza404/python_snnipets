class NonNegative:
    def __set_name__(self, object_type, name):
        self.name = name
    def __get__(self, instance, object_type):
        return vars(instance)[self.name]
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        vars(instance)[self.name] = value

class Movie:
    rating = NonNegative()
    runtime = NonNegative()
    budget = NonNegative()
    gross = NonNegative()
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.rating}, {self.runtime}, {self.budget}, {self.gross})"

movie = Movie("The Matrix", 8, 136, 63000000, 60310868)
print(movie)