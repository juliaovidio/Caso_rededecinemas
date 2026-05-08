from src.repositories.db import get_connection


class AttendanceRepository:
    def add(self, session_id: int, data: str, publico: int) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO attendance (session_id, data, publico) VALUES (?, ?, ?)",
                (session_id, data, publico),
            )
            conn.commit()
            return cur.lastrowid

    def total_by_session(self, session_id: int) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT COALESCE(SUM(publico),0) FROM attendance WHERE session_id = ?", (session_id,))
            return cur.fetchone()[0]

    def total_by_movie(self, movie_id: int) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT COALESCE(SUM(a.publico),0)
                FROM attendance a
                JOIN sessions s ON s.id = a.session_id
                WHERE s.movie_id = ?
                """,
                (movie_id,),
            )
            return cur.fetchone()[0]

    def total_by_cinema(self, cinema_id: int) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                """
                SELECT COALESCE(SUM(a.publico),0)
                FROM attendance a
                JOIN sessions s ON s.id = a.session_id
                WHERE s.cinema_id = ?
                """,
                (cinema_id,),
            )
            return cur.fetchone()[0]
