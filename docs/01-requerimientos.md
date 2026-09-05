# GameFinderBot — Propuesta del Proyecto y Requerimientos (TP0)

## 1. Propuesta del Sistema y Dominio
* **Nombre del Proyecto:** GameFinderBot (RecomendadorJuegos)
* **Dominio Elegido:** Videojuegos y Deportes Electrónicos. Posee un amplio catálogo de información (títulos, géneros, desarrolladores, puntuaciones) ideal para aplicar estructuras de datos, algoritmos de búsqueda y filtrados.
* **Problema a Resolver:** Los jugadores que completan o se saturan de un videojuego suelen no saber qué alternativa similar jugar a continuación según sus preferencias de género, mecánicas o estilos.
* **Usuario Objetivo:** Jugadores que buscan descubrir nuevos títulos afines a sus sagas y juegos favoritos.

## 2. Requerimientos Funcionales (RF)
| ID | Requerimiento Funcional | Descripción |
|---|---|---|
| **RF01** | Buscar videojuego | Permitir la búsqueda de un juego por su título exacto o parcial. |
| **RF02** | Listar catálogo | Mostrar el listado completo de los juegos registrados en el sistema. |
| **RF03** | Filtrar por género | Filtrar el catálogo según un género específico (ej. Deportes, Acción, RPG). |
| **RF04** | Ranking (Top N) | Calcular y mostrar los videojuegos mejor valorados por el público. |
| **RF05** | Recomendar títulos | Sugerir alternativas basadas en coincidencias de desarrollador o género. |

## 3. Requerimientos No Funcionales (RNF)
| ID | Requerimiento No Funcional | Descripción |
|---|---|---|
| **RNF01** | Interfaz CLI | La aplicación funcionará exclusivamente en interfaz de línea de comandos (Terminal). |
| **RNF02** | Encapsulamiento | Los datos de la clase `Juego` deberán protegerse con encapsulamiento estricto (`_atributo`) y `@property`. |
| **RNF03** | Persistencia | El catálogo inicial se cargará dinámicamente desde un archivo `juegos.json`. |

## 4. Fuera de Alcance (Límites del MVP)
* No se implementará autenticación ni perfiles de usuario.
* No se almacenará historial de búsquedas ni preferencias guardadas.
* No se conectará a APIs externas en tiempo real.

## 5. Ejemplo de Interacción (Interfaz de Terminal)

```text
========================================
       GAMEFINDERBOT — TERMINAL
========================================
1. Listar catálogo completo
2. Buscar videojuego por título
3. Filtrar videojuegos por género
0. Salir

Seleccione una opción: 2
Ingrese el título a buscar: Minecraft

Resultados encontrados:
- Minecraft | Género: Aventura | Rating: 9.5 | Precio: $29.99