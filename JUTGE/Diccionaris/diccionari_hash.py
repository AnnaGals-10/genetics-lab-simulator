# Implementació senzilla, sense rehashing, d'una taula
# de dispersió amb separate chaining
# Només les operacions assigna / elimina / valor / mida

from collections import namedtuple
Element = namedtuple("Element", ["clau", "valor"])

class Diccionari:

    def __init__(self):
        self._M = 1099
        # Taula de dispersió: cada item en aquesta taula serà una
        # llista d'elements (clau, valor)
        self._taula = self._M * [None] 
        for i in range(self._M):
            self._taula[i] = []
        self._n     = 0    # nombre d'elements emmagatzemats

    def buit(self):
        return self._n == 0

    def assigna(self, clau, info):
        """
        Assigna informació a una clau. Si la clau ja hi és dins
        el diccionari, la informació és modificada.
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = hash(clau) % len(self._taula)    # la funció 'hash' ens la dona Python
        p = self._posicio(clau, h)
        if p != None:
            elem = self._taula[h][p]
            self._taula[h][p] = elem._replace(valor=info) # Genera NOU element
        else:
            self._taula[h].append(Element(clau, info))
            self._n += 1
        alfa = self._n / self._M
        if alfa >= 1:
            self._rehash()

    def valor(self, clau):
        """
        retorna el valor associat a una clau, None si la clau no hi és
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = hash(clau) % len(self._taula)
        p = self._posicio(clau, h)
        return self._taula[h][p].valor if p is not None else None

    def elimina(self, clau):
        """
        Elimina la parella (clau, valor) del diccionari. Si la clau no pertany al
        diccionari, res canvia.
        cas pitjor: Theta(n). cas mitjà: Theta(1+n/M).
        """
        h = hash(clau) % len(self._taula)
        p = self._posicio(clau, h)
        if p != None:
            self._taula[h][p] = self._taula[h][-1]
            self._taula[h].pop()
            self._n -= 1

    def mida(self):
        return self._n

    def troba_minim(self):
        # Cal buscar-lo entre tots els elements. Cost Theta(n)
        minim = None
        for ll in self._taula:
            for e in ll:
                if minim is None or e.clau < minim.clau:
                    minim = e
        return minim

    def troba_maxim(self):
        # Cal buscar-lo entre tots els elements. Cost Theta(n)
        maxim = None
        for ll in self._taula:
            for e in ll:
                if maxim is None or e.clau > maxim.clau:
                    maxim = e
        return maxim

    def elements(self):
        resultat = []
        for ll in self._taula:
            for e in ll:
                resultat.append(e)
        return resultat

    def __str__(self):
        s = ''
        principi = True
        for ll in self._taula:
            for e in ll:
                if principi:
                    principi = False
                else:
                    s += " -- "
                s += f"{e.clau} : {e.valor}"
        return s
    
    # ------------------ mètode privat
    
    def _posicio(self, clau, h):
        """
        Retorna la posició de la clau a la llista      
        d'elements de la posició h, o None si no el troba.
        """
        l = self._taula[h]
        for i in range(len(l)):
            if l[i].clau == clau:
                return i
        return None

    def _rehash(self):
        elements = self.elements()
        self._M = 2*self._M # Modifiquem la mida de la taula.
        # Inicialitzem tot un altre cop
        self._taula = self._M * [None] 
        for i in range(self._M):
            self._taula[i] = []
        self._n = 0
        # re-posiciono les parelles (clau,valor)
        for e in elements:
            self.assigna(e.clau,e.valor)
            
      
