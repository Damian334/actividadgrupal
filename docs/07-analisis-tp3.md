# Análisis TP3 — Árbol Binario de Búsqueda


## 1. ¿Qué resolvimos?
Incorporamos un **árbol binario de búsqueda (BST)** para resolver la
búsqueda de videojuegos por su título de forma eficiente.


## 2. Clave de ordenamiento
Elegimos que el arbol ordene por **título** porque es una de las funciones
principales que tiene GAMeBOT, la busqueda de videojurgos por su titulo. De esta forma, 
podemos utilizar el título como clave para recorrer el árbol y encontrar el videojuego buscado.


## 3. Prueba del árbol
Acá dejamos la salida de `python algoritmos/probar_bst.py`:

[Preuba de funcionamiento del arbol vinario] (docs\capturas\Test-arbol-binario.jpg)


## 4. Comparación de tiempos
Este punto lo dejamos en blanco ya que esta parte del trabajo no se realizo.


## 5. Análisis de complejidad
Esta sección tambien lo dejamos en blanco por los mismos motivos.


## 6. Conclusión
En este trabajo incorporamos un árbol binario de búsqueda (BST) a GAMeBOT para mejorar la forma 
en que se realizan las búsquedas de videojuegos por título. Aprendimos a insertar elementos en el árbol,
buscar utilizando una clave y recorrerlo mediante los recorridos inorder, preorder y postorder.

## 7. Errores o dudas que tuvimos
Un problema que tuvimos fue durante la prueba de **probar_bts.py** cuando queriamos ejecutar el programa 
python "algoritmos/probar_bst.py" en el bash ya que no encontraba la carpeta "estructuras".
[muestra del errror] (docs/capturas/muestra-error.png)

Como no lograbamos encontrarle la vuela al asunto le consultamos al chatbot y nos recomendo que 
agregaramos al archivo **probar_bst.py** el siguiente codigo:

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Estas son unas instrucciones para que python pudiera encontrar la capeta principal del proyecto  y, 
de esta forma, importar correctamente `ArbolBST`.