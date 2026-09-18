from servicios.catalogo import Catalogo
from ui.terminal import MenuTerminal
from estructuras.arbol_binario import ArbolBST


def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/juegos.json")

    arbol = ArbolBST()

    for videojuego in catalogo.listar():
        arbol.insertar(
            videojuego,
            lambda videojuego: videojuego.titulo.lower()
        )

    menu = MenuTerminal(catalogo, arbol)
    menu.ejecutar()


if __name__ == "__main__":
    main()