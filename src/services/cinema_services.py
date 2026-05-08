from datetime import datetime, timedelta
from src.models.cinema import Cinema
from src.models.movie import Movie
from src.models.session import Session
from src.repositories.cinema_repository import CinemaRepository
from src.repositories.movie_repository import MovieRepository
from src.repositories.session_repository import SessionRepository
from src.repositories.attendance_repository import AttendanceRepository


class CinemaService:
    def __init__(self):
        self.repo = CinemaRepository()

    def cadastrar_cinema(self, nome: str, capacidade: int, endereco: str) -> int:
        return self.repo.add(Cinema(None, nome, capacidade, endereco))


class MovieService:
    def __init__(self):
        self.repo = MovieRepository()

    def cadastrar_filme(self, titulo: str, duracao_min: int, genero: str, diretor: str, elenco: str) -> int:
        return self.repo.add(Movie(None, titulo, duracao_min, genero, diretor, elenco))


class SessionService:
    def __init__(self):
        self.repo = SessionRepository()
        self.movie_repo = MovieRepository()
        self.cinema_repo = CinemaRepository()

    def cadastrar_sessao(self, cinema_id: int, movie_id: int, inicio_iso: str) -> int:
        movie = self.movie_repo.get(movie_id)
        if not movie:
            raise ValueError("Filme não encontrado")
        cinema = self.cinema_repo.get(cinema_id)
        if not cinema:
            raise ValueError("Cinema não encontrado")

        inicio = datetime.fromisoformat(inicio_iso)
        fim = inicio + timedelta(minutes=movie.duracao_min)

        return self.repo.add(Session(None, cinema_id, movie_id, inicio.isoformat(), fim.isoformat()))


class AttendanceService:
    def __init__(self):
        self.att_repo = AttendanceRepository()
        self.session_repo = SessionRepository()
        self.cinema_repo = CinemaRepository()

    def registrar_publico(self, session_id: int, data: str, publico: int) -> int:
        session = self.session_repo.get(session_id)
        if not session:
            raise ValueError("Sessão não encontrada")
        cinema = self.cinema_repo.get(session.cinema_id)
        if not cinema:
            raise ValueError("Cinema não encontrado")
        if publico > cinema.capacidade:
            raise ValueError("Público excede capacidade do cinema")
        return self.att_repo.add(session_id, data, publico)


class ReportService:
    def __init__(self):
        self.att_repo = AttendanceRepository()

    def total_por_sessao(self, session_id: int) -> int:
        return self.att_repo.total_by_session(session_id)

    def total_por_filme(self, movie_id: int) -> int:
        return self.att_repo.total_by_movie(movie_id)

    def total_por_cinema(self, cinema_id: int) -> int:
        return self.att_repo.total_by_cinema(cinema_id)
