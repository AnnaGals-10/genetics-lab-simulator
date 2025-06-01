from pila import Pila
from llista import Llista
from Bintree import BinTree
from graf import GrafDirigitEtiquetat
from heap import Heap
from PilaCua import Pila, Cua
from dijkstra import llegir_graf_etiquetat
from operator import lt
from collections import deque, namedtuple
from math import gcd, atan, sqrt, atan2, cos, sin


# Donada una matriu quadrada (representada com a llista de llistes, amb una llista per cada fila), feu
# una funció que ens digui si la matriu és un quadrat màgic o no.
# Un quadrat màgic és una matriu quadrada N✕N tal que tots els nombres entre 1 i N2 estan disposats
# de manera que les seves files, les seves columnes i les seves diagonals principals sumen el mateix.
# Per exemple, [[6,1,8],[7,5,3],[2,9,4]] és un quadrat màgic.

def quadrat_magic(L):
    pass



















# 5. Feu una funció que, donada una llista, retorni True si tots els elements són diferents, i False en cas
# contrari (per simplificar suposarem que tots els elements de la llista són del mateix tipus, és a dir, o
# bé tots són nombres, o bé tots són strings, etc).
# Pista: No compareu tots amb tots. Feu servir un diccionari

def diferents(diccionari):
    visitats = {}                       # create dictionary
    for element in diccionari:
        if element in visitats:         # if element is already in dictionary, return False
            return False
        else:
            visitats[element]= True     # else, append element to dictionary, all elements in dictionary are different
    return True


# 6. Són min-heaps les següents llistes?
# a) [None,12,24,34,45,24,79]
# b) [None,13,20,44,18,35,67,98,67,69,47]
# c) [None,10,14,15,23,38,44,46,51,98]
# d) [None,69,97,29,50,42,24,61,14,95,83,98,83,79,5,66]
# e) [None,2]

def es_min_heap(heap):
    if len(heap) == 1:
        return True
    for i in range(len(heap)):
        fill_esquerre = heap[2*i+1]
        fill_dret = heap[2*i+2]
        if fill_esquerre < len(heap) and heap[fill_esquerre] < heap[i]:
            return False
        elif fill_dret < len (heap) and heap[fill_dret] < heap[i]:
            return False
    else:
        return True


# 12. Els  arbres   binaris,   tal   com   els   vam   implementar   a   la   transparència   55   de   teoria,   són  arbres
# immutables. Com que vam fer servir un diccionari per implementar-los, aquesta implementació es pot
# ampliar per poder modificar els arbres (i que aquests siguin mutables). Feu les funcions 
    
    from sessio6 import ArbreBinari
    
    def modifica_valor_arbre(a,v):
        a["v"] = v
    def modifica_fill_esq(a,fesq):
        a["fesq"] = fesq
    def modifica_fill_dre(a,fdre):
        a["fdre"] = fdre

# 13. Feu una funció que, donat un arbre, retorni una llista amb els elements de les fulles de l'arbre
# (transparència 40 de teoria).


def llista_de_fulles(a):
    if a.empty():
        return []
    if a.leaf():
        return [a.get_root()]
    fulles_esq = llista_de_fulles(a.get_left())
    fulles_dre = llista_de_fulles(a.get_right())
    return fulles_esq + fulles_dre

a = BinTree(20,
            BinTree(12,
                    BinTree(9, BinTree(7), BinTree(2)),
                    BinTree(3)),
            BinTree(8,
                    BinTree(4),
                    BinTree(4))
           )

print(llista_de_fulles(a))

# 17.Feu una funció que, donats el recorregut en preordre i el recorregut en inordre d'un arbre binari,
# construeixi l'arbre binari corresponent. Suposarem que els elements de l'arbre són tots diferents

def construeix_arbre(preordre, inordre):
    if not preordre or not inordre:
        return None
    if len(preordre) == 1:
        return preordre[0]
    arrel = preordre[0]    # el primer element del preordre és l'arrel
    inordre_arrel = inordre.index[preordre[0]]  # busquem l'arrel la inordre

    in_esq = inordre[:inordre_arrel]  # fills esquerres fins l'arrel
    in_dre = inordre[inordre_arrel+1:]  # fills drets després de l'arre

    n_esq = len(in_esq)

    pre_esq = preordre[1:n_esq]
    pre_dre = preordre[n_esq+1:]

    arbre_esq = construeix_arbre(pre_esq, in_esq)
    arbre_dre = construeix_arbre(pre_dre, in_dre)

    return BinTree(arrel, arbre_esq, arbre_dre)


