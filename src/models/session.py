from dataclasses import dataclass

@dataclass
class Session:
    id: int | None
    cinema_id: int
    movie_id: int
    inicio: str  # ISO datetime
    fim: str     # ISO datetime
