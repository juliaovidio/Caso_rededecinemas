class CLIView:
    def menu(self):
        print("\n=== Rede de Cinemas ===")
        print("1. Cadastrar cinema")
        print("2. Cadastrar filme")
        print("3. Cadastrar sessão")
        print("4. Registrar público")
        print("5. Total por sessão")
        print("6. Total por filme")
        print("7. Total por cinema")
        print("0. Sair")
        return input("Escolha: ")

    def input_cinema(self):
        return (
            input("Nome: "),
            int(input("Capacidade: ")),
            input("Endereço: "),
        )

    def input_filme(self):
        return (
            input("Título: "),
            int(input("Duração (min): ")),
            input("Gênero: "),
            input("Diretor: "),
            input("Elenco: "),
        )

    def input_sessao(self):
        return (
            int(input("Cinema ID: ")),
            int(input("Filme ID: ")),
            input("Início (YYYY-MM-DD HH:MM): ").replace(" ", "T"),
        )

    def input_publico(self):
        return (
            int(input("Sessão ID: ")),
            input("Data (YYYY-MM-DD): "),
            int(input("Público: ")),
        )

    def input_id(self, label):
        return int(input(f"{label} ID: "))

    def show(self, msg):
        print(msg)
