from collections import namedtuple
Element = namedtuple("Element", ["clau", "valor"])


class Diccionari:
    def __init__(self):
        self._M = 500
        self._taula = self._M * [None] 
        for i in range(self._M):
            self._taula[i] = []
        self._n = 0 # Nombre d'elements emmagatzemats


    def buit(self):
        for element in self.taula:
            if element is not None:
                return False
        return True
    
    def hash(self, clau):
        return hash(clau) % self._M


    def assigna(self, clau, info):
        pos = self.hash(clau)
        i = self.posicio(pos, clau)
        L = self._taula[pos]

        if i == None:
            L.append(Element(clau, info))
            self._n += 1
        else:
            element = L[i]
            L[i] = element._replace(valor = info)



    def valor(self, clau):
        pos = self.hash(clau)
        L = self._taula[pos]

        for element in L:
            if element.clau == clau:
                return element.valor
        return None


    def elimina(self, clau):
        pos = self.hash(clau)
        L = self._taula[pos]
        for i in range(len(L)):
            if L[i].clau == clau:
                del L[i]
                self._n -= 1
            return
        return None


    def mida(self):
        return self._n

    def troba_minim(self):
        minim = None
        for ll in self._taula:
            for element in ll:
                if minim is None or element.clau < minim.clau:
                    minim = element
        return minim


 
    def troba_maxim(self):
        maxim = None
        for ll in self._taula:
            for element in ll:
                if maxim is None or element.clau > maxim.clau:
                    maxim = element
        return maxim
    

    def elements(self):
        elements = []
        for ll in self._taula:
            elements.extend(ll)
        return elements


    def posicio(self, pos, clau):
        L = self._taula[pos]
        for i in range(len(L)):
            if L[i].clau == clau:
                return i
        return None