from modelos.juego import Juego
from modelos.catalogo import CatalogoJuegos
from ui.terminal import MenuTerminal

def main():
    catalogo = CatalogoJuegos()

    # Carga inicial de datos de prueba
    catalogo.agregar_juego(Juego(1, "FIFA 24", "Deportes", "EA Sports", 7.8, 60.0))
    catalogo.agregar_juego(Juego(2, "Football Manager 2024", "Deportes", "Sports Interactive", 8.9, 50.0))
    catalogo.agregar_juego(Juego(3, "Rocket League", "Deportes", "Psyonix", 8.6, 0.0))
    catalogo.agregar_juego(Juego(4, "eFootball 2024", "Deportes", "Konami", 7.5, 0.0))

    # Iniciar la interfaz
    menu = MenuTerminal(catalogo)
    menu.ejecutar()

if __name__ == "__main__":
    main()