import sys
from pytokr import pytokr
from heapq import heappush, heappop, heapify
import math

def llegir_graf_etiquetat(f_item):
    n = int(f_item())
    m = int(f_item())
    G = [[] for _ in range(n)]
    for _ in range(m):
        u = int(f_item())
        v = int(f_item())
        w = int(f_item())
        G[u].append((w,v))
    return G

def dijkstra_mod(G, x, y):
    N = len(G)
    dist = [math.inf]*N
    prev = [None]*N
    dist[x] = 0
    h = [(0,x)]
    heapify(h)
    while h:
        d_u, u = heappop(h)
        if d_u > dist[u]:
            continue
        if u == y:
            break
        for w,v in G[u]:
            alt = dist[u]+w
            if alt<dist[v]:
                dist[v]=alt
                prev[v]=u
                heappush(h,(alt,v))
    if dist[y]==math.inf:
        return (math.inf,None)
    path=[]
    cur=y
    while cur is not None:
        path.append(cur)
        if cur==x:
            break
        cur=prev[cur]
    path.reverse()
    return (dist[y],path)

def dijkstra_camins(G, x, y):
    N=len(G)
    dist=[math.inf]*N
    count=[0]*N
    dist[x]=0
    count[x]=1
    h=[(0,x)]
    heapify(h)
    while h:
        d_u,u=heappop(h)
        if d_u>dist[u]:
            continue
        if u==y:
            break
        for w,v in G[u]:
            alt=dist[u]+w
            if alt<dist[v]:
                dist[v]=alt
                count[v]=count[u]
                heappush(h,(alt,v))
            elif math.isclose(alt,dist[v]):
                count[v]+=count[u]
    if dist[y]==math.inf:
        return 0
    return count[y]

fitxer=sys.argv[1]
with open(fitxer) as f:
    f_item=pytokr(f)
    G=llegir_graf_etiquetat(f_item)
    x=int(f_item())
    y=int(f_item())
dist,cam=dijkstra_mod(G,x,y)
print(dist)
print(cam)
print(dijkstra_camins(G,x,y))
