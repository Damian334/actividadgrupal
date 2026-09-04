# Diagrama de clases - boceto inicial

```mermaid
classDiagram
    class videojuego{
        -nombre: str
        -genero: str
        -rating: float
    }

    class Catalogo{
        -videojuegos: list
        +buscar(nombre) Elemento
        +listar() list
        +filtrar(genero) list
    }

 Catalogo "1" o-- "*" Elemento : contiene
```

```text
> Buscar elemento
Título: Minecraft

╔══════════════════════════════════════╗
║           🎬 CINEBOT                 ║
╠══════════════════════════════════════╣
║ Si te gustó Minecraft, quizás te     ║
║ interesen:                           ║
║                                      ║
║ 1. Stardew Valley                    ║
║ 2. Don't Starve                      ║
║ 3. Terraria                          ║
║                                      ║
╚══════════════════════════════════════╝

