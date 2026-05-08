import sqlite3


def get_connection():
    return sqlite3.connect("cinema.db")


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cinemas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        endereco TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        genero TEXT NOT NULL,
        duracao INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        movie_id INTEGER,
        horario TEXT NOT NULL,
        sala TEXT NOT NULL,
        FOREIGN KEY(movie_id) REFERENCES movies(id)
    )
    """)

    conn.commit()
    conn.close()

    print("Banco inicializado com sucesso!")
