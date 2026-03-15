from pydantic import BaseModel
from typing import ClassVar


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    total_pages: int
    genre: str

    _db: ClassVar[list["Book"]] = []

    def save(self):
        self.__class__._db.append(self)

    @classmethod
    def get_all(cls):
        return cls._db

    @classmethod
    def get_by_id(cls, book_id: int):
        for book in cls._db:
            if book.id == book_id:
                return book
        return None

    @classmethod
    def next_id(cls):
        if not cls._db:
            return 1
        return max(book.id for book in cls._db) + 1



if not Book.get_all():

    Book(
        id=1,
        title="Чистый код",
        author="Роберт Мартин",
        year=2008,
        total_pages=464,
        genre="Программирование"
    ).save()

    Book(
        id=2,
        title="Идеальный программист",
        author="Роберт Мартин",
        year=2011,
        total_pages=256,
        genre="Программирование"
    ).save()

    Book(
        id=3,
        title="Изучаем Python",
        author="Марк Лутц",
        year=2019,
        total_pages=1600,
        genre="Программирование"
    ).save()

    Book(
        id=4,
        title="История искусства",
        author="Эрнст Гомбрих",
        year=1950,
        total_pages=688,
        genre="Искусство"
    ).save()

    Book(
        id=5,
        title="Ван Гог. Жизнь",
        author="Стивен Найфи",
        year=2011,
        total_pages=976,
        genre="Искусство"
    ).save()