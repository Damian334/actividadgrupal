### 6) Prueba del Max-Heap

Se realizó una prueba con el catálogo de videojuegos insertados de forma consecutiva dentro del `MaxHeapSimple`, evaluando su comportamiento para la generación del ranking Top 10 por rating.

Los resultados mostraron que, independientemente del orden de inserción de los videojuegos, la raíz de la lista interna (`índice 0`) mantuvo siempre al videojuego con la calificación más alta. Durante las extracciones sucesivas de la cima mediante el algoritmo de hundir (`_hundir`), la estructura se reorganizó automáticamente restaurando la propiedad de Max-Heap en cada paso.

#### Prueba de funcionamiento del Max-Heap
Se comprobó que la ejecución de `obtener_top_n(10)` devolvió correctamente los 10 videojuegos con mayor rating ordenados de forma decreciente. Asimismo, se verificó que el uso de `copy.deepcopy` al extraer el Top impidió la destrucción de la estructura principal que utiliza el sistema en ejecución.

---

### 7) Comparación de Lista Común vs Max-Heap

Se evaluó el costo computacional y comportamiento de mantener un ranking de prioridades utilizando una lista simple con reordenamiento frente al uso de un `Max-Heap`.

| Métrica / Operación | Lista común + `.sort()` | Max-Heap Binario |
| :--- | :--- | :--- |
| **Acceso al elemento máximo** | $O(n \log n)$ (tras ordenar toda la lista) | **$O(1)$** (siempre en la raíz) |
| **Inserción de un nuevo elemento** | $O(1)$ (append) | **$O(\log n)$** (vía flotar) |
| **Extracción del máximo** | $O(n)$ o $O(1)$ (si ya está ordenada) | **$O(\log n)$** (vía hundir) |
| **Uso de memoria adicional** | Mínimo ($O(1)$) | Mínimo (Arreglo contiguo $O(n)$ sin punteros) |
| **Reorganización en cambios** | Reordena todo el dataset | Reorganiza solo la altura $O(\log n)$ |

#### Conclusión del Max-Heap
El uso de `.sort()` sobre una lista requiere reordenar todo el catálogo completo cada vez que se consulta el ranking, lo cual resulta ineficiente a medida que crece el volumen de datos. En cambio, el `Max-Heap` permite acceder al videojuego con mayor calificación en tiempo constante $O(1)$ y reestructurar la jerarquía en $O(\log n)$ sin manipular elementos irrelevantes del catálogo.

---

### Integración del Max-Heap en el menú

Se integró la estructura `MaxHeapSimple` al flujo principal de la aplicación (`main.py`) y a la interfaz de consola (`ui/terminal.py`).

Durante la carga del archivo `juegos.json`, los videojuegos se insertan simultáneamente en el árbol AVL (búsqueda por título) y en el Max-Heap (ranking por rating).

El menú principal actualizó el comportamiento de la siguiente opción:
* **Opción 3 (Ver Top 10 mejores):** Delegó su funcionamiento al método `obtener_top_n(10)` de la instancia `MaxHeapSimple`, eliminando la dependencia del ordenamiento lineal del catálogo.

Se comprobó el funcionamiento de la opción 3 en la terminal, verificando que los videojuegos devueltos por la interfaz coinciden de forma exacta con los mayor puntuados en el dataset.