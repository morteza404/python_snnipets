class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("title must be a string")
        self._title = value

    @property
    def author(self):
        return self._author
    @title.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("author must be a string")
        self._author = value

    @property
    def pages(self):
        return self._pages
    @title.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("pages must be a int")
        if value < 0:
            raise TypeError("pages must be a positive int")
        self._pages = value

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title}, {self.pages}, {self.author})"
    
book = Book("Python", "Guido van Rossum", 200)
print(book)
print(vars(book))
print(book.__dict__)