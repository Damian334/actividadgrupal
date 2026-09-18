from estructuras.arbol_binario import ArbolBST


class Elemento:

    def __init__(self, titulo, rating):
        self.titulo = titulo
        self.rating = rating

    def __repr__(self):
        return f"{self.titulo} (rating {self.rating})"


def main():

    arbol = ArbolBST()

    datos = [
        Elemento("Minecraft", 9.0),
        Elemento("Fortnite", 8.5),
        Elemento("Grand Theft Auto V", 9.5),
        Elemento("The Witcher 3", 9.3),
        Elemento("Red Dead Redemption 2", 9.7),
    ]

    for elemento in datos:
        arbol.insertar(
            elemento,
            clave=lambda elemento: elemento.titulo.lower()
        )

    print("Altura del árbol:", arbol.altura())

    print("\n--- inorder (ordenado alfabéticamente) ---")
    for elemento in arbol.inorder():
        print(" ", elemento)

    print("\n--- preorder ---")
    for elemento in arbol.preorder():
        print(" ", elemento.titulo)

    print("\n--- postorder ---")
    for elemento in arbol.postorder():
        print(" ", elemento.titulo)

    print("\n--- búsquedas ---")

    encontrado = arbol.buscar(
        "minecraft",
        clave=lambda elemento: elemento.titulo.lower()
    )
    print("Buscar 'minecraft':", encontrado)

    no_encontrado = arbol.buscar(
        "Far Cry",
        clave=lambda elemento: elemento.titulo.lower()
    )
    print("Buscar 'Far cry':", no_encontrado)


if __name__ == "__main__":
    main()