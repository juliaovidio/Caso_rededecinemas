from src.repositories.db import init_db
from src.controllers.cinema_controller import CinemaController
from src.views.cli_view import CLIView


def main():
    init_db()
    controller = CinemaController()
    view = CLIView()

    while True:
        op = view.menu()
        try:
            if op == "1":
                nome, capacidade, endereco = view.input_cinema()
                cinema_id = controller.criar_cinema(nome, capacidade, endereco)
                view.show(f"Cinema criado com ID {cinema_id}")
            elif op == "2":
                titulo, duracao, genero, diretor, elenco = view.input_filme()
                movie_id = controller.criar_filme(titulo, duracao, genero, diretor, elenco)
                view.show(f"Filme criado com ID {movie_id}")
            elif op == "3":
                cinema_id, movie_id, inicio = view.input_sessao()
                session_id = controller.criar_sessao(cinema_id, movie_id, inicio)
                view.show(f"Sessão criada com ID {session_id}")
            elif op == "4":
                session_id, data, publico = view.input_publico()
                reg_id = controller.registrar_publico(session_id, data, publico)
                view.show(f"Público registrado com ID {reg_id}")
            elif op == "5":
                session_id = view.input_id("Sessão")
                total = controller.relatorio_sessao(session_id)
                view.show(f"Total da sessão: {total}")
            elif op == "6":
                movie_id = view.input_id("Filme")
                total = controller.relatorio_filme(movie_id)
                view.show(f"Total do filme: {total}")
            elif op == "7":
                cinema_id = view.input_id("Cinema")
                total = controller.relatorio_cinema(cinema_id)
                view.show(f"Total do cinema: {total}")
            elif op == "0":
                break
            else:
                view.show("Opção inválida")
        except Exception as exc:
            view.show(f"Erro: {exc}")


if __name__ == "__main__":
    main()
