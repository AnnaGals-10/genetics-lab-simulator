from collections import deque

# L'arbre binari amb diccionaris l'hem vist *abans* de veure
# les estructures dinàmiques de dades. Per això fem servir el
# deque per al recorregut per nivells.

class ArbreBinari:

    def __init__(self,v=None,esq=None,dre=None):
        """
        Al tanto! un arbre binari buit NO és None
        Un arbre buit és un ArbreBinari amb self._root igual a None
        L'objecte creat per una crida a ArbreBinari() és un arbre buit.
        Si el valor de v és None, també ho han de ser esq i dre.
        """
        assert (v is None and esq is None and dre is None) or v is not None
        if v is None:
            self._root = None
        else:
            fesq  = esq if esq is not None else ArbreBinari()
            fdre  = dre if dre is not None else ArbreBinari()
            self._root = {"v": v, "fesq": fesq, "fdre": fdre}
            
    # Getters
    def valor_arrel(self):
        """
        Pre: Suposem que self no és buit
        retorna el valor a l'arrel de self
        """
        return self._root["v"]
    
    def fill_esq(self):
        """
        Pre: Suposem que self no és buit
        retorna un ArbreBinari que representa el fill esquerre de self
        """
        return self._root["fesq"]
    
    def fill_dre(self):
        """
        Pre: Suposem que self no és buit
        retorna un ArbreBinari que representa el fill dret de self
        """
        return self._root["fdre"]

    # Setters
    def modificar_valor_arrel(self,v):
        """
        canvia el valor a l'arrel de self. Aquest nou valor no pot ser None
        """
        assert(v is not None)
        if not self.buit():
            self._root["v"] = v
        else:
            self._root =  {"v": v, "fesq": ArbreBinari(), "fdre": ArbreBinari()}
        
    def modificar_fill_esq(self,esq):
        """
        Pre: esq és un ArbreBinari i self no és buit
        canvia el fill esquerre de self
        """
        self._root["fesq"] = esq
        
    def modificar_fill_dre(self,dre):
        """
        Pre: dre és un ArbreBinari i self no és buit
        canvia el fill dret de self
        """
        self._root["fdre"] = dre
        
    # Altres operacions
    def buit(self):
        """
        retorna True si self és buit, False en altre cas
        """
        return self._root == None
        
    def fulla(self):
        """
        retorna True si self és una fulla, False en altre cas
        """
        if self.buit():
            return False
        return self.fill_esq().buit() and self.fill_dre().buit()

    # Recorreguts 
    def preordre(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut en preordre
        """
        if self.buit():
            return []
        else:
            return [self.valor_arrel()] + self.fill_esq().preordre() + self.fill_dre().preordre()

    def postordre(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut en postordre
        """
        if self.buit():
            return []
        else:
            return self.fill_esq().postordre() + self.fill_dre().postordre() + [self.valor_arrel()]
        
    def inordre(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut en inordre
        """
        if self.buit():
            return []
        else:
            return self.fill_esq().inordre() + [self.valor_arrel()] + self.fill_dre().inordre()

    def nivells(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut per nivells
        """
        if self.buit():
            return []
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

    def __repr__(self):
        if self.buit():
            return self.__class__.__name__+"()"
        elif self.fulla():
            rt = self.valor_arrel().__repr__()
            return f"{self.__class__.__name__}({rt})"
        else:  #  Algun dels fills no és buit
            rt = self.valor_arrel().__repr__()
            if self.fill_dre().buit():  # El fill dret és buit?
                r_esq = self.fill_esq().__repr__()
                return f"{self.__class__.__name__}({rt}, esq={r_esq})"
            elif self.fill_esq().buit(): # El fill esquerre és buit?
                r_dre = self.fill_dre().__repr__()
                return f"{self.__class__.__name__}({rt}, dre={r_dre})"
            else:                         # Cap fill és buit
                r_esq = self.fill_esq().__repr__()
                r_dre = self.fill_dre().__repr__()
                return f"{self.__class__.__name__}({rt}, esq={r_esq}, dre={r_dre})"
        
