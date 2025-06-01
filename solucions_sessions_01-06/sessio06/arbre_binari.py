from collections import deque

# L'arbre binari amb diccionaris l'hem vist *abans* de veure
# les estructures dinàmiques de dades. Per això fem servir el
# deque per al recorregut per nivells.

class ArbreBinari:

    def __init__(self,v=None,esq=None,dre=None):
        """
        Al tanto! un arbre binari buit NO és None
        Un arbre buit és un ArbreBinari amb self.__node igual a None
        L'objecte creat per una crida a ArbreBinari() és un arbre buit.
        Si el valor de v és None, també ho han de ser esq i dre.
        """
        assert (v is None and esq is None and dre is None) or v is not None
        if v is None:
            self.__node = None
        else:
            fesq  = esq if esq is not None else ArbreBinari()
            fdre  = dre if dre is not None else ArbreBinari()
            self.__node = {"v": v, "fesq": fesq, "fdre": fdre}
            
    # Getters


    def arbre_maxim(self):

        def arbre_maxims_aux(t):
            if t is None:
                return None, None
            else:
                b1,m1 = arbre_maxims_aux(t._left)
                b2,m2 = arbre_maxims_aux(t._right)
                maxim = max(m1 if m1 is not None else t._element,
                            m2 if m2 is not None else t._element,
                            t._element)
                resultat = self._Node(maxim,b1,b2)
            return resultat, maxim
        
        b = ArbreBinari()
        b._root,_ = arbre_maxims_aux(self._root)
        return b
    
    
    def valor_arrel(self):
        """
        Pre: Suposem que self no és buit
        retorna el valor a l'arrel de self
        """
        return self.__node["v"]
    
    def fill_esq(self):
        """
        Pre: Suposem que self no és buit
        retorna un ArbreBinari que representa el fill esquerre de self
        """
        return self.__node["fesq"]
    
    def fill_dre(self):
        """
        Pre: Suposem que self no és buit
        retorna un ArbreBinari que representa el fill dret de self
        """
        return self.__node["fdre"]

    # Setters
    def modificar_valor_arrel(self,v):
        """
        canvia el valor a l'arrel de self. Aquest nou valor no pot ser None
        """
        assert(v is not None)
        if not self.buit():
            self.__node["v"] = v
        else:
            self.__node =  {"v": v, "fesq": ArbreBinari(), "fdre": ArbreBinari()}
        
    def modificar_fill_esq(self,esq):
        """
        Pre: esq és un ArbreBinari i self no és buit
        canvia el fill esquerre de self
        """
        self.__node["fesq"] = esq
        
    def modificar_fill_dre(self,dre):
        """
        Pre: dre és un ArbreBinari i self no és buit
        canvia el fill dret de self
        """
        self.__node["fdre"] = dre
        
    # Altres operacions
    def buit(self):
        """
        retorna True si self és buit, False en altre cas
        """
        return self.__node == None
        
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
            return 'ArbreBinari()'
        elif self.fulla():
            rt = self.valor_arrel().__repr__()
            return f"ArbreBinari({rt})"
        else:  #  Algun dels fills no és buit
            rt = self.valor_arrel().__repr__()
            if self.fill_dre().buit():  # El fill dret és buit?
                r_esq = self.fill_esq().__repr__()
                return f"ArbreBinari({rt}, esq={r_esq})"
            elif self.fill_esq().buit(): # El fill esquerre és buit?
                r_dre = self.fill_dre().__repr__()
                return f"ArbreBinari({rt}, dre={r_dre})"
            else:                         # Cap fill és buit
                r_esq = self.fill_esq().__repr__()
                r_dre = self.fill_dre().__repr__()
                return f"ArbreBinari({rt}, esq={r_esq}, dre={r_dre})"


