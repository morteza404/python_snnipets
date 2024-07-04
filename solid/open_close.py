# bofore

"""
این اصل میگوید که کلاس باید برای  گسترش باز و برای تغییر بسته باشد
در مثال بد زیر برای گفتن هر نوع جک جدید باید کلاس تغییر کند
"""


class Joke:
    def tell_joke(self): ...
    def tell_regular_joke(self): ...
    def tell_knock_joke(self): ...


# after
class Joke2:
    def tell_joke(self):
        raise NotImplementedError


class RegularJoke(Joke2):
    def tell_joke(self): ...


class KnockJoke(Joke2):
    def tell_joke(self): ...
