from src.repositories.db import get_connection
from src.models.session import Session


class SessionRepository:
    def add(self, session: Session) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO sessions (cinema_id, movie_id, inicio, fim) VALUES (?, ?, ?, ?)",
                (session.cinema_id, session.movie_id, session.inicio, session.fim),
            )
            conn.commit()
            return cur.lastrowid

    def get(self, session_id: int) -> Session | None:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, cinema_id, movie_id, inicio, fim FROM sessions WHERE id = ?",
                (session_id,),
            )
            row = cur.fetchone()
            return Session(*row) if row else None

    def list_all(self):
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, cinema_id, movie_id, inicio, fim FROM sessions")
            return [Session(*row) for row in cur.fetchall()]
