# GameBot
Es el asiste virtual que se encargara de buscar, explorar y recomendar distintos videojuegos a partir de caracteristicas y relaciones con titulos que hayas jugado y te gustaran.

## Dominio elegido
Elegimos los videojuegos ya que tiene una gran base de información, como nombres, generos, puntuaciones, plataformas y relaciones entre titulos.
Además es algo que a todos nos gusta ya que es un ambito muy popular hoy en día, uno si tiene una computadora, una consola o incluso en un celular, va a descargar juegos para entrenerse y pasar el rato.

## Problema que resuelve
Los jugadores pueden tener un problema al elegir que jugar despues de haber completado un videojuegos que los engancho demaciado.
Es por eso que GameBot busca solucionar este problema, ofreciendo recomendaciones a partir de videojuegos conocidos y sus características.

## Usuario objetivo
El sistema esta dirigido principalmente a los jugadores que quieren descubrir nuevos videojuegos que los entretengan y sean similares a otros que ya hayan jugado.

## Funciones iniciales
| ID | Funcionalidad |
|---|---|
| F1 | Buscar un videojuego por su nombre |
| F2 | Listar videojuegos por género |
| F3 | Mostrar el Top 10 de videojuegos mejor puntuados |
| F4 | Recomendar videojuegos relacionados con uno seleccionado |
| F5 | Ver videojuegos de la misma saga a partir de uno seleccionado |

## Ejemplo de uso

```text
========================================
              GAMEBOT
========================================

1. Buscar videojuego
2. Explorar por género
3. Ver Top 10 mejores
4. Ver videojuegos relacionados
5. Ver saga de videojuegos
0. Salir

Selecciona una opción: 4

Ingrese un videojuego: Minecraft

Seleccionando videojuegos a recomendar....

Juegos relacionados a Minecraft que te pueden justar:

- Stardew Valley
- Terraria
- Starbound
- Don't Starve
- Don't Starve Together
```
## Requerimientos
| ID | Requerimiento | Tipo |
|---|---|---|
| RF01 | El sistema debe permitir buscar un videojuego por nombre | Funcional |
| RF02 | El sistema debe permitir listar videojuegos por género | Funcional |
| RF03 | El sistema debe mostrar los 10 videojuegos mejor puntuados | Funcional |
| RF04 | El sistema debe mostrar videojuegos relacionados con un videojuego seleccionado | Funcional |
| RF05 | El sistema debe mostar otros videojuegos de la misma saga que el videojuego seleccionado | Funcional |

## Fuera de alcance (por ahora)
- No hay autenticación ni perfiles de usuario.
- No se crearán perfiles personalizados.
- No se almacenarán preferencias personales de los usuarios.