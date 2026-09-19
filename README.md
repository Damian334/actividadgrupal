# Presentacion

Este es un trabajo practico integrador de la catedra de Estructura de Datos de la carrera de Tecnicatura en Programación de la Universidad Nacional Guillermo Brown.

## Integrantes

Los integrantes de este proyecto son:

- Agustin Jerez
- Jose Estigarribia
- Damian Frontini

## GAMeBOT

En este trabajo se presenta GAMeBOT, un asistente virtual que recomienda videojuegos al usuario, realizado mediante el lenguaje de Python.

## Estado

- TP0: completado
- TP1: Completado
- TP2: No realizado
- TP3: Completado

## Arquitectura del Sistema

El proyecto sigue una estructura modular orientada a objetos que separa responsabilidades en distintas capas:

- **modelos/juegos.py:** Define la clase `Videojuego`, que representa los videojuegos del sistema. Utiliza atributos privados y acceso mediante `@property`.
- **servicios/catalogo.py:** Contiene la lógica de negocio para administrar el catálogo de videojuegos, realizar búsquedas, filtrados, obtener el Top 10 y encontrar videojuegos relacionados o del mismo desarrollador.
- **datos/juegos.json:** Archivo que contiene el conjunto de datos inicial de videojuegos en formato JSON.
- **ui/terminal.py:** Gestiona el menú interactivo en consola y la interacción con el usuario.
- **main.py:** Punto de entrada que carga los datos e inicia la aplicación.
- **tests/test_catalogo.py:** Contiene las pruebas automatizadas de las operaciones del catálogo.

## Requisitos e Instalación

### Requisitos previos

- Python 3.8 o superior

No se requieren librerías externas.

## Ejecución

Para ejecutar el programa:

```bash
python main.py
```
## Pruebas
```bash
python -m unittest discover tests
```

## Muestras
![Preuba de funcionamiento del menu v1] (docs/capturas/Prueba-menu01.jpg)
![Preuba de funcionamiento del menu v2] (docs/capturas/Prueba-menu02.jpg)
![Preuba de funcionamiento del arbol vinario] (docs/capturas/Test-arbol-binario.jpg)
