class Grafo:
    def __init__(self):
        self.adyacencias = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencias:
            self.adyacencias[vertice] = []

    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        if destino not in self.adyacencias[origen]:
            self.adyacencias[origen].append(destino)
        if origen not in self.adyacencias[destino]:
            self.adyacencias[destino].append(origen)

    def bfs(self, inicio):
        if inicio not in self.adyacencias:
            return []
        visitados = set()
        cola = [inicio]
        resultado = []
        visitados.add(inicio)
        while cola:
            actual = cola.pop(0)
            resultado.append(actual)
            for vecino in self.adyacencias[actual]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return resultado