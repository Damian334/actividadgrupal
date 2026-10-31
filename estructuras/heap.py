class MaxHeapSimple:
    def __init__(self):
        # La lista representa un arbol binario completo
        self.juegos = []

    def insertar(self, un_juego):
        # 1. Agregamos el juego al final de todo
        self.juegos.append(un_juego)
        # 2. Hacemos que flote si es mayor que su padre
        self._flotar(len(self.juegos) - 1)

    def _flotar(self, indice):
        # Mientras no estemos en la raíz y el hijo sea mayor que el padre
        while indice > 0:
            indice_padre = (indice - 1) // 2
            
            # Comparamos el rating del juego actual con el de su padre
            if self.juegos[indice].rating > self.juegos[indice_padre].rating:
                # Intercambiamos (Swap)
                self.juegos[indice], self.juegos[indice_padre] = self.juegos[indice_padre], self.juegos[indice]
                # Subimos el indice para seguir chequeando hacia arriba
                indice = indice_padre
            else:
                break # Si ya es menor, terminó 

    def extraer_maximo(self):
        if not self.juegos:
            return None
        if len(self.juegos) == 1:
            return self.juegos.pop()

        # Guardamos el max (la raiz) para retornarlo
        maximo = self.juegos[0]
        
        # Pasamos el ultimo elemento a la raiz y achicamos la lista
        self.juegos[0] = self.juegos.pop()
        
        # Hundimo desde la raíz (indice 0)
        self._hundir(0)
        
        return maximo

    def _hundir(self, indice):
        largo = len(self.juegos)
        
        while True:
            hijo_izq = 2 * indice + 1
            hijo_der = 2 * indice + 2
            mayor = indice

            # Si el hijo izquierdo existe y es mayor que el actual mayor
            if hijo_izq < largo and self.juegos[hijo_izq].rating > self.juegos[mayor].rating:
                mayor = hijo_izq

            # Si el hijo derecho existe y es mayor que el actual mayor
            if hijo_der < largo and self.juegos[hijo_der].rating > self.juegos[mayor].rating:
                mayor = hijo_der

            # Si el mayor sigue siendo el padre, ya encontramos su lugar
            if mayor == indice:
                break

            # Si no, intercambiamos y seguimos bajando
            self.juegos[indice], self.juegos[mayor] = self.juegos[mayor], self.juegos[indice]
            indice = mayor
    def obtener_top_n(self, n=10):
        import copy
        # Hacemos una copia profunda del heap para extraer los máximos 
        # sin vaciar ni destruir el heap original que usa la app.
        heap_copia = copy.deepcopy(self)
        resultado = []
        
        while heap_copia.juegos and len(resultado) < n:
            maximo = heap_copia.extraer_maximo()
            if maximo:
                resultado.append(maximo)
                
        return resultado