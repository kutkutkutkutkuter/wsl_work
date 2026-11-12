
from app.db.db import get_session
from app.db.models import create_tables
from app.db.crud import (
    create_category,
    create_book,
    get_categories,
    get_books
)


def initialize_database():
    create_tables()

    with get_session() as session:

        if get_categories(session):
            print("База данных уже заполнена!")
            return

        # Создание категорий
        fiction_id = create_category(
            session,
            "Художественная литература"
        )

        fantasy_id = create_category(
            session,
            "Фэнтези и фантастика"
        )

        science_id = create_category(
            session,
            "Научная литература"
        )

        # Художественная литература
        create_book(
            session,
            "Мастер и Маргарита",
            "Роман Михаила Булгакова",
            650, "", fiction_id
        )

        create_book(
            session,
            "Преступление и наказание",
            "Роман Фёдора Достоевского",
            550, "", fiction_id
        )

        create_book(
            session,
            "1984",
            "Антиутопический роман Джорджа Оруэлла",
            700, "", fiction_id
        )

        # Фэнтези и фантастика
        create_book(
            session,
            "Властелин колец",
            "Фэнтези-роман Джона Толкина",
            1200, "", fantasy_id
        )

        create_book(
            session,
            "Гарри Поттер и философский камень",
            "Фэнтези-роман Джоан Роулинг",
            850, "", fantasy_id
        )

        create_book(
            session,
            "Дюна",
            "Научно-фантастический роман Фрэнка Герберта",
            950, "", fantasy_id
        )

        # Научная литература
        create_book(
            session,
            "Краткая история времени",
            "Книга Стивена Хокинга о Вселенной",
            750, "", science_id
        )

        create_book(
            session,
            "Эгоистичный ген",
            "Книга Ричарда Докинза о теории эволюции",
            800, "", science_id
        )

        create_book(
            session,
            "Космос",
            "Книга Карла Сагана об устройстве Вселенной",
            900, "", science_id
        )

        print("База данных успешно заполнена!")
        print("Категорий:", len(get_categories(session)))
        print("Книг:", len(get_books(session)))


if __name__ == "__main__":
    initialize_database()
