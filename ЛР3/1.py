class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        super.__str__(self)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    def __str__(self):
        return f"{super().__str__()}. Страниц {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name=name, author=author)
        super().__str__()
        if not isinstance(duration, (float, int)):
            raise TypeError("Продолжительность книги должна быть типа int или float")
        if duration <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    def __str__(self):
        return f"{super().__str__()}. Продолжительность {self.duration}"


pap1 = PaperBook('first', 'he', 1)
aud1 = AudioBook('second', 'she', 2)
print(pap1)
print(aud1)
