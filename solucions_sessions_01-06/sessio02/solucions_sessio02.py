#############    
# Sessió 02 # 
#############    

import sys
from pytokr import pytokr
from collections import deque

# Funcions auxiliars
def llegir_graf():
    n = int(f_item())   # nombre de vertexos |V|
    m = int(f_item())   # nombre d'arestes |E|
    G = [None] * n
    for i in range(n):
        G[i] = []
    for i in range(m): # m parelles u,v: aresta u -> v
        u = int(f_item())
        v = int(f_item())
        G[u].append(v)
    return G

def crea_accio():
    ordre = 0
    def ff(x):
        nonlocal ordre
        ordre += 1
        print(ordre,'=>',x)
    return ff

# bfs

def bfs(G, accio):
    # G és un graf amb el format de llegir_graf (lab)

    def bfs_vertex(G, s, ac = (lambda x: x) ):     
        # Entrada: Graf G(V, E), començant al vèrtex s.
        # Sortida: Per a cada vèrtex u, dist[u] és
        #         la distancia de s a u (nombre d'arestes).
        
        N = len(G)
        dist = {u:float('inf') for u in range(N)}
        dist[s] = 0; visitats[s] = True
        q = deque(); q.append(s) 
        while len(q) > 0:
            u = q.popleft()
            visitats[u] = True
            ac(u)
            for v in G[u]:
                if dist[v] == float('inf'):
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist

    N = len(G)   # visitats serà un diccionari
    visitats   = {u:False for u in range(N)}  
    distancies = []
    for i in range(N):
        if not visitats[i]:
            d = bfs_vertex(G,i,accio)
            distancies.append(d)
    return distancies

# dfs

def dfs(G, accio):
    # G és un graf com els de llegir_graf
    
    def dfs_vertex(G, v, ac = (lambda x: x) ):
        visitats[v] = True
        accio(v)
        for u in G[v]:
            if not visitats[u]: 
                dfs_vertex(G, u, ac)
                
    N = len(G)
    visitats = {}          # visitats serà un diccionari
    for i in range(N):
        visitats[i] = False
    for i in range(N):
        if not visitats[i]: 
            dfs_vertex(G,i,accio)

fitxer = sys.argv[1]   # Hem de passar el nom del fitxer com a argument
                       # de la crida, p.ex: python3 dfs_bfs_nx.py exemple1.inp
with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf()

print("------------DFS:")
dfs(G,crea_accio())
print("------------BFS:")
distancies = bfs(G,crea_accio())
print(distancies)


