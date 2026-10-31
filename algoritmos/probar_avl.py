import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from estructuras.avl import AVL
from estructuras.arbol_binario import ArbolBST
from modelos.juegos import Videojuego
def probar_avl_vs_bst():
    print("=== PRUEBA AVL: GAMeBOT ===")
    
    # 10 videojuegos en orden alfabético estricto (peor caso para el BST)
    # Respetando tu constructor: (id_juego, titulo, genero, desarrollador, rating, precio)
    juegos_ordenados = [
        Videojuego(1, "Dark Souls", "RPG", "FromSoftware", 9.0, 39.99),
        Videojuego(2, "Elden Ring", "RPG", "FromSoftware", 9.6, 59.99),
        Videojuego(3, "Fortnite", "Battle Royale", "Epic Games", 8.5, 0.0),
        Videojuego(4, "Grand Theft Auto V", "Acción", "Rockstar Games", 9.5, 29.99),
        Videojuego(5, "Minecraft", "Sandbox", "Mojang", 9.0, 26.95),
        Videojuego(6, "Red Dead Redemption 2", "Acción", "Rockstar Games", 9.7, 59.99),
        Videojuego(7, "Skyrim", "RPG", "Bethesda", 9.2, 39.99),
        Videojuego(8, "Tetris", "Puzle", "Tetris Company", 8.0, 9.99),
        Videojuego(9, "The Witcher 3", "RPG", "CD Projekt Red", 9.3, 39.99),
        Videojuego(10, "Zelda: Breath of the Wild", "Aventura", "Nintendo", 9.8, 59.99),
    ]

    bst = ArbolBST()
    avl = AVL()

    # Carga en BST
    inicio_bst = time.perf_counter()
    for j in juegos_ordenados:
        bst.insertar(j, clave=lambda x: x.titulo.lower())
    fin_bst = time.perf_counter()

    # Carga en AVL
    inicio_avl = time.perf_counter()
    for j in juegos_ordenados:
        avl.insertar(j)
    fin_avl = time.perf_counter()

    print(f"\n1. Cantidad de videojuegos cargados: {len(juegos_ordenados)}")
    print(f"2. Altura BST (Desbalanceado): {bst.altura()}  [Esperado: 10]")
    print(f"3. Altura AVL (Auto-balanceado): {avl.obtener_altura(avl.raiz)}  [Esperado: 4]")
    print(f"4. Tiempo inserción BST: {fin_bst - inicio_bst:.6f} seg")
    print(f"5. Tiempo inserción AVL: {fin_avl - inicio_avl:.6f} seg")

    print("\n--- Búsqueda rápida en AVL ---")
    encontrado = avl.buscar("Minecraft")
    print("Búsqueda 'Minecraft':", encontrado)

    print("\n--- Recorrido Inorder AVL (Orden Alfabético) ---")
    for juego in avl.inorder():
        print(" ", juego)

if __name__ == "__main__":
    probar_avl_vs_bst()