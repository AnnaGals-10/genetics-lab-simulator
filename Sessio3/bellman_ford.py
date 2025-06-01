# Aquest fitxer és per a que el feu servir a la sessió de laboratori 3
# Hem implementat Bellman-Ford que hem vist a classe de teoria.

import sys
from pytokr import pytokr

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


def bellman_ford(G, s):
    # Entrada: Graf G=(V,E) dirigit, en format de llegir_graf_etiquetat; vèrtex inicial s
    # Sortida: dist[u] distància de s a u, camins[u] camí mínim de s a u

    N = len(G)
    prev = [None]*N
    dist = [float('inf')]*N
    dist[s] = 0

    for _ in range(N-1):
        for u in range(len(G)):    # iterem sobre totes les arestes, per a això necessito
            for p in G[u]:         # iterar sobre vertexos i després sobre les llistes
                w,v = p            # d'adjacència de cada vèrtex
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w 
                    prev[v] = u 
                
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
                      # python3 bellman_ford.py exemple_bellman_ford.inp
with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf_etiquetat()

d,p = bellman_ford(G,0)

print('--------------------')
for v in range(len(G)):
    print('cost',v,'=',d[v])
    print('camí',v,'=',p[v])
    print('--------------------')

