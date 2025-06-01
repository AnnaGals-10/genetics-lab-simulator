
class ArbreBinari:

    def __init__(self):
        self.elements = [None]

    def surar(self, i):
        assert self.elements != [] and 1 <= i < len(self.elements)                           #CONDICIÓN
        if self.elements > 1 and self.elements[i//2] > self.elements[i]:                     #si aún hay elementos en la lista y el hijo es mayor que el padre
            self.elements[i], self.elements[i//2] = self.elements[i//2], self.elements[i]    #intercambiar hijo y padre si se cumple lo anterior
            self.surar(self.elements, i//2)                                                  #Llamada recursiva a surar con el índice del padre para continuar subiendo el nodo en el heap
    
    def enfonsar(self, i):
        assert self.elements != [] and 1 <= i < len(self.elements)                           #CONDICIÓN
        n = len(self.elements)-1                                                             #último índice
        c = 2*i                                                                              #hijo izquierdo
        if c <= n:                                                                           #si aún hay hijos que inspeccionar
            if c+1 <= n and self.elements[c+1] < self.elements[c]:                           #si hay hijo derecho y este es mas grande que el de la izquierda
                c += 1                                                                       #enfonsarem con el hijo de la derecha y no el de la izquerda
            if self.elements[i] > self.elements[c]:                                          #si el padre es mayor que el hijo (violación minheap)
                self.elements[i], self.elements[c] = self.elements[c], self.elements[i]      #intercambiamos padre e hijo
                self.enfonsar(self.elements, c)                                              #llamada recursiva para seguir enfonsando
    
    def inserir(self, x):                                                                    
        self.elements.append(x)                                                              #añade un elemento x a la lista de elementos (última posición)
        self.surar(self.elements, len(self.elements) - 1)                                    #llamada a la función surar para ir subiendo el nuevo elemento a su posición adecuada
    
    def obtenir_min(self):
        assert self.elements != []                                                           #CONDICIÓN
        primer = self.elements[1]                                                            #primer es el primer elemento de la lista
        darrer = self.elements.pop()                                                         #darrer
        if len(self.elements) > 1:
            self.elements[1] = darrer
            self.enfonsar(self.elements, 1)
        return primer
    
    

def heapify(items = []):             # No destructiva
    lst = [None] + items.copy()      # afegeixo l'element a ignorar en la posició 0
    darrer_index = len(lst)-1
    for i in range(darrer_index//2, 0, -1):
        enfonsar(lst,i)
    return lst

def heapSort(v):                  # operació destructiva
    p = heapify(v)                # cost lineal
    for i in range(len(v)):       # faig N vegades una operació de cost logN
        v[i] = obtenir_min(p)

#################
# fem-ho tot 'in-place'
#################

def heapify_in_place(items=[]):              # destructiva!
    items.insert(0,None)                     # afegim l'element a ignorar en la posició 0
    darrer_index = len(items)-1              # i procedim igual que amb el heapify queja hem vist
    for i in range(darrer_index//2, 0, -1):
        enfonsar(items,i)                    # no retornem res

        
""" 

Ara la idea és fer servir la mateixa llista per guardar-ho tot.

La llista estarà dividida en tres trossos::

- A la posició 0 el 'None' auxiliar per indicar que no fem servir la posició 0
- De la posició 1 a la K tindrem el heap (min-heap en aquests exemples)
- De la posició K+1 fins al final tindrem la llista ordenada a l'inrevés (de més gran a més petit)

Per a això, haurem de modificar una mica les funcions:

obtenir_min(lst) ==> obtenir_min_in_place(lst,k)
enfonsar(lst,i)  ==> enfonsar_in_place(lst,i,k)

En tots dos casos, el paràmetre k addicional li diu a la funció on s'acaba el heap (i comença 
la part de la llista on guardem els elements ja "ordenats").

Alguns detalls:
---------------

* Fixem-nos en

    if k > 1:
        lst[1] = darrer
        lst[k] = primer
        enfonsar_in_place(lst,1,k-1)

de la funció obtenir_min_in_place(lst,k). 

Això ens està dient que el primer element del (min-)heap, és a dir, el
més petit, el posem a la darrera posició del heap, que és k, i que
enfonsem l'element a l'índex 1 fins a la posició k-1, és a dir, li
diem que el heap s'acaba a k-1, ja que el que està a la posició k es
quedarà allà, ja ben ordenat.

* Fixem-nos en 

    v.reverse()                   # cost lineal, reverse in-place
    v.pop()                       # cost constant

a la funció heapSort_in_place(v).

Com que els elements els he anat posant a la llista en l'ordre contrari. Si N és la mida de la llista
original, tenim:

El més petit és a l'índex N-1
El següent més petit (el més petit sense comptar el primer) és a l'índex N-2
El següent més petit (el més petit sense comptar el primer i el segon) és a l'índex N-3
etc...

Al final he d'invertir la llista i eliminar el None.

Per què no fer primer v.pop(0) i després v.reverse()?? Perquè pop() té cost constant
i pop(0) té cost lineal.

"""

def heapSort_in_place(v):         # operació destructiva
    heapify_in_place(v)           # cost lineal
    mida = len(v)
    for i in range(1,len(v)):     # faig N vegades una operació de cost logN
        obtenir_min_in_place(v,mida-i)
    v.reverse()                   # cost lineal, reverse in-place
    v.pop()                       # cost constant

def obtenir_min_in_place(lst,k):  # operació destructiva
    # Pre: lst no pot ser buida
    #      1 <= k < len(lst), representa la darrera posició de la llista
    #      inclosa en el heap (lst[k+1:] no forma part del heap)
    primer = lst[1]
    darrer = lst[k]
    if k > 1:
        lst[1] = darrer
        lst[k] = primer
        enfonsar_in_place(lst,1,k-1)

def enfonsar_in_place(lst, i, k):
    # Pre: lst no és buida
    #      1 <= i < k
    #      1 <= k < len(lst), representa la darrera posició de la llista
    #      inclosa en el heap (lst[k+1:] no forma part del heap)
    n = k                                        # darrer índex
    c = 2*i                                      # fill esquerra
    if c <= n:                                   # Si hi ha fills...
        if c+1 <= n and lst[c+1] < lst[c]:       # Si hi ha fill dret i és més petit que l'esquerra...
            c += 1                               # ...enfonsarem amb el fill dret
        if lst[i] > lst[c]:                      # Si es viola el heap-order...
            lst[i],lst[c] = lst[c],lst[i]        # ...permutem pare i fill, i...
            enfonsar_in_place(lst, c, k)         # ...continuem enfonsant
