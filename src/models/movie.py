from dataclasses import dataclass

@dataclass
class Movie:
    id: int | None
    titulo: str
    duracao_min: int
    genero: str
    diretor: str
    elenco: str
