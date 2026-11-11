from app.db.crud import get_categories, get_books


def main():
    print("=" * 50)
    print("       КАТАЛОГ КНИЖНОГО МАГАЗИНА")
    print("=" * 50)

    categories = get_categories()
    books = get_books()

    for category in categories:
        print(f"\nКатегория: {category['title']}")
        print("-" * 50)

        for book in books:
            if book["category"] == category["id"]:
                print(f"Название: {book['title']}")
                print(f"Описание: {book['description']}")
                print(f"Цена: {book['price']} руб.")
                print(f"Ссылка: {book['url'] or 'Не указана'}")
                print("-" * 30)

    print("\nРабота программы завершена!")


if __name__ == "__main__":
    main()
