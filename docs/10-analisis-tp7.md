### 7) Análisis y Propuesta de Implementación de Grafos (TP7)

Se evaluó la incorporación de una estructura de **Grafo No Dirigido** para modelar y optimizar las recomendaciones de videojuegos relacionados y alternativas de desarrolladores dentro del sistema GAMeBOT.

#### ¿Por qué se propone incorporar un Grafo?
Las estructuras previas (BST, Árbol General y Max-Heap) resolvieron de manera eficiente las búsquedas por clave, las jerarquías por género y los rankings por prioridad. Sin embargo, las relaciones de similitud entre videojuegos son de naturaleza **red**, donde un juego puede relacionarse con múltiples otros por género, desarrollador o mecánicas de manera cruzada. 

Implementar un grafo permite mapear estas conexiones de forma explícita mediante vértices y aristas, evitando recorrer linealmente todo el catálogo ante cada consulta de relación.

#### Comparación de Alternativas para Relaciones

| Métrica / Aspecto | Filtrado Lineal en Catálogo | Estructura de Grafo (Adyacencia) |
| :--- | :--- | :--- |
| **Modelado de Red** | Implícito (evalúa condiciones en tiempo de ejecución) | **Explícito** (conexiones directas en memoria) |
| **Complejidad de búsqueda** | $O(n)$ | **$O(V + E)$** |
| **Algoritmos de recorrido** | Ninguno (filtrado básico) | **BFS (Amplitud) y DFS (Profundidad)** |
| **Mantenimiento** | Bajo acoplamiento, alto costo temporal de consulta | Mayor estructura inicial, optimización de consultas en red |

#### Conclusión de Diseño
El grafo complementa perfectamente a las estructuras anteriores. Mientras el árbol AVL resuelve el acceso rápido y el Max-Heap gestiona el Top 10, el **Grafo** actúa como la red de descubrimiento, permitiendo aplicar recorridos en amplitud (BFS) para sugerir títulos cercanos en afinidad al usuario.