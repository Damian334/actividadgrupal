from modelos.juego import Juego
from modelos.catalogo import CatalogoJuegos

def main():
    catalogo = CatalogoJuegos()

    # Datos de prueba iniciales
    catalogo.agregar_juego(Juego(1, "FIFA 24", "Deportes", "EA Sports", 7.8, 60.0))
    catalogo.agregar_juego(Juego(2, "Football Manager 2024", "Deportes", "Sports Interactive", 8.9, 50.0))
    catalogo.agregar_juego(Juego(3, "Rocket League", "Deportes", "Psyonix", 8.6, 0.0))

    print("=== Catálogo RecomendadorJuegos ===")
    for juego in catalogo.listar_todos():
        print(juego)

if __name__ == "__main__":
    main()