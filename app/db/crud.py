
from app.db.db import get_connection


# =====================================
# CATEGORIES — КАТЕГОРИИ
# =====================================

# CREATE — создание категории
def create_category(title):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO categories (title)
                VALUES (%s)
                RETURNING id;
            """, (title,))

            return cursor.fetchone()["id"]


# READ — получение всех категорий
def get_categories():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title
                FROM categories
                ORDER BY id;
            """)

            return cursor.fetchall()


# UPDATE — обновление категории
def update_category(category_id, title):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE categories
                SET title = %s
                WHERE id = %s;
            """, (title, category_id))


# DELETE — удаление категории
def delete_category(category_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM categories
                WHERE id = %s;
            """, (category_id,))


# =====================================
# BOOKS — КНИГИ
# =====================================

# CREATE — создание книги
def create_book(title, description, price, url, category):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO books
                (title, description, price, url, category)
                VALUES (%s, %s, %s, %s, %s)
                RETURNING id;
            """, (title, description, price, url, category))

            return cursor.fetchone()["id"]


# READ — получение всех книг
def get_books():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT
                    id,
                    title,
                    description,
                    price,
                    url,
                    category
                FROM books
                ORDER BY id;
            """)

            return cursor.fetchall()


# UPDATE — обновление книги
def update_book(
    book_id,
    title,
    description,
    price,
    url,
    category
):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                UPDATE books
                SET title = %s,
                    description = %s,
                    price = %s,
                    url = %s,
                    category = %s
                WHERE id = %s;
            """, (
                title,
                description,
                price,
                url,
                category,
                book_id
            ))


# DELETE — удаление книги
def delete_book(book_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""
                DELETE FROM books
                WHERE id = %s;
            """, (book_id,))
