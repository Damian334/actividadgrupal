# Casos de uso

## Caso de uso: Buscar videojuego

- **Actor**: Usuario

- **Precondición**: el catálogo está cargado.

- **Flujo principal**:
  1. El usuario selecciona la opción "Buscar videojuego".
  2. El sistema pide el título.
  3. El usuario ingresa el título.
  4. El sistema busca el videojuego sin distinguir mayúsculas y minúsculas.
  5. El sistema muestra el videojuego encontrado.

- **Flujo alternativo**: si no se encuentra el videojuego, el sistema informa que no existe.

## Caso de uso: Explorar por género

- **Actor**: Usuario

- **Precondición**: el catálogo está cargado.

- **Flujo principal**:
  1. El usuario selecciona la opción "Explorar por género".
  2. El sistema solicita un género.
  3. El usuario ingresa el género.
  4. El sistema busca los videojuegos que pertenecen a ese género.
  5. El sistema muestra los resultados.

- **Flujo alternativo**: si no existen videojuegos de ese género, el sistema informa que no se encontraron resultados.

## Caso de uso: Ver Top 10 mejores

- **Actor**: Usuario

- **Precondición**: el catálogo está cargado.

- **Flujo principal**:
  1. El usuario selecciona la opción "Ver Top 10 mejores".
  2. El sistema ordena los videojuegos según su rating, de mayor a menor.
  3. El sistema muestra los 10 videojuegos con mayor rating.

## Caso de uso: Ver videojuegos relacionados

- **Actor**: Usuario

- **Precondición**: el catálogo está cargado.

- **Flujo principal**:
  1. El usuario selecciona la opción "Ver videojuegos relacionados".
  2. El sistema solicita el título de un videojuego.
  3. El usuario ingresa el título.
  4. El sistema busca el videojuego.
  5. El sistema busca otros videojuegos que tengan el mismo género.
  6. El sistema muestra los videojuegos relacionados.

- **Flujo alternativo**: si el videojuego no existe o no se encuentran videojuegos relacionados, el sistema informa que no se encontraron resultados.

## Caso de uso: Ver alternativas del desarrollador

- **Actor**: Usuario

- **Precondición**: el catálogo está cargado.

- **Flujo principal**:
  1. El usuario selecciona la opción "Ver alternativas del desarrollador".
  2. El sistema solicita el título de un videojuego.
  3. El usuario ingresa el título.
  4. El sistema busca el videojuego.
  5. El sistema identifica su desarrollador.
  6. El sistema busca otros videojuegos del mismo desarrollador.
  7. El sistema muestra las alternativas encontradas.

- **Flujo alternativo**: si el videojuego no existe o no hay otros videojuegos del mismo desarrollador, el sistema informa que no se encontraron alternativas.