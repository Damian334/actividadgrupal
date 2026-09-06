import json
from modelos.juegos import Videojuego


class Catalogo:

    def __init__(self):
        self._videojuegos = []

    def cargar_desde_json(self, ruta):
        with open(ruta, encoding="utf-8") as archivo:
            datos = json.load(archivo)

        for item in datos:
            videojuego = Videojuego(
                item["id"],
                item["titulo"],
                item["genero"],
                item["desarrollador"],
                item["rating"],
                item["precio"]
            )

            self._videojuegos.append(videojuego)

    def listar(self):
        return list(self._videojuegos)

    def buscar(self, titulo):
        for videojuego in self._videojuegos:
            if videojuego.titulo.lower() == titulo.lower():
                return videojuego

        return None

    def filtrar(self, genero):
        resultados = []

        for videojuego in self._videojuegos:
            if videojuego.genero.lower() == genero.lower():
                resultados.append(videojuego)

        return resultados

    def top_10(self):
        videojuegos_ordenados = sorted(
            self._videojuegos,
            key=lambda videojuego: videojuego.rating,
            reverse=True
        )

        return videojuegos_ordenados[:10]

    def relacionados(self, titulo):
        videojuego = self.buscar(titulo)

        if videojuego is None:
            return []

        resultados = []

        for juego in self._videojuegos:
            if juego.genero.lower() == videojuego.genero.lower():
                if juego.titulo.lower() != videojuego.titulo.lower():
                    resultados.append(juego)

        return resultados

    def alternativas_desarrollador(self, titulo):
        videojuego = self.buscar(titulo)

        if videojuego is None:
            return []

        resultados = []

        for juego in self._videojuegos:
            if juego.desarrollador.lower() == videojuego.desarrollador.lower():
                if juego.titulo.lower() != videojuego.titulo.lower():
                    resultados.append(juego)

        return resultados