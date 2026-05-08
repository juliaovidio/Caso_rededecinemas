from dataclasses import dataclass

@dataclass
class Cinema:
    id: int | None
    nome: str
    capacidade: int
    endereco: str
