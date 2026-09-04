import json
from modelos.juego import Juego

class CatalogoJuegos:
    def __init__(self):
        self._juegos = []

    def cargar_desde_json(self, ruta_archivo: str):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
                for item in datos:
                    juego = Juego(
                        id_juego=item['id'],
                        titulo=item['titulo'],
                        genero=item['genero'],
                        desarrollador=item['desarrollador'],
                        rating=item['rating'],
                        precio=item['precio']
                    )
                    self.agregar_juego(juego)
        except FileNotFoundError:
            print(f"⚠️ No se encontró el archivo en: {ruta_archivo}")

    def agregar_juego(self, juego: Juego):
        self._juegos.append(juego)

    def listar_todos(self) -> list:
        return self._juegos

    def buscar_por_titulo(self, titulo: str) -> list:
        return [j for j in self._juegos if titulo.lower() in j.titulo.lower()]

    def filtrar_por_genero(self, genero: str) -> list:
        return [j for j in self._juegos if j.genero.lower() == genero.lower()]