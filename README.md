# ⚽ RecomendadorJuegos — Sistema de Recomendación en Python

> Proyecto integrador incremental para la materia **Estructuras de Datos** (UNAB).

## 💡 Sobre el Proyecto
¿Terminaste un juego y no sabés qué jugar después? **RecomendadorJuegos** es una aplicación de terminal diseñada para buscar, clasificar y recomendar títulos según tus géneros, valoraciones y desarrolladores preferidos. 

Elegimos el dominio de videojuegos tomando como punto de partida títulos deportivos (como *FIFA*, *eFootball* o *Football Manager*) para construir relaciones complejas entre datos reales, evolucionando la arquitectura desde POO básica hasta Árboles, Heaps y Grafos.

## 👥 Equipo de Desarrollo
* **José** — Implementación del dominio (`modelos/`), estructura base de objetos y Git workflow.
* **Damian** — Interfaz de usuario en terminal (`ui/`) y diseño de menú.
* **Agustin** — Carga y gestión de datasets (`datos/`) y requerimientos.

## 🏗️ Decisiones de Diseño y Arquitectura
Para mantener el código ordenado y escalable, dividimos la solución en capas independientes:

* **`modelos/juego.py`**: Clase entidad con encapsulamiento estricto (`_atributo`) que resguarda la información base (título, rating, género, desarrollador).
* **`modelos/catalogo.py`**: Lógica de negocio encargada de búsquedas, filtrados y ordenamiento.
* **`ui/terminal.py`**: Capa de presentación desacoplada; interactúa con el usuario sin conocer la lógica interna.
* **`datos/`**: Almacenamiento persistente del catálogo.

## 🚀 Inicio Rápido
1. Clonar el repositorio y posicionarse en la raíz:
   ```bash
   git clone https://github.com/Damian334/actividadgrupal.git
   cd TrabajoPracticoVideojuegos