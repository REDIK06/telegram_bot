import sqlite3
from pathlib import Path
from pprint import pprint

db = None
cursor = None

def init_db():
    global db, cursor
    db = sqlite3.connect(Path(__file__).resolve().parent.parent / "db.sqlite")
    cursor = db.cursor()

def create_tables():
    cursor.execute("""
    DROP TABLE IF EXISTS kinopoisk;
    """)

    cursor.execute("""
    DROP TABLE IF EXISTS genres;
        """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS kinopoisk (
            id INTEGER PRIMARY KEY,
            name TEXT,
            genre_id INTEGER,
            duration TEXT,
            year INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    """)

    db.commit()


def populate_db():
    cursor.execute("""
    INSERT INTO genres (name) VALUES 
        ("фильм/треллер/экшентриллер"),
        ("чёрная комедия/научная фантастика"),
        ("фантастика/фильм ужасов/драма"),
        ("мистерия"),
        ("боевик/триллер"),
        ("научная фантастика/боевик/комедия"),
        ("боевик/триллер/криминал"),
        ("драма/мелодрама"),
        ("триллер/драма"),
        ("драма/биография")
    """)
    # Добавьте фильмы с указанием genre_id
    cursor.execute("""
    INSERT INTO kinopoisk (name, genre_id, duration, year) VALUES 
        ("Красное уведомление", 1, "1ч 58", 2021),
        ("Не смотри вверх", 2, "2ч 25", 2021),
        ("Птичий короб", 3, "2ч 4", 2018),
        ("Достать ножи: Стеклянная луковица", 4, "2ч 19", 2022),
        ("Серый человек", 5, "2ч 2", 2022),
        ("Проект 'Адам'", 6, "1ч 46", 2022),
        ("Тайлер Рейк: Операция по спасению", 7, "1ч 56", 2020),
        ("Пурпурные сердца", 8, "2ч 2", 2022),
        ("Непрощённая", 8, "1ч 52", 2021),
        ("Ирландец", 10, "3ч 29", 2019)
    """)
    db.commit()


def get_movies_by_genre(genre_id):
    cursor.execute("""
        SELECT * FROM kinopoisk WHERE genre_id = ?
    """, (genre_id,))
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
    pprint(get_movies_by_genre(1))
