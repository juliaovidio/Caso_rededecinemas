from src.repositories.db import get_connection
from src.models.movie import Movie


class MovieRepository:
    def add(self, movie: Movie) -> int:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO movies (titulo, duracao_min, genero, diretor, elenco) VALUES (?, ?, ?, ?, ?)",
                (movie.titulo, movie.duracao_min, movie.genero, movie.diretor, movie.elenco),
            )
            conn.commit()
            return cur.lastrowid

    def get(self, movie_id: int) -> Movie | None:
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                "SELECT id, titulo, duracao_min, genero, diretor, elenco FROM movies WHERE id = ?",
                (movie_id,),
            )
            row = cur.fetchone()
            return Movie(*row) if row else None

    def list_all(self):
        with get_connection() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, titulo, duracao_min, genero, diretor, elenco FROM movies")
            return [Movie(*row) for row in cur.fetchall()]
