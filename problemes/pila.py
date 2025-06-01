class Pila:

    # ----------------------------------------------------
    # Classe interna per definir els elements de la pila:
    # Cada element de la pila serà una instància de _Node
    class _Node:
        __slots__ = '_element', '_next' 
        
        def __init__(self, element, next):
            self._element = element 
            self._next = next              
    # ------------------------------------------

    def __init__(self):
        self._cap = None
        self._mida = 0

    def buida(self):
        return self._mida == 0
 
    def mida(self):
        return self._mida

    def push(self, e):
        self._cap = self._Node(e, self._cap)
        self._mida += 1
        return self
        
    def cim(self):
        # Pre: La pila no és buida
        return (self._cap)._element

    def pop(self):
        # Pre: La pila no és buida
        resposta = (self._cap)._element
        self._cap = (self._cap)._next 
        self._mida -= 1
        return resposta
    
