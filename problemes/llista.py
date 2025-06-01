class Llista:
    # ----------------------------------------------------
    # Clase interna para definir los elementos de la lista.
    # Cada elemento de la lista será una instancia de _Node.
    class _Node:
        __slots__ = '_element', '_next', '_prev'  # Se usa __slots__ para mejorar la eficiencia al limitar los atributos.
        
        def __init__(self, prev, next, element=None):
            self._element = element  # Almacena el elemento (dato) del nodo.
            self._next = next        # Referencia al siguiente nodo.
            self._prev = prev        # Referencia al nodo anterior.
    # ----------------------------------------------------
    
    def __init__(self):
        # Se crea un nodo centinela, que no almacena dato (element=None) y sirve como marcador de inicio y fin.
        self.__sentinella = self._Node(None, None)
        # El nodo centinela se autorreferencia para poder detectar los extremos de la lista.
        self.__sentinella._next = self.__sentinella
        self.__sentinella._prev = self.__sentinella
        # El cursor se usa para marcar la posición actual en la lista.
        self.__cursor = self.__sentinella
        # Contador de elementos (excluyendo el nodo centinela).
        self.__n = 0

    # Retorna el número de elementos en la lista.
    def mida(self):
        return self.__n

    # Retorna True si la lista está vacía.
    def buida(self):
        return self.__n == 0

    # Comprueba si el cursor está en el primer elemento (después del centinela).
    def is_at_front(self):
        return self.__cursor == self.__sentinella._next
  
    # Comprueba si el cursor está al final de la lista (en el centinela).
    def is_at_end(self):
        return self.__cursor == self.__sentinella

    # Mueve el cursor una posición hacia atrás.
    # Pre: El cursor no debe estar en el primer elemento.
    def move_backward(self):
        assert not self.is_at_front()  # Aseguramos que no estemos en el inicio.
        self.__cursor = self.__cursor._prev

    # Mueve el cursor una posición hacia adelante.
    # Pre: El cursor no debe estar en el centinela (final).
    def move_forward(self):
        assert not self.is_at_end()  # Aseguramos que no estemos en el final.
        self.__cursor = self.__cursor._next

    # Mueve el cursor al primer elemento de la lista.
    def move_to_front(self):
        self.__cursor = self.__sentinella._next

    # Mueve el cursor al final de la lista (al nodo centinela).
    def move_to_end(self):
        self.__cursor = self.__sentinella

    # Retorna el elemento referenciado por el cursor.
    # Pre: El cursor no debe estar en el centinela.
    def front(self):
        assert not self.is_at_end()  # Verifica que el cursor esté en un nodo válido (no centinela).
        return self.__cursor._element

    # Inserta el elemento x antes de la posición del cursor.
    def insert(self, x):
        # Se crea un nuevo nodo cuyo nodo siguiente es el actual cursor y el nodo anterior es el que precede al cursor.
        p = self._Node(self.__cursor._prev, self.__cursor, x)
        # Se actualiza el puntero _next del nodo anterior para que apunte al nuevo nodo.
        self.__cursor._prev._next = p
        # Se actualiza el puntero _prev del nodo actual (cursor) para que apunte al nuevo nodo.
        self.__cursor._prev = p
        # Se incrementa el contador de elementos.
        self.__n += 1
        return self

    # Elimina el elemento referenciado por el cursor y avanza el cursor una posición.
    def erase(self):
        assert not self.is_at_end()  # Pre: El cursor no debe estar en el centinela.
        p = self.__cursor  # Nodo a eliminar.
        # Se reestablecen los punteros de los nodos adyacentes, saltando el nodo p.
        p._next._prev = p._prev
        p._prev._next = p._next
        # Se mueve el cursor al siguiente nodo.
        self.__cursor = p._next
        # Se decrementa el contador de elementos.
        self.__n -= 1

    # Invierte la lista de manera destructiva (modifica la lista original).
    def reverse(self):
        if not self.buida():
            # Empezamos con el nodo centinela.
            to_change = self.__sentinella
            # Simula un do...while: primero se invierten los punteros del centinela.
            next_to_change = to_change._next
            # Intercambia los punteros _prev y _next.
            to_change._prev, to_change._next = to_change._next, to_change._prev
            to_change = next_to_change
            # Recorre el resto de la lista hasta volver al centinela.
            while not to_change == self.__sentinella:
                next_to_change = to_change._next
                to_change._prev, to_change._next = to_change._next, to_change._prev
                to_change = next_to_change

    # Representación en forma de cadena de la lista.
    def __str__(self):
        s = ''
        # Se posiciona el cursor al inicio.
        self.move_to_front()
        # Se recorre la lista hasta llegar al centinela.
        while not self.is_at_end():
            s += str(self.front())
            self.move_forward()
        return s

    # Aplica la función f a cada elemento de la lista, creando una nueva lista con los resultados.
    def transform(self, f):
        l = Llista()  # Nueva lista donde se guardarán los elementos transformados.
        p = self.__sentinella._next
        # Recorre cada nodo hasta volver al centinela.
        while p != self.__sentinella:
            l.insert(f(p._element))
            p = p._next
        return l

    # Crea una nueva lista filtrando los elementos que cumplen con la condición dada por la función f.
    def filter(self, f):
        l = Llista()  # Nueva lista para almacenar los elementos filtrados.
        p = self.__sentinella._next
        while p != self.__sentinella:
            if f(p._element):  # Si el elemento cumple la condición, se inserta en la nueva lista.
                l.insert(p._element)
            p = p._next
        return l

    # Reduce (acumula) los elementos de la lista aplicando la función f secuencialmente, iniciando con x0.
    def reduce(self, x0, f):
        x = x0
        p = self.__sentinella._next
        while p != self.__sentinella:
            x = f(x, p._element)  # Se acumula el resultado.
            p = p._next
        return x

    # Permite iterar sobre la lista usando el protocolo de iteradores de Python.
    def __iter__(self):
        self.move_to_front()  # Se inicia la iteración desde el principio.
        return self

    # Define el siguiente elemento en la iteración.
    def __next__(self):
        if self.is_at_end():
            raise StopIteration  # Termina la iteración si se llega al centinela.
        else:
            resultat = self.front()  # Obtiene el elemento actual.
            self.move_forward()      # Avanza el cursor.
            return resultat
        
    # Método especial que intercala los elementos de la lista actual con los de otra lista pasada como argumento.
    # Coloca los elementos de self en las posiciones impares, y los de llista en las posiciones pares.
    def trenar(self, llista):
        self.move_to_front()   # Posiciona el cursor al inicio de la lista actual.
        llista.move_to_front() # Posiciona el cursor al inicio de la otra lista.
        # Mientras la lista actual no se termine (no se alcance el centinela)
        while not self.is_at_end():
            # Inserta el primer elemento de llista antes del cursor de self.
            self.insert(llista.front())
            # Elimina ese elemento de llista.
            llista.erase()
            # Avanza el cursor en self para dejar espacio al siguiente elemento de llista.
            self.move_forward()
            # Si aún hay elementos en llista, avanza su cursor.
            if not llista.is_at_end():
                llista.move_forward()
        return self
