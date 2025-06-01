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
       l = ArbreBinari()
       l._root = self._esq._root
       return l

    def fill_dre(self):
       r = ArbreBinari()
       r._root = self._dre._root
       return r

    def modificar_valor_arrel(self,v):
       #assert v is not None
        if not self.buit():
            self._root._element = v
        else:
            self._root = self._Node(v)

    def modificar_fill_esq(self,esq):
       if not self._buit:
          self.fill_esq = esq
       else:
          self.fill_esq = self._Node(esq)
          
    def modificar_fill_dre(self,dre):
       if not self._buit:
          self.fill_dre = dre
       else:
          self.fill_dre = self._Node(dre)

    def buit(self):
       return self._buit
    
    def fulla(self):
       pass
 """
 retorna True si self és una fulla, False en altre cas
 """
 # Recorreguts
 def preordre(self):
 """
 retorna una llista amb els elements de self, 
 ordenats d'acord a la definició del recorregut en preordre
 """
 def postordre(self):
 """
 retorna una llista amb els elements de self, 
 ordenats d'acord a la definició del recorregut en postordre
 """
 def inordre(self):
 """
 retorna una llista amb els elements de self, 
 ordenats d'acord a la definició del recorregut en inordre
 """
 def nivells(self):
   if self.buit():
      return []
   else:
      resultat = []
      