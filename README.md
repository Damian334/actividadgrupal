# Presentacion
Este es un trabajo practico integrador de la catedra de Estructura de Datos de la carrera de Tecnicatura en Programación de la Universidad Nacional Guillermo Brown.

## Integrantes
Los integrantes de este proyecto son:
- Agustin Jerez
- Jose Estigarribia
- Damian Frontini

## GameBot
En este trabajo se presenta GameFinderBot un asistente virtual que recomienda videojuegos al usuario, realizado mediante el lenguaje de Python.

## Estado
- TP0: completado
- TP1:

## Arquitectura del Sistema

El proyecto sigue una estructura modular orientada a objetos que separa responsabilidades en distintas capas:

* **modelos/juego.py:** Define la entidad `Juego` aplicando encapsulamiento estricto mediante atributos protegidos (`_atributo`) y acceso de lectura controlado por `@property`.
* **modelos/catalogo.py:** Contiene la lógica de negocio para la administración del catálogo, búsquedas y filtrados de la colección.
* **datos/juegos.json:** Archivo de persistencia que almacena el dataset inicial de videojuegos en formato JSON.
* **ui/terminal.py:** Gestiona el menú interactivo en consola y la interacción con el usuario.
* **main.py:** Punto de entrada que carga los datos de inicio e inicializa la aplicación.

## Requisitos e Instalación

### Requisitos previos
* Python 3.8 o superior

### Instrucciones de ejecución

1. Clonar el repositorio o posicionarse en la carpeta raíz del proyecto:
   ```bash
   cd TrabajoPracticoVideojuegos

## Diagrama de Clases (UML)

```mermaid
classDiagram
    class Juego {
        -_id: int
        -_titulo: str
        -_genero: str
        -_desarrollador: str
        -_rating: float
        -_precio: float
        +id: int
        +titulo: str
        +genero: str
        +desarrollador: str
        +rating: float
        +precio: float
    }

    class CatalogoJuegos {
        -_juegos: list
        +cargar_desde_json(ruta_archivo)
        +agregar_juego(juego)
        +listar_todos()
        +buscar_por_titulo(titulo)
        +filtrar_por_genero(genero)
    }

    class MenuTerminal {
        -_catalogo: CatalogoJuegos
        +ejecutar()
    }

    CatalogoJuegos "1" *-- "*" Juego : contiene
    MenuTerminal "1" --> "1" CatalogoJuegos : usa
