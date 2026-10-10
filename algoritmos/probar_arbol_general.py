import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from servicios.catalogo import Catalogo
from estructuras.arbol_general import ArbolGeneral


def probar_arbol_general():
    print("=== PRUEBA DEL ARBOL GENERAL - GAMeBOT ===")

    catalogo = Catalogo()
    ruta_json = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "datos",
        "juegos.json"
    )

    catalogo.cargar_desde_json(ruta_json)
    videojuegos = catalogo.listar()

    # Crear el árbol general
    arbol = ArbolGeneral()
    arbol.insertar_raiz("Videojuegos")

    # Crear una categoría por cada género
    generos = []

    for juego in videojuegos:
        if juego.genero not in generos:
            generos.append(juego.genero)
            arbol.agregar_hijo("Videojuegos", juego.genero)

    # Agregar cada videojuego debajo de su género
    for juego in videojuegos:
        arbol.agregar_hijo(juego.genero, juego.titulo)

    print(f"\nCantidad de videojuegos: {len(videojuegos)}")
    print(f"Cantidad de géneros: {len(generos)}")

    print("\n--- Categorías y videojuegos ---")
    for genero in generos:
        print(f"\n{genero}:")
        for juego in catalogo.filtrar(genero):
            print(f"  - {juego.titulo}")

    print("\n--- Recorrido por amplitud (BFS) ---")
    print(arbol.amplitud())

    print("\n--- Recorrido profundidad preorder ---")
    print(arbol.profundidad_preorder())

    print("\n--- Recorrido profundidad postorder ---")
    print(arbol.profundidad_postorder())


if __name__ == "__main__":
    probar_arbol_general()