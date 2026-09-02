# TP0: Lanzamiento y Requerimientos — RecomendadorJuegos

**1. Propuesta del Sistema**
* **Nombre del Proyecto:** RecomendadorJuegos
* **Dominio:** Videojuegos y Deportes Electrónicos
* **Justificación:** Se trabaja con un catálogo de videojuegos clasificado por títulos, géneros, desarrolladores, puntuaciones y mecánicas principales, permitiendo implementar búsquedas, rankings y grafos de afinidad.
* **Problema a Resolver:** Los usuarios que terminan o se saturan de un título deportivo o de acción no saben qué alternativa similar jugar según sus preferencias de físicas, modos de juego o licencias.
* **Usuario Objetivo:** Jugadores que buscan descubrir títulos afines a sus sagas favoritas (ej. simuladores deportivos, carreras o estrategia).

**2. Requerimientos Funcionales (RF)**
* **RF01 (Buscar):** El sistema debe permitir buscar un videojuego por su título exacto o parcial.
* **RF02 (Listar):** El sistema debe mostrar el listado completo de los juegos registrados en el catálogo.
* **RF03 (Filtrar):** El sistema debe permitir filtrar el catálogo por un género específico (ej. Deportes, Carreras, RPG).
* **RF04 (Ranking):** El sistema debe calcular y mostrar el Top N de juegos mejor valorados por el público.
* **RF05 (Recomendar):** El sistema debe sugerir alternativas basadas en coincidencias de desarrollador, género o mecánicas compartidas.

**3. Requerimientos No Funcionales (RNF)**
* **RNF01:** La aplicación funcionará exclusivamente en interfaz de línea de comandos (Terminal).
* **RNF02:** Los datos de cada `Juego` deberán protegerse con encapsulamiento estricto (`_atributo`).

**4. Ejemplo de Interacción (Salida Esperada)**

========================================
    ⚽ RECOMENDADOR JUEGOS — TERMINAL
========================================
Opción seleccionada: 1 (Buscar juego)
Ingrese el título: FIFA

╔══════════════════════════════════════════╗
║          RECOMENDADOR JUEGOS             ║
╠══════════════════════════════════════════╣
║ Si te gustó FIFA, quizás te interesen:   ║
║                                          ║
║ 1. Football Manager 2024       ⭐ 8.9     ║
║ 2. eFootball 2024              ⭐ 7.5     ║
║ 3. Rocket League               ⭐ 8.6     ║
╚══════════════════════════════════════════╝