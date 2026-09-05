# Diagrama de clases - boceto inicial

```mermaid
classDiagram
    class Juego {
        -int id
        -string titulo
        -string genero
        -string desarrollador
        -float rating
        -float precio
        +getId() int
        +getTitulo() string
        +getGenero() string
        +getDesarrollador() string
        +getRating() float
        +getPrecio() float
        +es_similar(otro) bool
    }

    class CatalogoJuegos {
        -list juegos
        +agregar_juego(juego) bool
        +buscar_por_titulo(titulo) Juego
        +filtrar_por_genero(genero) list
        +obtener_top_n(n) list
    }

    CatalogoJuegos "1" o-- "*" Juego : almacena
```

```text
> Buscar elemento
Título: Minecraft

╔══════════════════════════════════════╗
║           🎬 CINEBOT                ║
╠══════════════════════════════════════╣
║ Si te gustó Minecraft, quizás te     ║
║ interesen:                           ║
║                                      ║
║ 1. Stardew Valley                    ║
║ 2. Don't Starve                      ║
║ 3. Terraria                          ║
║                                      ║
╚══════════════════════════════════════╝

