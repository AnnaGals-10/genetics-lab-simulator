import sys
from pytokr import pytokr
import networkx as nx

# Lectura graf DIRIGIT amb llistes d'adjacència, i els nodes
# són nombres enters 0...N-1 (si el graf té N nodes)

def llegir_graf():
    G = nx.DiGraph()        # Suposo que tot són grafs dirigits
    n = int(f_item())       # nombre de vertexos |V|
    G.add_nodes_from(range(n))
    m = int(f_item())       # nombre d'arestes |E|
    for i in range(m):      # m parelles u,v: aresta u -> v
        u = int(f_item())
        v = int(f_item())
        G.add_edge(u,v)
    return G

fitxer = sys.argv[1]  # Hem de passar el nom del fitxer com a argument
with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf()
print(list(nx.dfs_edges(G,source=0)))
print(list(nx.bfs_edges(G,source=0)))
