
from sqlalchemy import String, Text, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.db import Base, engine


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        unique=True
    )
    books: Mapped[list["Book"]] = relationship(
    back_populates="category",
    cascade="all, delete-orphan"
)

class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(Text)

    price: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    url: Mapped[str] = mapped_column(Text, default="")

    category_id: Mapped[int | None] = mapped_column(
        "category",
        ForeignKey("categories.id")
    )

    category: Mapped["Category | None"] = relationship(
        back_populates="books"
    )


def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Таблицы успешно созданы!")


if __name__ == "__main__":
    create_tables()

