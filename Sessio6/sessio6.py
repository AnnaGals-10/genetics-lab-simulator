from collections import deque

class ArbreBinari:
    def __init__(self,v=None,esq=None,dre=None):
        #assert (v is None and left is None and right is None) or v is not None
        if v is None:
           self._root = None # Arbre buit
        else:
            l = esq._root if (esq is not None) else None # <== ATENCIÓ!!!
            r = dre._root if (dre is not None) else None # <== ATENCIÓ!!!
            self._root = self._Node(v, l, r) 

    def valor_arrel(self):
       return self._root._element

    def fill_esq(self):
       return self._node["fesq"]

    def fill_dre(self):
       return self._node["fdre"]

    def modificar_valor_arrel(self,v):
       #assert v is not None
        if not self.buit():
            self._node["v"] = v
        else:
            self._node = {"v": v, "fesq": ArbreBinari(), "fdre": ArbreBinari()}

    def modificar_fill_esq(self,esq):
       self._node = ("fesq")

    def modificar_fill_dre(self,dre):
       self._node = ("fdre")

    def buit(self):
          return self._node == None

    def fulla(self):
        if self.buit():
            return False
        return self.fill_esq().buit() and self.fill_dre().buit()
 
    def preordre(self):
        if self.buit():
            return[]
        else:
            return [self.valor_arrel()] + self.fill_esq().preordre() + self.fill_dre().preordre()

    def postordre(self):
        if self.buit():
            return[]
        else:
            return self.fill_esq().postordre() + self.fill_dre.postordre() + [self.valor_arrel()]

    def inordre(self):
        if self.buit():
            return[]
        else:
            return self.fill_esq().inordre + [self.valor_arrel()] + self.fill_dre().inordre

    def nivells(self):
        if self.buit():
            return[]
        else:
            resultat = []
            q = deque()
            q.append(self)
            while len(q) > 0:
                tt = q.popleft()
                resultat.append(tt.valor_arrel())
                if not tt.fill_esq().buit():
                    q.append(tt.fill_esq())
                if not tt.fill_dre().buit():
                    q.append(tt.fill_dre())
            return resultat
        
def inversio(t):
    if 
