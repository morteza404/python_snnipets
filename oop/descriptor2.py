class Movie:
    def __init__(self, title, rating, runtime, budget, gross):
        self.title = title
        self.rating = rating
        self.runtime = runtime
        self.budget = budget
        self.gross = gross

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        self._title = value

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        if not isinstance(value, int):
            raise TypeError("rating must be an integer")
        if value < 0:
            raise ValueError(f"negative value not allowed {value}")
        self._rating = value

    @property
    def runtime(self):
        return self._runtime

    @runtime.setter
    def runtime(self, value):
        if not isinstance(value, int):
            raise TypeError("runtime must be an integer")
        if value < 0:
            raise ValueError(f"negative value not allowed {value}")
        self._runtime = value

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, value):
        if not isinstance(value, int):
            raise TypeError("budget must be an integer")
        if value < 0:
            raise ValueError(f"negative value not allowed {value}")
        self._budget = value

    @property
    def gross(self):
        return self._gross

    @gross.setter
    def gross(self, value):
        if not isinstance(value, int):
            raise TypeError("gross must be an integer")
        if value < 0:
            raise ValueError(f"negative value not allowed {value}")
        self._gross = value


    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.rating}, {self.runtime}, {self.budget}, {self.gross})"


movie = Movie("The Matrix", 8, 136, 63000000, 60310868)
print(movie)
