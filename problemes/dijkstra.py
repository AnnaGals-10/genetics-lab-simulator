# dijkstra.py

import sys
from pytokr import pytokr

# ------------- Funcions de heap -------------
def surar(lst, i):
    if i > 1 and lst[i // 2] > lst[i]:
        lst[i], lst[i // 2] = lst[i // 2], lst[i]
        surar(lst, i // 2)

def enfonsar(lst, i):
    n = len(lst) - 1
    c = 2 * i
    if c <= n:
        if c+1 <= n and lst[c+1] < lst[c]:
            c += 1
        if lst[i] > lst[c]:
            lst[i], lst[c] = lst[c], lst[i]
            enfonsar(lst, c)

def inserir(lst, x):
    lst.append(x)
    surar(lst, len(lst) - 1)

def obtenir_min(lst):
    primer = lst[1]
    darrer = lst.pop()
    if len(lst) > 1:
        lst[1] = darrer
        enfonsar(lst, 1)
    return primer  

def heapify(items=[]):
    lst = [None]
    for e in items:
        lst.append(e)
    darrer_index = len(lst) - 1
    for i in range(darrer_index // 2, 0, -1):
        enfonsar(lst, i)
    return lst

def buit(lst):
    return len(lst) == 1 and lst[0] == None

# ---------------- Lectura de graf i Dijkstra -----------------

def llegir_graf_etiquetat():
    """
    Llegeix d'un flux de tokens (f_item) un graf dirigit etiquetat
    amb format:
      n m
      u1 v1 w1
      u2 v2 w2
      ...
    Retorna una llista G de longitud n, on G[u] = [(w1,v1), (w2,v2), ...].
    *Atenció*: Perquè funcioni, f_item ha d'estar definit en l'àmbit global
    o has de passar-lo com a paràmetre d'alguna manera.
    """
    n = int(f_item())   # nombre de vertexos |V|
    m = int(f_item())   # nombre d'arestes |E|
    G = [[] for _ in range(n)]
    for i in range(m):
        u = int(f_item())
        v = int(f_item())
        w = int(f_item())
        G[u].append((w, v))
    return G

def dijkstra(G, s):
    """
    Calcula distàncies mínimes i camins des de s fins a tots els nodes del graf G,
    on G[u] = [(w,v), ...] (aresta u->v de pes w).
    Retorna dist, prev, i també reconstrueix els camins en forma de llista 'p'.
    """
    N = len(G)
    prev = [None]*N
    dist = [float('inf')]*N
    dist[s] = 0

    minheap = [(0, s)]
    minheap = heapify(minheap)
    
    while not buit(minheap):
        d,u = obtenir_min(minheap)
        if d == dist[u]:
            for p in G[u]:
                w,v = p
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    inserir(minheap, (dist[v], v))

    # Reconstrucció de camins
    camins = [None]*N
    for u2 in range(N):
        c = [u2]
        ver = u2
        while ver != s and ver is not None:
            ver = prev[ver]
            c = [ver] + c
        camins[u2] = c if ver is not None else None
    
    return dist, camins

# ------------------------- DEMO (main) -------------------------
if __name__ == "__main__":
    # Si executem directament: python dijkstra.py fitxer.in
    if len(sys.argv) < 2:
        print("Error: cal passar el nom del fitxer com a argument")
        sys.exit(1)

    fitxer = sys.argv[1]
    with open(fitxer) as f:
        f_item = pytokr(f)  # definim la funció 'f_item' pel fitxer
        G = llegir_graf_etiquetat()  # llegim el graf

    dist, p = dijkstra(G, 0)

    print('--------------------')
    for v in range(len(G)):
        print('cost',v,'=',dist[v])
        print('camí',v,'=',p[v])
        print('--------------------')
