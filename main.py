from servicios.catalogo import Catalogo
from ui.terminal import MenuTerminal
from estructuras.arbol_binario import ArbolBST
from estructuras.avl import AVL
from estructuras.arbol_general import ArbolGeneral


def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/juegos.json")

    arbol = ArbolBST()
    avl = AVL()
    arbol_categorias = ArbolGeneral()

    videojuegos = catalogo.listar()

    for videojuego in videojuegos:
        arbol.insertar(
            videojuego,
            clave=lambda videojuego: videojuego.titulo.lower()
        )

        avl.insertar(videojuego)

    arbol_categorias.insertar_raiz("Videojuegos")

    generos = []

    for videojuego in videojuegos:
        genero = videojuego.genero

        if genero.lower() not in [
            existente.lower() for existente in generos
        ]:
            generos.append(genero)
            arbol_categorias.agregar_hijo("Videojuegos", genero)

    for videojuego in videojuegos:
        arbol_categorias.agregar_hijo(videojuego.genero, videojuego.titulo)

    menu = MenuTerminal(catalogo, arbol, avl, arbol_categorias)
    menu.ejecutar()


if __name__ == "__main__":
    main()