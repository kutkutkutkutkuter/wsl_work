
from app.db.db import get_connection


def create_tables():
    with get_connection() as connection:
        with connection.cursor() as cursor:

            # Таблица категорий книг
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS categories (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL
                );
            """)

            # Таблица книг
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS books (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255) NOT NULL,
                    description TEXT,
                    price NUMERIC(10, 2) NOT NULL,
                    url TEXT DEFAULT '',
                    category INTEGER REFERENCES categories(id)
                );
            """)

    print("Таблицы успешно созданы!")


if __name__ == "__main__":
    create_tables()

