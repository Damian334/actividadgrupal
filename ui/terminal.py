import os

from servicios.catalogo import Catalogo


class MenuTerminal:

    def __init__(self, catalogo: Catalogo):
        self._catalogo = catalogo

    def _limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _mostrar_encabezado(self):
        print("========================================")
        print("          GAMeBOT - TERMINAL            ")
        print("========================================")

    def ejecutar(self):
        while True:
            self._limpiar_pantalla()
            self._mostrar_encabezado()

            print("1. Buscar videojuego")
            print("2. Explorar por género")
            print("3. Ver Top 10 mejores")
            print("4. Ver videojuegos relacionados")
            print("5. Ver alternativas del desarrollador")
            print("0. Salir")
            print("========================================")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self._buscar_por_titulo()

            elif opcion == "2":
                self._filtrar_por_genero()

            elif opcion == "3":
                self._ver_top_10()

            elif opcion == "4":
                self._ver_relacionados()

            elif opcion == "5":
                self._ver_alternativas()

            elif opcion == "0":
                print("\n¡Gracias por usar GAMeBOT!\n")
                break

            else:
                print("\nOpción no válida. Intente nuevamente.")

            input("\nPresione ENTER para volver al menú...")

    def _buscar_por_titulo(self):
        titulo = input("\nIngrese el título a buscar: ").strip()

        juego = self._catalogo.buscar(titulo)

        if juego:
            print("\n--- VIDEOJUEGO ENCONTRADO ---")
            print(f"Título: {juego.titulo}")
            print(f"Género: {juego.genero}")
            print(f"Desarrollador: {juego.desarrollador}")
            print(f"Rating: {juego.rating}")
            print(f"Precio: ${juego.precio}")
        else:
            print(f"\nNo se encontró el videojuego '{titulo}'.")

    def _filtrar_por_genero(self):
        genero = input("\nIngrese el género: ").strip()

        resultados = self._catalogo.filtrar(genero)

        if resultados:
            print(f"\n--- JUEGOS DE {genero.upper()} ---")

            for juego in resultados:
                print(
                    f"- {juego.titulo} | "
                    f"Rating: {juego.rating} | "
                    f"Desarrollador: {juego.desarrollador}"
                )
        else:
            print(f"\nNo hay juegos del género '{genero}'.")

    def _ver_top_10(self):
        resultados = self._catalogo.top_10()

        print("\n--- TOP 10 MEJORES VIDEOJUEGOS ---")

        posicion = 1

        for juego in resultados:
            print(
                f"{posicion}. {juego.titulo} | "
                f"Rating: {juego.rating}"
            )

            posicion += 1

    def _ver_relacionados(self):
        titulo = input("\nIngrese el título del videojuego: ").strip()

        resultados = self._catalogo.relacionados(titulo)

        if resultados:
            print(f"\n--- VIDEOJUEGOS RELACIONADOS CON {titulo.upper()} ---")

            for juego in resultados:
                print(
                    f"- {juego.titulo} | "
                    f"Género: {juego.genero} | "
                    f"Rating: {juego.rating}"
                )
        else:
            print("\nNo se encontraron videojuegos relacionados.")

    def _ver_alternativas(self):
        titulo = input("\nIngrese el título del videojuego: ").strip()

        resultados = self._catalogo.alternativas_desarrollador(titulo)

        if resultados:
            print(
                f"\n--- ALTERNATIVAS DEL DESARROLLADOR DE "
                f"{titulo.upper()} ---"
            )

            for juego in resultados:
                print(
                    f"- {juego.titulo} | "
                    f"Rating: {juego.rating}"
                )
        else:
            print("\nNo se encontraron otras alternativas del desarrollador.")