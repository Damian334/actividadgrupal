class Juego:
    def __init__(self, id_juego: int, titulo: str, genero: str, desarrollador: str, rating: float, precio: float):
        self._id = id_juego
        self._titulo = titulo
        self._genero = genero
        self._desarrollador = desarrollador
        self._rating = rating
        self._precio = precio

    @property
    def id(self) -> int:
        return self._id

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def genero(self) -> str:
        return self._genero

    @property
    def desarrollador(self) -> str:
        return self._desarrollador

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def precio(self) -> float:
        return self._precio

    def __repr__(self) -> str:
        return f"Juego('{self._titulo}', '{self._genero}', ⭐{self._rating})"