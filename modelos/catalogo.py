from modelos.juego import Juego

class CatalogoJuegos:
    def __init__(self):
        self._juegos = []

    def agregar_juego(self, juego: Juego):
        self._juegos.append(juego)

    def listar_todos(self) -> list:
        return self._juegos

    def buscar_por_titulo(self, titulo: str) -> list:
        return [j for j in self._juegos if titulo.lower() in j.titulo.lower()]

    def filtrar_por_genero(self, genero: str) -> list:
        return [j for j in self._juegos if j.genero.lower() == genero.lower()]