# Diagrama de clases

> Actualizado en TP1 con la implementación de la v1.

```mermaid
classDiagram

    class Videojuego {

        -id: int
        -titulo: str
        -genero: str
        -desarrollador: str
        -rating: float
        -precio: float

        +id() int
        +titulo() str
        +genero() str
        +desarrollador() str
        +rating() float
        +precio() float
        +repr() str
    }

    class Catalogo {

        -videojuegos: list

        +cargar_desde_json(ruta) None
        +buscar(titulo) Videojuego
        +listar() list
        +filtrar(genero) list
        +top_10() list
        +relacionados(titulo) list
        +alternativas_desarrollador(titulo) list
    }

    Catalogo "1" o-- "*" Videojuego : contiene
```

```text
> Buscar elemento
Título: Minecraft

╔══════════════════════════════════════╗
║           🎬 GAMeBOT                ║
╠══════════════════════════════════════╣
║ Si te gustó Minecraft, quizás te     ║
║ interesen:                           ║
║                                      ║
║ 1. Stardew Valley                    ║
║ 2. Don't Starve                      ║
║ 3. Terraria                          ║
║                                      ║
╚══════════════════════════════════════╝

