# Análisis TP3 — Árbol Binario de Búsqueda


## 1. ¿Qué resolvimos?
Incorporamos un **árbol binario de búsqueda (BST)** para resolver la
búsqueda por [atributo elegido, ej: título] de forma más eficiente.


## 2. Clave de ordenamiento
[Explicar por qué ordenamos por ese atributo. Ej: "El usuario busca por
título, así que ordenamos por título para que la búsqueda sea directa."]


## 3. Prueba del árbol
Acá dejamos la salida de `python algoritmos/probar_bst.py`:
[Preuba de funcionamiento del arbol vinario] (docs\capturas\Test-arbol-binario.jpg)


## 4. Comparación de tiempos
Este punto lo dejamos en blanco ya que esta parte del trabajo no se realizo


## 5. Análisis de complejidad
- **Búsqueda secuencial:** O(n). Recorre toda la lista en el peor caso.
- **Búsqueda binaria:** O(log n) pero exige lista ordenada (ordenar cuesta O(n log n) una s
- **Búsqueda en árbol:** O(log n) promedio si el árbol está balanceado;
O(n) en el peor caso si está degenerado (como una lista).
- **Inserción en árbol:** O(log n) promedio, O(n) peor caso.
- **Recorridos (inorder, preorder, postorder):** O(n), porque visitan cada nodo 1 vez.


## 6. Conclusión
[Con cuál nos quedamos y por qué. Ej: "Con 100.000 elementos la secuencial
tarda X ms y el árbol Y ms. El árbol conviene para búsquedas frecuentes;
el costo de construir el árbol se paga una sola vez."]


## 7. Errores o dudas que tuvimos
[Si tuvieron algún problema y cómo lo resolvieron. Suma puntos mostrarlo.]