from operator import lt, gt

class Heap:
    def __init__(self, items=[], cmp=lt):
        """
        Crea un heap a partir d'una llista d'elements (items) i d'una funció de comparació (cmp).
        Per defecte, cmp és lt, així que es construeix un min-heap.
        """
        self.__cmp = cmp
        self.__heapify(items)

    @staticmethod
    def heapify(items, cmp=lt):
        """
        Mètode estàtic que crea un Heap a partir de la llista d'elements 'items' i el comparador 'cmp'.
        Retorna un Heap ja inicialitzat.
        """
        return Heap(items, cmp)

    def inserir(self, x):
        """
        Insereix l'element x al heap, mantenint la propietat d'heap.
        """
        self.__lst.append(x)
        self.__surar(len(self.__lst) - 1)
        
    def obtenir(self):
        """
        Extreu i retorna l'element amb la mínima clau (segons cmp) del heap.
        Pre: El heap no està buit.
        """
        assert not self.buit(), "El heap està buit."
        primer = self.__lst[1]
        darrer = self.__lst.pop()
        if len(self.__lst) > 1:
            self.__lst[1] = darrer
            self.__enfonsar(1)
        return primer  

    def buit(self):
        """
        Retorna True si el heap és buit (és a dir, només té l'element dummy en la posició 0).
        """
        return len(self.__lst) == 1  # recorda que __lst[0] és sempre None

    def mida(self):
        """
        Retorna la mida (nombre d'elements) del heap.
        """
        return len(self.__lst) - 1

    # Mètodes privats

    def __heapify(self, ll=[]):
        """
        Inicialitza el heap amb la llista d'elements 'll'. El primer element de __lst és dummy.
        """
        self.__lst = [None]  # Dummy a la posició 0
        for e in ll:
            self.__lst.append(e)
        darrer_index = len(self.__lst) - 1
        for i in range(darrer_index // 2, 0, -1):
            self.__enfonsar(i)

    def __surar(self, i):
        """
        Mètode recursiu per “surar” l'element a la posició i si viola la propietat d'heap.
        """
        if i > 1 and self.__cmp(self.__lst[i], self.__lst[i // 2]):
            self.__lst[i], self.__lst[i // 2] = self.__lst[i // 2], self.__lst[i]
            self.__surar(i // 2)

    def __enfonsar(self, i):
        """
        Mètode recursiu per “enfonsar” l'element a la posició i si viola la propietat d'heap.
        """
        n = len(self.__lst) - 1
        c = 2 * i  # fill esquerre
        if c <= n:
            if c + 1 <= n and self.__cmp(self.__lst[c + 1], self.__lst[c]):
                c += 1  # triem el fill amb la clau més petita
            if self.__cmp(self.__lst[c], self.__lst[i]):
                self.__lst[i], self.__lst[c] = self.__lst[c], self.__lst[i]
                self.__enfonsar(c)
