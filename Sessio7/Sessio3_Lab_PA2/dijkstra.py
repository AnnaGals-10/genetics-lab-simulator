# Aquest fitxer és per a que el feu servir a la sessió de laboratori 3
# Hem modificat el dijkstra que ja coneixiem per a
# que proporcioni el mateix resultat que la funció del mòdul
# NetworkX single_source_dijkstra, i així pogueu comparar/verificar
# el que hem estat fent a classe.

import sys
from pytokr import pytokr

#------------------------------------------------------------------

def surar(lst, i):
    # Pre: lst no és buida
    #      1 <= i < len(lst)
    if i > 1 and lst[i // 2] > lst[i]:              # Si l'element no és l'arrel i es viola el heap-order...
        lst[i], lst[i // 2] = lst[i // 2], lst[i]   # ...permutem pare i fill, i...
        surar(lst, i // 2)                          # ...continuem surant
            
def enfonsar(lst, i):
    # Pre: lst no és buida
    #      1 <= i < len(lst)
    n = len(lst)-1                               # darrer índex
    c = 2*i                                      # fill esquerra
    if c <= n:                                   # Si hi ha fills...
        if c+1 <= n and lst[c+1] < lst[c]:       # Si hi ha fill dret i és més petit que l'esquerra...
            c += 1                               # ...enfonsarem amb el fill dret
        if lst[i] > lst[c]:                      # Si es viola el heap-order...
            lst[i],lst[c] = lst[c],lst[i]        # ...permutem pare i fill, i...
            enfonsar(lst, c)                     # ...continuem enfonsant

def inserir(lst, x):
    lst.append(x)
    surar(lst,len(lst)-1)

def obtenir_min(lst):
    # Pre: lst no pot ser buida
    primer = lst[1]
    darrer = lst.pop()
    if len(lst) > 1:
        lst[1] = darrer
        enfonsar(lst,1)
    return primer  
            
def heapify(items = []):
    lst = [None]  # element a ignorar en la posició 0
    for e in items:
        lst.append(e)
    darrer_index = len(lst)-1
    for i in range(darrer_index//2, 0, -1):
        enfonsar(lst,i)
    return lst

def buit(lst):
    return len(lst) == 1 and lst[0] == None

#------------------------------------------------------------------

# Lectura graf DIRIGIT amb llistes d'adjacència, i els nodes
# són nombres enters 0...N-1 (si el graf té N nodes)

def llegir_graf_etiquetat():
    n = int(f_item())   # nombre de vertexos |V|
    m = int(f_item())   # nombre d'arestes |E|
    G = [[] for _ in range(n)]
    for i in range(m):     # m parelles u,v,w: aresta u --w--> v
        u = int(f_item())
        v = int(f_item())
        w = int(f_item())
        G[u].append((w,v))
    return G


def dijkstra(G, s):
    # Entrada: Graf G=(V,E), en format de llegir_graf_etiquetat; vèrtex inicial s
    # Sortida: dist[u] distància de s a u, prev[u] camí mínim de s a u

    N = len(G)                  # Nombre de vertexos
    prev = [None]*N
    dist = [float('inf')]*N
    dist[s] = 0

    minheap = [(0,s)]
    minheap = heapify(minheap)
    
    while not buit(minheap):
        d,u = obtenir_min(minheap)
        if d == dist[u]:
            for p in G[u]:
                w,v = p
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w 
                    prev[v] = u 
                    inserir(minheap,(dist[v],v))

    # Ara que tenim prev, cal reconstruir els camíns mínims per a cada vèrtex
    camins = [None]*N
    for u in range(N):
        # calculo camí per al vèrtex u
        cami   = [u]
        vertex = u
        while vertex != s and vertex != None:
            vertex = prev[vertex]
            cami = [vertex] + cami 
        camins[u] = cami if vertex is not None else None
    
    return dist,camins



fitxer = sys.argv[1]  # Hem de passar el nom del fitxer com a argument
                      # de la crida, per exemple:
                      # python3 dijkstra.py exemple_dijkstra1.inp
with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf_etiquetat()

d,p = dijkstra(G,0)

print('--------------------')
for v in range(len(G)):
    print('cost',v,'=',d[v])
    print('camí',v,'=',p[v])
    print('--------------------')

