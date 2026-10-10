from collections import deque
class ArbolGeneral:from collections import deque

class NodoGeneral:
    def __init__(self, data):
        self.data = data
        self.hijos = []

class ArbolGeneral:
    def __init__(self):
        self.raiz = None

    def insertar_raiz(self, dato):
        if not self.raiz:
            self.raiz = NodoGeneral(dato)
        return self.raiz

    def agregar_hijo(self, padre_dato, hijo_dato):
        padre = self.buscar(padre_dato)
        if padre:
            nuevo_hijo = NodoGeneral(hijo_dato)
            padre.hijos.append(nuevo_hijo)
            return nuevo_hijo
        return None

    def buscar(self, dato):
        if not self.raiz:
            return None
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.data == dato:
                return actual
            for hijo in actual.hijos:
                cola.append(hijo)
        return None

    def amplitud(self):
        if not self.raiz:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.data)
            for hijo in actual.hijos:
                cola.append(hijo)
        return resultado

    def profundidad_preorder(self):
        resultado = []
        def _preorder(nodo):
            if nodo:
                resultado.append(nodo.data)
                for hijo in nodo.hijos:
                    _preorder(hijo)
        _preorder(self.raiz)
        return resultado
    def __init__(self):
        self.raiz = None

    def insertar_raiz(self, dato):
        if not self.raiz:
            self.raiz = NodoGeneral(dato)
        return self.raiz

    def agregar_hijo(self, padre_dato, hijo_dato):
        padre = self.buscar(padre_dato)
        if padre:
            nuevo_hijo = NodoGeneral(hijo_dato)
            padre.hijos.append(nuevo_hijo)
            return nuevo_hijo
        return None

    def buscar(self, dato):
        if not self.raiz:
            return None
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            if actual.data == dato:
                return actual
            for hijo in actual.hijos:
                cola.append(hijo)
        return None

    def amplitud(self):
        if not self.raiz:
            return []
        resultado = []
        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.data)
            for hijo in actual.hijos:
                cola.append(hijo)
        return resultado

    def profundidad_preorder(self):
        resultado = []
        def _preorder(nodo):
            if nodo:
                resultado.append(nodo.data)
                for hijo in nodo.hijos:
                    _preorder(hijo)
        _preorder(self.raiz)
        return resultado

    def profundidad_postorder(self):
        resultado = []

        def _postorder(nodo):
            if nodo:
                for hijo in nodo.hijos:
                    _postorder(hijo)
                resultado.append(nodo.data)

        _postorder(self.raiz)
        return resultado