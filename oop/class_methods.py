# Helper methods for initialization:


class MyStream:

    @classmethod
    def from_file(cls, filepath, ignore_comments=False):
        with open(filepath, "r") as fileobj:
            for obj in cls(fileobj, ignore_comments):
                yield obj

    @classmethod
    def from_socket(cls, socket, ignore_comments=False):
        # Placeholder until implemented
        raise NotImplementedError("from_socket method is not implemented yet")

    def __init__(self, iterable, ignore_comments=False):
        self.iterable = iterable
        self.ignore_comments = ignore_comments

    def __iter__(self):
        for line in self.iterable:
            if self.ignore_comments and line.startswith("#"):
                continue
            yield line.strip()
