import sys
from pytokr import pytokr
import networkx as nx

def llegir_graf_etiquetat():
    G = nx.DiGraph()          # Suposem que tot són grafs dirigits
    n = int(f_item())         # nombre de vertexos |V|
    G.add_nodes_from(range(n))
    m = int(f_item())         # nombre d'arestes |E|
    for i in range(m):        # m parelles u,v: aresta u -> v
        u = int(f_item())
        v = int(f_item())
        w = int(f_item())
        G.add_edge(u,v,weight=w)
    return G

fitxer = sys.argv[1]  # Hem de passar el nom del fitxer com a argument
                      # de la crida, per exemple:
                      # python3 dijkstra_nx.py exemple_dijkstra1.inp
with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf_etiquetat()

d,p = nx.single_source_bellman_ford(G,source=0)

print('--------------------')
for v in G.nodes:
    if v in d:
        print('cost',v,'=',d[v])
        print('camí',v,'=',p[v])
    else:
        print('cost',v,'= inf')
        print('camí',v,'= None')
    print('--------------------')

