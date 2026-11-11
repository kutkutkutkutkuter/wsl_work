from app.db.models import create_tables
from app.db.crud import (
    create_category,
    create_book,
    get_categories,
    get_books
)


def initialize_database():
    create_tables()

    if get_categories():
        print("База данных уже заполнена!")
        return

    fiction_id = create_category("Художественная литература")
    science_id = create_category("Научная литература")

    create_book(
        "Мастер и Маргарита",
        "Роман Михаила Булгакова",
        650,
        "",
        fiction_id
    )

    create_book(
        "Преступление и наказание",
        "Роман Фёдора Достоевского",
        550,
        "",
        fiction_id
    )

    create_book(
        "Краткая история времени",
        "Книга Стивена Хокинга",
        750,
        "",
        science_id
    )

    create_book(
        "Эгоистичный ген",
        "Книга Ричарда Докинза",
        800,
        "",
        science_id
    )

    print("База данных успешно заполнена!")
    print("Категорий:", len(get_categories()))
    print("Книг:", len(get_books()))


if __name__ == "__main__":
    initialize_database()
