from sqlalchemy import select

from app.db.db import get_session
from app.db.models import Book, Category


# ==========================
# CRUD для категорий
# ==========================

def create_category(title):
    with get_session() as session:
        category = Category(title=title)
        session.add(category)
        session.flush()
        return category.id


def get_categories():
    with get_session() as session:
        result = session.scalars(
            select(Category).order_by(Category.id)
        )
        return result.all()


def update_category(category_id, title):
    with get_session() as session:
        category = session.get(Category, category_id)

        if category is None:
            return False

        category.title = title
        return True


def delete_category(category_id):
    with get_session() as session:
        category = session.get(Category, category_id)

        if category is None:
            return False

        session.delete(category)
        return True


# ==========================
# CRUD для книг
# ==========================

def create_book(title, description, price, url, category_id):
    with get_session() as session:
        book = Book(
            title=title,
            description=description,
            price=price,
            url=url,
            category_id=category_id
        )

        session.add(book)
        session.flush()
        return book.id


def get_books():
    with get_session() as session:
        result = session.scalars(
            select(Book).order_by(Book.id)
        )
        return result.all()


def update_book(book_id, title, description, price, url, category_id):
    with get_session() as session:
        book = session.get(Book, book_id)

        if book is None:
            return False

        book.title = title
        book.description = description
        book.price = price
        book.url = url
        book.category_id = category_id

        return True


def delete_book(book_id):
    with get_session() as session:
        book = session.get(Book, book_id)

        if book is None:
            return False

        session.delete(book)
        return True
    
if __name__ == "__main__":
    
    print("\nПроверка CRUD категорий")

    category_id = create_category("Тестовая категория")

    print("Добавлена категория с ID:", category_id)

    category = next(
        (c for c in get_categories() if c.id == category_id),
        None
    )

    if category:
        print("Категория найдена:", category.title)

    update_category(category_id, "Обновлённая категория")

    print("Категория обновлена!")

    delete_category(category_id)

    print("Категория удалена!")
