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
        CREATE TABLE IF NOT EXISTS kinopoisk (
            id INTEGER PRIMARY KEY,
            name TEXT,
            genre TEXT,
            duration TEXT,
            year INTEGER
        )
    """)
    db.commit()


def populate_db():
    cursor.execute("""
    INSERT INTO kinopoisk (name, genre, duration, year) VALUES 
        ("Красное уведомление", "фильм/треллер/экшентриллер","1ч 58", 2021),
        ("Не смотри вверх", "чёрная комедия/научная фантастика/фильм-катастрофа/политическая сатира","2ч 25", 2021),
        ("Птичий короб", "фантастика/фильм ужасов/драма","2ч 4", 2018),
        ("Достать ножи: Стеклянная луковица", "мистерия","2ч 19", 2022),
        ("Серый человек", "боевик/триллер","2ч 2", 2022),
        ("Проект 'Адам'", "научная фантастика/боевик/комедия","1ч 46", 2022),
        ("Тайлер Рейк: Операция по спасению", "боевик/триллер/криминал","1ч 56", 2020),
        ("Пурпурные сердца", "драма/мелодрама","2ч 2", 2022),
        ("Непрощённая", "триллер/драма","1ч 52", 2021),
        ("Ирландец", "драма/биография","3ч 29", 2019)
    """)
    db.commit()

def get_kinopoisk():
    cursor.execute("""
        SELECT * FROM kinopoisk
    """)
    return cursor.fetchall()


if __name__ == "__main__":
    init_db()
    create_tables()
    populate_db()
    pprint(get_kinopoisk())

