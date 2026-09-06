from modelos.catalogo import CatalogoJuegos
from ui.terminal import MenuTerminal

def main():
    catalogo = CatalogoJuegos()
    
    # Carga dinámica desde la capa de datos
    catalogo.cargar_desde_json("datos/juegos.json")

    # Iniciar la interfaz
    menu = MenuTerminal(catalogo)
    menu.ejecutar()

if __name__ == "__main__":
    main()