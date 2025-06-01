# Aquest fitxer és per a que el feu servir a la sessió de laboratori 3
# Hem modificat el bfs_vertex i el dfs_vertex que ja coneixiem per a
# que proporcionin el mateix resultat que les funcions del mòdul
# NetworkX dfs_edges i bfs_edges, i així pogueu comparar/verificar
# el que hem estat fent a classe.

import sys
from pytokr import pytokr
from collections import deque

def llegir_graf():
    n = int(f_item())   # nombre de vertexos |V|
    m = int(f_item())   # nombre d'arestes |E|
    G = [[] for _ in range(n)]
    for i in range(m):     # m parelles u,v: aresta u -> v
        u = int(f_item())
        v = int(f_item())
        G[u].append(v)
    return G

def bfs_vertex(G, s):     
    # Entrada: Graf G(V, E), començant al vèrtex s.
    # Sortida: 
    
    #La llista d'arestes, en l'ordre en que s'han recorregut.
    N = len(G)
    dist = {u:float('inf') for u in range(N)}
    dist[s] = 0
    arestes = []
    q = deque();  q.append(s) 
    while len(q) > 0:
        u = q.popleft()
        for v in G[u]:
            if dist[v] == float('inf'):
                dist[v] = dist[u] + 1
                arestes.append((u,v))
                q.append(v)
    return arestes

def dfs_vertex(G,s):
    # Entrada: Graf G(V, E), començant al vèrtex s.
    # Sortida: La llista d'arestes, en l'ordre en que s'han recorregut.

    def dfs_vertex_aux(G,prev,v):
        visitats[v] = True
        if prev is not None:
            arestes.append((prev,v))
        for u in G[v]:
            if not visitats[u]:
                dfs_vertex_aux(G,v,u)
                
    visitats = { u:False for u in range(len(G)) }
    arestes  = []
    dfs_vertex_aux(G,None,s)
    return arestes


fitxer = sys.argv[1]  # Hem de passar el nom del fitxer com a argument
with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf()

arestes_dfs = dfs_vertex(G,0)
print(arestes_dfs)
arestes_bfs = bfs_vertex(G,0)
print(arestes_bfs)

