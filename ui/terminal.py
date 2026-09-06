import os
from modelos.catalogo import CatalogoJuegos

class MenuTerminal:
    def __init__(self, catalogo: CatalogoJuegos):
        self._catalogo = catalogo

    def _limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _mostrar_encabezado(self):
        print("========================================")
        print("    ⚽ RECOMENDADOR JUEGOS — TERMINAL   ")
        print("========================================")

    def ejecutar(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_encabezado()
            print("1. Listar catálogo completo")
            print("2. Buscar juego por título")
            print("3. Filtrar por género")
            print("0. Salir")
            print("========================================")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self._listar_juegos()
            elif opcion == "2":
                self._buscar_por_titulo()
            elif opcion == "3":
                self._filtrar_por_genero()
            elif opcion == "0":
                print("\n¡Gracias por usar RecomendadorJuegos! 👋\n")
                break
            else:
                print("\n⚠️ Opción no válida. Intente nuevamente.")

            input("\nPresione ENTER para volver al menú...")

    def _listar_juegos(self):
        print("\n--- 🎮 CATÁLOGO COMPLETO ---")
        juegos = self._catalogo.listar_todos()
        if not juegos:
            print("El catálogo está vacío.")
            return
        for j in juegos:
            print(f"• [{j.id}] {j.titulo} | {j.genero} | ⭐ {j.rating} | Dev: {j.desarrollador}")

    def _buscar_por_titulo(self):
        titulo = input("\nIngrese el título a buscar: ").strip()
        resultados = self._catalogo.buscar_por_titulo(titulo)
        if resultados:
            print(f"\nResultados encontrados ({len(resultados)}):")
            for j in resultados:
                print(f"• {j.titulo} ({j.genero}) — ⭐ {j.rating}")
        else:
            print(f"\n❌ No se encontraron coincidencias para '{titulo}'.")

    def _filtrar_por_genero(self):
        genero = input("\nIngrese el género (ej. Deportes): ").strip()
        resultados = self._catalogo.filtrar_por_genero(genero)
        if resultados:
            print(f"\nJuegos del género '{genero}':")
            for j in resultados:
                print(f"• {j.titulo} — ⭐ {j.rating}")
        else:
            print(f"\n❌ No hay juegos registrados bajo el género '{genero}'.")