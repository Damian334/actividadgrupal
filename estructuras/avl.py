class NodoAVL:
    def __init__(self, dato):
        self.dato = dato  # Objeto Videojuego
        self.izq = None
        self.der = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    def obtener_altura(self, nodo):
        return nodo.altura if nodo else 0

    def obtener_balance(self, nodo):
        return self.obtener_altura(nodo.izq) - self.obtener_altura(nodo.der) if nodo else 0

    def rotacion_derecha(self, z):
        y = z.izq
        T3 = y.der
        y.der = z
        z.izq = T3
        z.altura = 1 + max(self.obtener_altura(z.izq), self.obtener_altura(z.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        return y

    def rotacion_izquierda(self, z):
        y = z.der
        T2 = y.izq
        y.izq = z
        z.der = T2
        z.altura = 1 + max(self.obtener_altura(z.izq), self.obtener_altura(z.der))
        y.altura = 1 + max(self.obtener_altura(y.izq), self.obtener_altura(y.der))
        return y

    def insertar(self, juego):
        def _insertar(nodo, juego):
            if not nodo:
                return NodoAVL(juego)

            if juego < nodo.dato:
                nodo.izq = _insertar(nodo.izq, juego)
            elif juego > nodo.dato:
                nodo.der = _insertar(nodo.der, juego)
            else:
                return nodo  # No duplica si ya existe

            nodo.altura = 1 + max(self.obtener_altura(nodo.izq), self.obtener_altura(nodo.der))
            balance = self.obtener_balance(nodo)

            # Casos de rotación
            if balance > 1 and juego < nodo.izq.dato:
                return self.rotacion_derecha(nodo)
            if balance < -1 and juego > nodo.der.dato:
                return self.rotacion_izquierda(nodo)
            if balance > 1 and juego > nodo.izq.dato:
                nodo.izq = self.rotacion_izquierda(nodo.izq)
                return self.rotacion_derecha(nodo)
            if balance < -1 and juego < nodo.der.dato:
                nodo.der = self.rotacion_derecha(nodo.der)
                return self.rotacion_izquierda(nodo)

            return nodo

        self.raiz = _insertar(self.raiz, juego)

    def buscar(self, titulo):
        actual = self.raiz
        titulo_lower = titulo.lower()
        while actual:
            actual_titulo = actual.dato.titulo.lower() if hasattr(actual.dato, 'titulo') else str(actual.dato).lower()
            if actual_titulo == titulo_lower:
                return actual.dato
            elif titulo_lower < actual_titulo:
                actual = actual.izq
            else:
                actual = actual.der
        return None

    def inorder(self):
        res = []
        def _inorder(nodo):
            if nodo:
                _inorder(nodo.izq)
                res.append(nodo.dato)
                _inorder(nodo.der)
        _inorder(self.raiz)
        return res