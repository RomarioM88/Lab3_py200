class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name
    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"
class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"Автор: '{self.name}'. Книга: '{self.author}'. Количество страниц: {self.pages}"
class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Продолжительность книги должна быть типа float")
        if duration <= 0:
            raise ValueError("Продолжительность книги должна быть положительным числом")
        self.duration = duration

    def __str__(self):
        return f"Автор: '{self.name}'. Книга: '{self.author}'. Продолжительность книги(час/мин): {self.duration}."

if __name__ == "__main__":
    book = Book("Война и мир", "Толстой Н.В.")
    print(book)
    paperbook = PaperBook("Пушкин А.С", "Пиковая дама", 1000)
    print(paperbook)
    ebook = AudioBook("Булгаков М.А", "Мастер и Маргарита", 10.36)
    print(ebook)
    #ebook.name = "cgffgfg"
    #print(ebook.name)