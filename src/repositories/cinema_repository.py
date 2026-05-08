from src.repositories.db import get_connection
from src.models.cinema import Cinema


class CinemaRepository:
    def add(self, cinema: Cinema) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO cinemas (nome, capacidade, endereco) VALUES (?, ?, ?)",
                (cinema.nome, cinema.capacidade, cinema.endereco),
            )
            conn.commit()
            return cur.lastrowid

    def get(self, cinema_id: int) -> Cinema | None:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, nome, capacidade, endereco FROM cinemas WHERE id = ?", (cinema_id,))
            row = cur.fetchone()
            return Cinema(*row) if row else None

    def list_all(self):
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, nome, capacidade, endereco FROM cinemas")
            return [Cinema(*row) for row in cur.fetchall()]
