from servicios.catalogo import Catalogo
from ui.terminal import MenuTerminal

def main():
    catalogo = Catalogo()
    catalogo.cargar_desde_json("datos/juegos.json")
    menu = MenuTerminal(catalogo)
    menu.ejecutar()

if __name__ == "__main__":
    main()