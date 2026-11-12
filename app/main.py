
from app.db.crud import get_categories, get_books


def main():
    print("=" * 60)
    print("             КАТАЛОГ КНИЖНОГО МАГАЗИНА")
    print("=" * 60)

    categories = get_categories()
    books = get_books()

    if not categories:
        print("Категории не найдены.")
        return

    for category in categories:
        print(f"\n Категория: {category.title}")
        print("-" * 60)

        category_books = [
            book for book in books
            if book.category_id == category.id
        ]

        if not category_books:
            print("В этой категории пока нет книг.")
            continue

        for book in category_books:
            print(f"Название: {book.title}")
            print(f"Описание: {book.description}")
            print(f"Цена: {book.price} руб.")
            print(f"Ссылка: {book.url or 'Не указана'}")
            print("-" * 40)

    print("\nКаталог успешно загружен!")
    print(f"Всего категорий: {len(categories)}")
    print(f"Всего книг: {len(books)}")


if __name__ == "__main__":
    main()