# 19. Implementeu una funció que, donat un arbre binari i un nombre x, retorni el nombre d'elements de
# l'arbre que són estrictament més grans que x. Si l'arbre fos un BST (és a dir, un arbre binari que
# satisfà la propietat de BST), es podria fer una funció més eficient per resoldre el mateix problema?


def mes_grans_que_x(a, x):
    if a.empty():
        return []
    recorregut_preordre = a.preorder()
    mes_grans = []
    for elements in recorregut_preordre:
        if elements > x:
            mes_grans.append(elements)
    return mes_grans

arbre = BinTree(20,
                    BinTree(12, BinTree(5), BinTree(15)),
                    BinTree(30, None, BinTree(35))
                   )

mes_grans_que_x(arbre, 15)


# 21.El transposat d'un graf dirigit G = (V,E) és el graf dirigit GT = (V,ET) on definirem
#                               ET = {(v,vertexos) | (vertexos,v) ∈ E} 
# Feu una funció que, donat un graf dirigit G, calculi el graf GT transposat. 
# La funció ha de ser destructiva (no ha de retornar res, ha de modificar G), tot i que es permet la
# utilització d'un graf auxiliar mentre es fa el càlcul. Suposarem que el graf G està implementat amb
# llistes d'adjacència, en el format que hem fet servir a les sessions de laboratori.


def graf_transposat(graf):
    n = graf.nombre_vertexos()
    transposat = [[] for _ in range(n)]  
    for vertexos in range(n):
        for (w, v) in graf._vertexos[vertexos]:
            transposat[v].append((w, vertexos))
    graf._vertexos = transposat
    return graf

# Creem un graf de 4 vèrtexs
G = GrafDirigitEtiquetat(4)
G.afegir_aresta(0, 1, 1)
G.afegir_aresta(1, 2, 1)
G.afegir_aresta(2, 3, 1)
G.afegir_aresta(3, 0, 1)
    
print("Graf original:")
for vertexos in range(G.nombre_vertexos()):
    print(f"{vertexos}: {G._vertexos[vertexos]}")
    
graf_transposat(G)

print("\nGraf transposat:")
for vertexos in range(G.nombre_vertexos()):
    print(f"{vertexos}: {G._vertexos[vertexos]}")


# 22.El quadrat d'un graf G = (V,E) és el graf GQ = (V,EQ) on definirem
#                               EQ = { (u,v) | ∃ w ∈ V t.q. (u,w) ∈ V ∧ (w,v) ∈ V }
# Feu una funció que, donat un graf G, calculi el quadrat GQ d'un graf G. 
# La funció no ha de ser destructiva (ha de retornar el nou graf, no ha de modificar G). Suposarem que
# el graf G està implementat amb llistes d'adjacència, en el format que hem fet servir a les sessions de
# laboratori.

def graf_quadrat(graf):
    n = graf.nombre_vertexos()
    quadrat = [[] for _ in range(n)] 
    for u in range(n):
        for (w,v) in graf._vertexos[u]:
            for (w2,x) in graf._vertexos[v]:
                quadrat[u].append((1, x))
    nou_graf = GrafDirigitEtiquetat(n)
    nou_graf._vertexos = quadrat
    return nou_graf

# Creem un graf de 4 vèrtexs amb arestes:
# 0 -> 1, 1 -> 2, 2 -> 3, 3 -> 0
G = GrafDirigitEtiquetat(4)
G.afegir_aresta(0, 1, 1)
G.afegir_aresta(1, 2, 1)
G.afegir_aresta(2, 3, 1)
G.afegir_aresta(3, 0, 1)

print("Graf original:")
for u in range(G.nombre_vertexos()):
    print(f"{u}: {G._vertexos[u]}")

Q = graf_quadrat(G)

print("\nGraf quadrat:")
for u in range(Q.nombre_vertexos()):
    print(f"{u}: {Q._vertexos[u]}")

 
# 24.Modifiqueu l'algorisme de Dijkstra que hem vist a classe de manera que calculi el camí més curt des
# d'un vèrtex x a un vèrtex y donats: def dijkstra_mod(G,x,y). Hauria de retornar la distància d'x
# a y (float("inf") si no es pot anar d'x a y) i una llista amb el camí (None si no es pot anar d'x a
# y).


