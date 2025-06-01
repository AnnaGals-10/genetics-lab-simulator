from cua import Cua

class ArbreBinari:

    #------------------- classe _Node interna --------------------------
    class _Node:
        __slots__ = '_element', '_left', '_right'   # streamline memory usage

        def __init__(self, element, left = None, right = None):
            self._element = element
            self._left    = left
            self._right   = right

        
    #----------------------------------------- ------------------------

    # Al tant amb la distinció entre l'arbre buit (que no és None) i el node buit, que sí que ho és
    
    def __init__(self,v=None,esq=None,dre=None):
        """
        Al tanto! un arbre binari buit NO és None
        Un arbre buit és un ArbreBinari amb self.__node igual a None
        L'objecte creat per una crida a ArbreBinari() és un arbre buit.
        Si el valor de v és None, també ho han de ser esq i dre.
        """
        assert (v is None and esq is None and dre is None) or v is not None
        if v is None:
            self._root = None   # Arbre buit
        else:
            l = esq._root if (esq is not None) else None    # <== ATENCIÓ!!!
            r = dre._root if (dre is not None) else None    # <== ATENCIÓ!!!
            self._root = self._Node(v, l, r)
            
    # Getters
    def valor_arrel(self):
        """
        Pre: Suposem que self no és buit
        retorna el valor a l'arrel de self
        """
        assert(not self.buit())
        return self._root._element
    
    def fill_esq(self):
        """
        Pre: Suposem que self no és buit
        retorna un ArbreBinari (o instància de subclasse)
        que representa el fill esquerre de self
        """
        assert(not self.buit())
        lft = self.__class__()
        lft._root = self._root._left
        return lft
    
    def fill_dre(self):
        """
        Pre: Suposem que self no és buit
        retorna un ArbreBinari (o instància de subclasse)
        que representa el fill dret de self
        """
        assert(not self.buit())
        rft = self.__class__()
        rft._root   = self._root._right
        return rft

    # Setters
    def modificar_valor_arrel(self,v):
        """
        canvia el valor a l'arrel de self. Aquest nou valor no pot ser None
        """
        assert(v is not None)
        if not self.buit():
            self._root._element = v
        else:
            self._root = self._Node(v)
        
    def modificar_fill_esq(self,esq):
        """
        Pre: esq és un ArbreBinari i self no és buit
        canvia el fill esquerre de self
        """
        assert(not self.buit())
        self._root._left = esq._root
        
    def modificar_fill_dre(self,dre):
        """
        Pre: dre és un ArbreBinari i self no és buit
        canvia el fill dret de self
        """
        assert(not self.buit())
        self._root._right = dre._root
        
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
        return self._root._left is None and self._root._right is None

    def __eq__(self,b):
        # Pre: b és un ArbreBinari
        def eq_aux(a,b):
            if a is None:
                return b is None
            elif b is None:
                return False
            else:
                if a._element != b._element:
                    return False
                else:
                    return eq_aux(a._left,b._left) and eq_aux(a._right, b._right)
        return eq_aux(self._root,b._root)

    def __str__(self):   # Escriure l'arbre com a string, amb 0 com a marca
        if not self.buit():
            x = self.valor_arrel()
            return ' ' + str(x) + str(self.fill_esq()) + str(self.fill_dre())
        else:
            return ' 0'
    
    # Recorreguts 
    def preordre(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut en preordre
        """
        def _preordre(t):
            if t is None:
                return []
            else:
                return [t._element] + _preordre(t._left) + _preordre(t._right)

        if self.buit():
            return []
        else:
            return _preordre(self._root)        

    def postordre(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut en postordre
        """
        def _postordre(t):
            if t is None:
                return []
            else:
                return _postordre(t._left) + _postordre(t._right) + [t._element] 

        if self.buit():
            return []
        else:
            return _postordre(self._root)
        
    def inordre(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut en inordre
        """
        def _inordre(t):
            if t is None:
                return []
            else:
                return _inordre(t._left) + [t._element] + _inordre(t._right)

        if self.buit():
            return []
        else:
            return _inordre(self._root)

    def nivells(self):
        """
        retorna una llista amb els elements de self, ordenats d'acord a la definició 
        del recorregut per nivells
        """
        if self.buit():
            return []
        else:
            resultat = []
            q = Cua()
            q.encuar(self._root)
            while not q.buida():
                tt = q.desencuar()
                resultat.append(tt._element)
                if tt._left is not None:
                    q.encuar(tt._left)
                if tt._right is not None:
                    q.encuar(tt._right)
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
