import sqlite3
from pathlib import Path

DB_PATH = Path("data") / "cinema.db"


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS cinemas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                capacidade INTEGER NOT NULL,
                endereco TEXT NOT NULL
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                duracao_min INTEGER NOT NULL,
                genero TEXT NOT NULL,
                diretor TEXT NOT NULL,
                elenco TEXT NOT NULL
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cinema_id INTEGER NOT NULL,
                movie_id INTEGER NOT NULL,
                inicio TEXT NOT NULL,
                fim TEXT NOT NULL,
                FOREIGN KEY (cinema_id) REFERENCES cinemas(id),
                FOREIGN KEY (movie_id) REFERENCES movies(id)
            )
            """
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id INTEGER NOT NULL,
                data TEXT NOT NULL,
                publico INTEGER NOT NULL,
                FOREIGN KEY (session_id) REFERENCES sessions(id)
            )
            """
        )
        conn.commit()