def dijkstra_mod(graf, x, y):
    assert 0 <= x < graf.nombre_vertexos() and 0 <= y < graf.nombre_vertexos()
    N = graf.nombre_vertexos()
    dist = [float('inf')] * N
    prev = [None] * N
    dist[x] = 0
    minheap = Heap.heapify([(0, x)], cmp=lt)
    while not minheap.buit():
        d, u = minheap.obtenir()
        if u == y: 
            break
        if d == dist[u]:
            for (w, v) in graf._vertexos[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    minheap.inserir((dist[v], v))
    if dist[y] == float('inf'):
        return float('inf'), None
    path = []
    actual = y
    while actual is not None:
        path.append(actual) 
        actual = prev[actual]
    path.reverse()
    return dist[y], path

# Exemple d'ús:
G = GrafDirigitEtiquetat(4)
G.afegir_aresta(0, 1, 1)
G.afegir_aresta(0, 2, 4)
G.afegir_aresta(1, 2, 2)
G.afegir_aresta(1, 3, 6)
G.afegir_aresta(2, 3, 3)
d, cami = dijkstra_mod(G, 0, 3)
print("Distància:", d)
print("Camí:", cami)


# 25.Modifiqueu l'algorisme de Dijkstra que hem vist a classe de manera que compti quants camins
# òptims (de mínim cost; pot haver-ne més d'un) hi ha entre dos vèrtexos x i y: def
# dijkstra_camins(G,x,y). Hauria de retornar un nombre, 0 si no n'hi ha cap. Suposarem que les
# arestes del graf tenen costos estrictament > 0 (pareu atenció, hem de respondre quants camins, és
# a dir, hem de comptar-los; NO hem de retornar els camins).

def dijkstra_camins(graf, x, y):
    assert 0 <= x < graf.nombre_vertexos() and 0 <= y < graf.nombre_vertexos()
    N = graf.nombre_vertexos()
    
    # Inicialització: distancies infinita i comptatge de camins a 0
    dist = [float('inf')] * N
    count = [0] * N
    dist[x] = 0
    count[x] = 1

    minheap = Heap.heapify([(0, x)], cmp=lt) 
    while not minheap.buit():
        d, u = minheap.obtenir()
        if d != dist[u]:
            continue
        for (w, v) in graf._vertexos[u]:
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                count[v] = count[u]
                minheap.inserir((new_dist, v))
            elif new_dist == dist[v]:
                count[v] += count[u]
    
    if dist[y] == float('inf'):
        return 0
    return count[y]

# Creem un graf de 5 vèrtexs (0..4)
G = GrafDirigitEtiquetat(5)
# Definim les arestes:
# 0 -> 1 amb pes 1, 0 -> 2 amb pes 1
# 1 -> 3 amb pes 1, 2 -> 3 amb pes 1
# 3 -> 4 amb pes 1
G.afegir_aresta(0, 1, 1)
G.afegir_aresta(0, 2, 1)
G.afegir_aresta(1, 3, 1)
G.afegir_aresta(2, 3, 1)
G.afegir_aresta(3, 4, 1)

# En aquest graf hi ha dos camins òptims des de 0 a 4:
#    0 -> 1 -> 3 -> 4  i  0 -> 2 -> 3 -> 4, amb cost total 3
num_camins = dijkstra_camins(G, 0, 4)
print("Nombre de camins òptims de 0 a 4:", num_camins)


###### Suposem que definim una classe per representar punts en un plà:


class Punt: 
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def distancia(self, p):
        """ Pre: p és instància de la classe Punt """
        dx = self.getX() - p.getX()
        dy = self.getY() - p.getY()
        return sqrt(dx*dx + dy*dy)
    
    def radi(self):
        return sqrt(self.getX()*self.getX() + self.getY()*self.getY())
    
    def angle(self):
        if (self.getX() == 0 and self.getY() == 0):
            return 0
        return atan(self.getY()/self.getX())
    
    def __add__(self, p):
        """ Pre: p és instància de la classe Punt """
        return Punt(self.getX() + p.getX(), self.getY() + p.getY())



# 26.Volem canviar la implementació de la classe Punt a una implementació que utilitzi coordenades
# polars i no coordenades cartesianes.  Identifiqueu quins mètodes cal canviar.

        # s'haurien de modificar els getters

# 27.Ara, canvieu la implementació i feu servir coordenades polars. Penseu que els mètodes de la classe
# han de tenir la mateixa semàntica, és a dir, s'han de comportar exactament igual. Per exemple, els
# mètodes getX i getY, que abans eren simples getters, ara ja no ho són. A més, recordeu que els
# punts s'han de continuar creant a partir de les coordenades cartesianes, p.ex. p = Punt(3,-1) 


class PuntPolar: 
    def __init__(self, x, y):
        self.__r = sqrt(x*x + y*y)
        self.__theta = atan2(y,x)

    def getX(self):
        return self.__r*cos(self.__theta)
    
    def getY(self):
        return self.__r*sin(self.__theta)
    
    def distancia(self, p):
        """ Pre: p és instància de la classe Punt """
        dx = self.getX() - p.getX()
        dy = self.getY() - p.getY()
        return sqrt(dx*dx + dy*dy)
    
    def radi(self):
        return self.__r
    
    def angle(self):
        return self.__theta
    
    def __add__(self, p):
        """ Pre: p és instància de la classe Punt """
        return Punt(self.getX() + p.getX(), self.getY() + p.getY())
    
    def __str__(self):
        return f"Punt amb coordenades ({self.getX()}, {self.getY()}) "

    def __repr__(self):
        return f"Punt({self.getX()},{self.getY()})"

    def __eq__(self, value):
        return self.getX() == value.getX() and self.getY() == value.getY()

p1 = PuntPolar(3, -1)
p2 = PuntPolar(3, -1)
p3 = PuntPolar(2, 5)

print("p1 =", p1)              # Crida a __str__
print("p1 repr =", repr(p1))    # Crida a __repr__
print("p1 == p2 ?", p1 == p2)    # Crida a __eq__
print("p1 == p3 ?", p1 == p3)

# 28.Què hagués passat si no haguéssim fet servir els getters a la resta de funcions? Imagineu que
# haguéssim escrit el mètode distancia així:
 #   def distancia(self, p):
  #      dx = self.__x - p.__x   # podem accedir a atributs privats d'objectes
   #     dy = self.__y - p.__y   # instància de la mateixa classe que estem definint
    #    return sqrt(dx*dx + dy*dy) """

'''Si accedíssim directament als atributs privats (per exemple, `self.__x` i `p.__x`), 
    el mètode funcionaria correctament dins de la mateixa classe, ja que Python permet 
    accedir als atributs privats d'altres instàncies de la mateixa classe. Però això fa
    que el codi estigui fortament lligat a la representació interna (en aquest cas, 
    coordenades cartesianes). Així, si més endavant canviessis la implementació per 
    utilitzar coordenades polars, el mètode `distancia` deixaria de funcionar
    correctament. En resum, fer servir getters encapsula la representació interna 
    i facilita la seva modificació sense afectar altres mètodes. '''

# 29. Afegiu a la classe Punt els mètodes __str__,  __repr__ i __eq__

'''Implementat a dalt'''


    

# 30. A la classe Racional (sessió 5 de laboratori) substituïu el mètode suma_racional pel mètode
# __add__ de manera que pugueu utilitzar l'operador +. Feu el mateix amb el mètode igual,  és a dir,
# elimineu-lo i escriviu el mètode __eq__. Així podreu fer servir l'operador ==.


class Racional:
    def __init__(self, n, d):
        """ Retorna el nombre racional n/d, suposant n i d són enters i d != 0 """
        assert d != 0
        g = gcd(n, d)
        self.__numerador = n // g
        self.__denominador = d // g
     
    # Mètodes consultors / 'getters'
    def numerador(self):
        """ Retorna el numerador del nombre racional r amb valor absolut més petit """
        return self.__numerador
         
    def denominador(self):
        """ Retorna el denominador del nombre racional r amb valor > 0 més petit """
        return self.__denominador
    
    # Operacions amb racionals
    def producte_racional(self, q):
        n = self.numerador() * q.numerador()
        d = self.denominador() * q.denominador()
        return Racional(n, d)
    
    def str_racional(self):
        n = self.numerador()
        d = self.denominador()
        return str(n) if d == 1 else f"{n}/{d}"
    
    def __add__(self, q):
        n1 = self.numerador() * q.denominador()
        n2 = q.numerador() * self.denominador()
        d = self.denominador() * q.denominador()
        return Racional(n1 + n2, d)
    
    def __eq__(self, q):
        if not isinstance(q, Racional):
            return NotImplemented
        return (self.numerador() * q.denominador() == q.numerador() * self.denominador())

		 
def nombre_harmonic_exacte(n):
	s = Racional(0,1)
	for k in range(1,n+1):
		s = s.suma_racional(Racional(1,k))
	return s.str_racional()
		
print(nombre_harmonic_exacte(15))



# 32 Aquest és un problema divertit: Afegiu __repr__ a la classe ArbreBinari. (sessió 6 de laboratori).


class BinTree:

    def __init__(self,v=None,left=None,right=None):
        """
        Warning, an empty tree is NOT None
        An empty tree is a BinTree with self.__node equal to None
        The object created by a call to BinTree() is an empty tree
        Requirement: If the value v is None, so must be the two children.
        """
        assert (v is None and left is None and right is None) or v is not None
        if v is None:
            self.__node = None
        else:
            left  = left  if left  is not None else BinTree()
            right = right if right is not None else BinTree()
            self.__node = {"v": v, "fesq": left, "fdre": right}
            
    # Getters
    def get_root(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the value at the root of the BinTree
        """
        return self.__node["v"]
    
    def get_left(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the left child of the BinTree
        """
        return self.__node["fesq"]
    
    def get_right(self):
        """
        Pre: It is assumed that the BinTree is NOT empty
        returns the right child of the BinTree
        """
        return self.__node["fdre"]

    # Setters
    def set_root(self,v):
        """
        changes the value at the root of the BinTree
        """
        assert(v is not None)
        if not self.empty():
            self.__node["v"] = v
        else:
            self.__node =  {"v": v, "fesq": BinTree(), "fdre": BinTree()}
        
    def set_left(self,left):
        """
        Pre: left is a BinTree and the BinTree is not empty
        changes the left child of the BinTree
        """
        self.__node["fesq"] = left
        
    def set_right(self,right):
        """
        Pre: right is a BinTree and the BinTree is not empty
        changes the right child of the BinTree
        """
        self.__node["fdre"] = right
        
    # Other operations
    def empty(self):
        """
        returns True if the BinTree is empty, False in other case
        """
        return self.__node == None
        
    def leaf(self):
        """
        returns True if the BinTree is a leaf, False if not.
        """
        return self.get_left().empty() and self.get_right().empty()

    # Traversals 
    def preorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the pre-order traversal.
        """
        if self.empty():
            return []
        else:
            return [self.get_root()] + self.get_left().preorder() + self.get_right().preorder()

    def postorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the post-order traversal.
        """
        if self.empty():
            return []
        else:
            return self.get_left().postorder() + self.get_right().postorder() + [self.get_root()]
        
    def inorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the in-order traversal.
        """
        if self.empty():
            return []
        else:
            return self.get_left().inorder() + [self.get_root()] + self.get_right().inorder()

    def levelorder(self):
        """
        returns a list with the elements of the BinTree, ordered 
        as is specified in the definition of the levels-order traversal.
        """
        if self.empty():
            return []
        else:
            resultat = []
            q = deque()
            q.append(self)
            while len(q) > 0:
                tt = q.popleft()
                resultat.append(tt.get_root())
                if not tt.get_left().empty():
                    q.append(tt.get_left())
                if not tt.get_right().empty():
                    q.append(tt.get_right())
            return resultat
        
    def __repr__(self):
        if self.empty():
            return "BinTree()"
        return f"BinTree({self.get_root()}, {repr(self.get_left())}, {repr(self.get_right())})"

T = BinTree(20, BinTree(10), BinTree(30))
print(repr(T))



#33. Fer una funció def palindrom(x) que determini si una seqüència x (de Python: llista, tupla o
#string) és un palíndrom o no. És a dir, cal indicar si la seqüència es llegeix igual d’esquerra a dreta
#que a l’inrevés. Utilitzeu una pila (encara que es pugui fer sense).

def palindrom(x):
    if isinstance(x, str):
        x = x.replace(" ", "")
    caracters = list(x)
    pila = []
    for i in range(len(caracters) // 2):
        pila.append(caracters[i]) #afegeix a la pila la primera meitat de caracters sense el caracter central (//=divisio entera)
    for i in range(len(caracters) // 2 + len(caracters) % 2, len(caracters)):
        if caracters[i] != pila.pop():#compara cada caracter amb l'elemento superior de la pila (que es el último elemento de la primera mitad de la secuencia)
            return False
    return True


## 35

def escriu(n):
    p = Pila()
    while n > 0:
        p.push(n)
        n-=1
    while not p.buida():
        t = p.pop()
        print(""+str(t), end = "")
        if t > 1:
            k = t-1
            while k > 0:
                p.push(k)
                k-=1
    print()

#37. Fer un programa per resoldre el següent problema: Donada una cua de parells d’enters, on el primer
#és un identificador d’usuari i el segon el temps esperat de la gestió que vol fer, dissenyeu una
#operació que reparteixi els usuaris en dues noves cues de tal manera que:
#a) Cap persona esperi més a la nova cua que una que tenia al darrera inicialment.
#b) Totes esperin el mínim temps possible.
#c) Si un usuari pot anar a les dues cues, s’escollira la primera.

#Element = namedtuple("Element", ["id", "temps_espera"])

def repartir_usuaris(q):
    q1=[]
    q2=[]
    for element in q:
        if len(q1) == 0:
            q1.append(element)
        elif element.temps_espera <= q1[-1].temps_espera:
            q1.append(element)
        else:
            q2.append(element)
    return q1, q2

'''
q = [
    Element(id=3, temps_espera=2),
    Element(id=6, temps_espera=3),
    Element(id=2, temps_espera=5),
    Element(id=11, temps_espera=1),
    Element(id=8, temps_espera=4),
    Element(id=5, temps_espera=3),
    Element(id=9, temps_espera=2),
    Element(id=1, temps_espera=3),
    Element(id=7, temps_espera=4),
    Element(id=15, temps_espera=2),
    Element(id=4, temps_espera=3)
]

q1, q2 = repartir_usuaris(q)

print("Sortida:")
for elem in q1:
    print(elem.id, elem.temps_espera)
for elem in q2:
    print(elem.id, elem.temps_espera)

'''
#38. Diem que el resultat de trenar dues cues q1 i q2 és una cua q3 on els elements de q1 apareixen a les
#posicions senars (primera, tercera, cinquena, etc) i els elements de q2 apareixen a les posicions
#parelles (segona, quarta, sisena, etc). Després de l’últim element de la cua més curta apareixen la
#resta dels elements de la cua més llarga. Volem afegir un mètode a la classe Cua per trenar una altra
#cua amb G. Òbviament aquesta operació és destructiva per a totes dues cues. Manipuleu les
#referències a instàncies de _Node directament, no feu servir setters ni getters. trenar té la següent
#especificació:

def trenar(self, c):
    """
    Operació destructiva per trenar self amb la cua c. 
    c ha d'acabar buida.
    """
    dummy = self._Node(None, None)
    actual = dummy
    p1 = self._cap
    p2 = c._cap
    count = 0
    while p1 is not None or p2 is not None:
        if count % 2 == 0:
            if p1 is not None:
                actual._next = p1
                actual = actual._next
                p1 = p1._next
        else:
            if p2 is not None:
                actual._next = p2
                actual = actual._next
                p2 = p2._next
        count += 1
    # Ajustar les referències de self
    self._cap = dummy._nex
    # Trobar la nova cua (últim node)
    if self._cap is None:
        self._cua = None
    else:
        final = self._cap
        while final._next is not None:
            final = final._next
        self._cua = final
    # Nova mida: suma de les dues cues
    self._mida = self._mida + c._mida
    # Deixar la cua c buida
    c._cap = None
    c._cua = None
    c._mida = 0

    
#39.Fer una funció def comptar(lst,n) que, donada una llista lst de parelles d'enters (al tanto, lst
#és una instància de Llista, no una llista de Python) i un número n, que compti quants cops apareix
#n com a primer element d'una parella i sumi els segons elements d'aquestes parelles (de les que n és
#el primer element). Ha de retornar aquests dos valors (el comptatge i la suma).

#from collections import namedtuple
#Element = namedtuple("Element", ["first", "second"])

def comptar(lst,n):
    comptador = 0
    suma = 0
    for element in lst:
        if element.first == n:
            comptador = comptador + 1
            suma = suma + element.second
        else:
            None
    print(f"El número {n} apareix {comptador} cops com a primer element de parelles i la suma dels segons elements d'aquestes parelles és {suma}")
'''
exemple
lst = [Element(1, 2), Element(3, 4), Element(1, 5), Element(2, 6)]
comptar(lst, 1)
'''
#40.Cal fer un programa que calculi estadístiques d’una seqüència de parell d’enters. Cada parell d’enters
#es composa de parells <codi nombre> un codi d’operació (un enter negatiu) i d’un enter (en aquest
#ordre). Si el codi és -1 això vol dir que el nombre que té com a parella compta com a vàlid. Si el codi
#és -2 llavors vol dir que cal invalidar qualsevol de les aparicions del nombre que segueix a
#continuació. (seria equivalent al fet que s’hagués esborrat una de les aparicions prèvies vàlides
#d’aquest element a la seqüència). Si el nombre s’ha d’invalidar però no té cap aparició prèvia vàlida,
#llavors no cal esborrar res. Cada vegada que processem una parella de la seqüència, cal treure per la
#sortida estàndard el mínim, al màxim i la mitjana dels elements vàlids que hi hagin al tros de
#seqüència que haurem processat. En cas que no hi hagi cap element vàlid, llavors cal escriure només
#un zero. Per exemple:
#Entrada: -1 1 -1 1 -1 3 -1 2 -1 1 -2 1 -2 2 -2 3 -2 34 0 0
#Sortida: 1 1 1
#1 1 1
#1 3 1.66667
#1 3 1.75
#1 3 1.6
#1 3 1.75
#1 3 1.66667
#1 1 1
#1 1 1
#No podeu fer servir cap contenidor dels que Python ofereix (llistes, tuples, diccionaris, etc)

class Element:
    def __init__(G, code, number):
        G.code = code
        G.number = number

class ProcessadorSequencies:
    def __init__(G):
        G.valid_numbers = []
        G.comptador = 0
        G.suma = 0
    
    def proces(G, code, number):
        if code == -1:
            G.valid_numbers.append(number)
        elif code == -2 and number in G.valid_numbers:
            G.valid_numbers.remove(number)
        
        if G.valid_numbers:
            min_number = min(G.valid_numbers)
            max_number = max(G.valid_numbers)
            avg_number = sum(G.valid_numbers) / len(G.valid_numbers)
            print(min_number, max_number, avg_number)
        else:
            print(0)

'''
EXEMPLE
processor = ProcessadorSequencies()
parelles = [(-1, 1), (-1, 1), (-1, 3), (-1, 2), (-1, 1), (-2, 1), (-2, 2), (-2, 3), (-2, 34), (0, 0)]

for parella in parelles:
    processor.proces(parella[0], parella[1])
'''

#41.Fer una funció def interseccio(lst1,lst2) que, donades dues llistes (instàncies de Llista)
#ordenades d'enters, retorni una nova llista amb la intersecció de les esmentades llistes. No x'han de
#visitar elements de forma innecessària ni fer servir estructures auxiliars.

def interseccio(lst1, lst2):
    lst=[]
    i=0
    j=0
    while len(lst1) > i and len(lst2) > j:
        if lst1[i] == lst2[j]:
            lst.append(lst1[i])
            i+=1
            j+=1  
        elif lst1[i] < lst2[j]:
            i+=1
        else:
            j+=1
    return lst

'''
EXEMPLE:
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
res = interseccio(lst1, lst2)
print(res)
'''

#42. Volem implementar dins de la classe Llista un mètode nou amb la següent especificació:
def esborrar_tots(self,x):
    """
    Operació  destructiva  on s'han  eliminat  de  self  totes  les  aparicions  d'x  (la
    resta   d'elements   queda   en   el   mateix   ordre   original);   si   el   cursor   de  self
    referenciava   a   una   aparicio   d'x,   passa   a   referenciar   al   primer   element
    diferent d'x posterior a aquesta (si no hi ha cap element diferent d'x, passa
    a la dreta el tot); en cas contrari, el cursor no canvia
    """
    actual = self._sentinella._next
    while actual != self._sentinella:
        seguent = actual._next
        if actual._element == x:
            # Desconectar el nodo actual
            actual._prev._next = actual._next
            actual._next._prev = actual._prev
            if self._cursor == actual:
                temp = seguent
                while temp != self._sentinella and temp._element == x:
                    temp = temp._next
                self._cursor = temp
            self._n -= 1
        actual = seguent
                
#43. En un problema anterior hem demanat fer un mètode de la classe Cua per trenar dues cues. Afegiu
#ara un mètode a la classe Llista per trenar dues llistes, self i la llista-paràmetre. L'operació és
#destructiva, és a dir, self és la llista trenada i la llista-paràmetre queda buida:
def trenar(self,llista):
    """
    Operació destructiva per trenar self amb la llista l. l ha d'acabar buida.
    Recordar que el resultat de trenar dues llistes l1 i l2 és una llista l3 on els elements de l1 apareixen a
    les posicions senars (primera, tercera, cinquena, etc) i els elements de l2 apareixen a les posicions
    parelles (segona, quarta, sisena, etc). Després de l’últim element de la llista més curta apareixen la
    resta dels elements de la llista més llarga   
    """
    self.move_to_front()
    llista.move_to_front()

    while not self.is_at_end() and not llista.is_at_end():
        self.insert(llista.front())
        llista.erase()
        self.move_forward()

    if self.is_at_end() and not llista.buida():
        self.move_to_end()
        while not llista.buida():
            self.insert(llista.front())
            llista.erase()

    return self


# 44

# Problema 3 sessions 12&13; problema 44 col·lecció
    def splice(self,x,lst):
        # Pre: lst és una instància de Llista
        if self.buida():
            self._sentinella = lst._sentinella
            self._cursor     = self._sentinella
            self._n          = lst._n
        elif not lst.buida():
            # referències importants d'lst
            primer_lst = lst._sentinella._next
            darrer_lst = lst._sentinella._prev
            # buscar x
            p = self._sentinella._next
            while p != self._sentinella and p._element != x:
                p = p._next
            # tant si he trobat x com si no, he de fer el mateix
            q = p._prev
            q._next = primer_lst
            primer_lst._prev = q
            p._prev = darrer_lst
            darrer_lst._next = p
            self._n += lst._n
        # buidem lst, NO puc fer lst = Llista()
        lst.__init__()
    
     



#45.Fes una funció def inverteix_prefix(lst,m) que, donada una llista de mida n i un nombre 0 ≤
#m ≤ n, retorni una nova llista igual que lst però amb els m primers elements (prefix de mida m) de
#lst invertits.
#Per exemple, si l1 = [[3,7,-2,5,0,7]] i m = 3, la crida inverteix_prefix(l1,m) ha de
#retornar la (nova) llista [[-2,7,3,5,0,7]].

def inverteix_prefix(lst,m):
    inv_lst = []
    for i in range(m-1,-1,-1):
        inv_lst.append(lst[i])
    for i in range(m,len(lst)):
        inv_lst.append(lst[i])

    return inv_lst

'''
EXEMPLE
lst = [1,2,3,4,5]
m=3
res = inverteix_prefix(lst,m)
print(res)
'''

## 45. INverteix prefix

def inverteix_prefix(self, m):
    """
    Retorna una nova llista igual que self però amb els m primers elements invertits.
    Pre: 0 ≤ m ≤ mida de la llista
    """
    assert 0 <= m <= self.__n
    nova = Llista()
    p = self.__sentinella._next

    # Inserim els m primers elements per davant (s'inverteixen)
    stack = []
    for _ in range(m):
        stack.append(p._element)
        p = p._next
    for elem in reversed(stack):
        nova.insert(elem)

    # Inserim la resta en ordre
    while p != self.__sentinella:
        nova.insert(p._element)
        nova.move_forward()  # per col·locar-se al final de la nova llista
        p = p._next

    return nova


#48. Feu una funció def reflex(a,b) que, donades dues instàncies de ArbreBinari, ens digui si són
#reflexos. Dos arbres binaris a i b són reflexos si les arrels són iguals i el fill dret d'a i el fill esquerre
#de b són reflexos, i el fill esquerre d'a i el fill dret de b són reflexos. Dos arbres binaris buits són
#reflexos.

class Node:
    def __init__(G, value=None, left=None, right=None):
        G.value = value
        G.left = left
        G.right = right

class ArbreBinari:
    def __init__(G, root=None):
        G.root = root

def reflex(a,b):
    if a is None and b is None:
        print(f"{a} i {b} són reflexos")
    elif a is None or b is None:
        print(f"{a} i {b} no són reflexos")
    elif a.value == b.value and reflex(a.left, b.right) and reflex(a.right, b.left):
        print(f"{a} i {b} són reflexos")

'''
a = Node(1, Node(2), Node(3))
b = Node(1, Node(3), Node(2))

print(reflex(a, b))
'''

#EXERCICIEXTRA: Fes una funcio on donada una llista retorni el nombre, n, de cops que surt el número m a la llista
#Que retorni també una llista com la original però suprimint el nombre m

def duplicats(lst, m):
    comptador = 0
    lst2 = lst[:]
    i=0
    while i < len(lst2):
        if lst2[i] == m:
            comptador = comptador + 1
            lst2.pop(i)
        else:
            i+=1
    return comptador, lst2

'''
EXEMPLE
lst = [1,1,2,3,4,4,4,5]
m = 4
comptador, lst2 = duplicats(lst, m)
print(comptador, lst2)
'''          
            
#EXERCICIEXTRA: Fes una funcio on donada una llista retorni una llista amb els números que apareixen més d'un cop
#a la llista i que retorni tambe una llista amb els números sense repetir

def repetits(lst):
    rep = []
    lst2 = []

    for i in range(len(lst)):
        comptador = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                comptador += 1            
    
        if comptador > 1:
            if lst[i] not in rep:
                rep.append(lst[i])
        else:
            if lst[i] not in lst2:
                lst2.append(lst[i])
    
    # Eliminar los elementos repetidos de lst2
    for num in rep:
        while num in lst2:
            lst2.remove(num)
    
    return rep, lst2

'''
lst = [1, 1, 2, 3, 4, 4, 4, 5]
rep, lst2 = repetits(lst)
print("Números que aparecen más de una vez:", rep)
print("Lista sin números repetidos:", lst2)
'''



# palindrom amb stacks

from pila import Pila


def es_palindrom(a):
    p = Pila()
    for c in a:
        p.push(c)
    for c in a:
        if c != p.pop():
            return False        
    else:
        return True
    
# a = [1, 2, 3, 2, 1]
# es_palindrom(a)



