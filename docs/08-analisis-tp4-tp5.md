### 4) Prueba del AVL

Se realizó una prueba con diez videojuegos insertados en orden alfabético, comparando el comportamiento de un BST con un árbol AVL.

Los resultados mostraron que el BST alcanzó una altura de 10, mientras que el AVL obtuvo una altura de 4. Esto demuestra que el AVL mantuvo una estructura más equilibrada mediante las rotaciones realizadas durante las inserciones.

[Preuba de funcionamiento del AVL ](docs\capturas\Prueba-avl.jpg)

También se comprobó que la búsqueda de Minecraft devolvió el videojuego correspondiente y que el recorrido inorder presentó los elementos en orden alfabético.

En cuanto a los tiempos de inserción, el BST tardó 0,000026 segundos y el AVL 0,000051 segundos en esta ejecución. Estos valores corresponden únicamente a la prueba realizada y no permiten establecer por sí solos cuál estructura tendrá mejor rendimiento con grandes cantidades de datos.

### 4) comparación de BST vs AVL

Se insertaron 10 videojuegos en orden alfabético para comparar el comportamiento del árbol binario de búsqueda (BST) y el árbol AVL.

| Métrica | BST común | AVL |
|---|---:|---:|
| Altura del árbol | 10 | 4 |
| Tiempo de inserción | 0.000026 s | 0.000051 s |
| Recorrido inorder | O(n) | O(n) |
| Complejidad de búsqueda en el peor caso | O(log n) | O(log n) |



### 5) Prueba del árbol general

Se realizó una prueba utilizando el catálogo compuesto por 15 videojuegos distribuidos en 9 géneros.

Se implementaron y ejecutaron los recorridos por amplitud (BFS), profundidad preorder y profundidad postorder. Los tres recorridos finalizaron correctamente y permitieron comprobar que la estructura organiza los videojuegos según su género y respeta el orden de visita correspondiente a cada algoritmo.

[Preuba de funcionamiento del arbol generl ](docs\capturas\Prueba-arbol-general.jpg)


### 5) Comparación entre AVL y árbol general

El árbol AVL y el árbol general permiten organizar y buscar datos, pero tienen características diferentes. El AVL es un árbol binario de búsqueda que se mantiene equilibrado mediante rotaciones, mientras que el árbol general permite organizar los elementos en una jerarquía con varios hijos por nodo.

| Operación | AVL | Árbol general |
|---|---|---|
| Inserción | O(log n) | O(1) |
| Búsqueda | O(log n) | O(n) |
| Recorrido inorder | O(n) | O(n) |
| Recorrido por amplitud | O(n) | O(n) |
| Altura en el peor caso | O(log n) | O(n) |

En conclusión, el AVL resulta conveniente para realizar búsquedas eficientes, ya que mantiene su altura equilibrada. En cambio, el árbol general es adecuado para representar relaciones jerárquicas. Por este motivo, ambas estructuras cumplen funciones diferentes y complementarias dentro del proyecto.

### Integración de las estructuras en el menu

Se integraron las estructuras de datos AVL y árbol general al proyecto para mejorar la búsqueda y permitir la exploración del catálogo por género.

El árbol AVL se utiliza en la opción 1 del menú para buscar videojuegos por título. El árbol general se utiliza en la opción 2 para explorar los videojuegos organizados según su género.

El menú principal mantiene las siguientes opciones:

1. Buscar videojuego.
2. Explorar por género.
3. Ver Top 10 mejores.
4. Ver videojuegos relacionados.
5. Ver alternativas del desarrollador.
0. Salir.

Las opciones de Top 10, videojuegos relacionados y alternativas del desarrollador continúan utilizando las funcionalidades del catálogo implementadas previamente.

Se comprobó el funcionamiento de las opciones del menú y se verificó que la búsqueda mediante el AVL y la exploración por género mediante el árbol general funcionaran correctamente.