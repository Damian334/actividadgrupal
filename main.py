from servicios.catalogo import Catalogo
from ui.terminal import MenuTerminal
from estructuras.arbol_binario import ArbolBST
from estructuras.heap import MaxHeapSimple  


def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/juegos.json")

    arbol = ArbolBST()
    heap = MaxHeapSimple()  

    
    for videojuego in catalogo.listar():
        # para búsquedas por título
        arbol.insertar(
            videojuego,
            clave=lambda videojuego: videojuego.titulo.lower()
        )
        # Insertamos en el Heap (para el ranking de mejores ratings)
        heap.insertar(videojuego)

    
    menu = MenuTerminal(catalogo, arbol, heap)
    menu.ejecutar()


if __name__ == "__main__":
    main()
