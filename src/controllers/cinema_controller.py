from src.services.cinema_services import CinemaService, MovieService, SessionService, AttendanceService, ReportService


class CinemaController:
    def __init__(self):
        self.cinema_service = CinemaService()
        self.movie_service = MovieService()
        self.session_service = SessionService()
        self.attendance_service = AttendanceService()
        self.report_service = ReportService()

    def criar_cinema(self, nome, capacidade, endereco):
        return self.cinema_service.cadastrar_cinema(nome, capacidade, endereco)

    def criar_filme(self, titulo, duracao, genero, diretor, elenco):
        return self.movie_service.cadastrar_filme(titulo, duracao, genero, diretor, elenco)

    def criar_sessao(self, cinema_id, movie_id, inicio_iso):
        return self.session_service.cadastrar_sessao(cinema_id, movie_id, inicio_iso)

    def registrar_publico(self, session_id, data, publico):
        return self.attendance_service.registrar_publico(session_id, data, publico)

    def relatorio_sessao(self, session_id):
        return self.report_service.total_por_sessao(session_id)

    def relatorio_filme(self, movie_id):
        return self.report_service.total_por_filme(movie_id)

    def relatorio_cinema(self, cinema_id):
        return self.report_service.total_por_cinema(cinema_id)
