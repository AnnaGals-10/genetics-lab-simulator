from collections import deque # El BFS necessita deque
from heap import Heap # La classe que vam fer a la sessió 5!
from operator import lt 
import sys
from pytokr import pytokr
from dijkstra import inserir, surar, obtenir_min, heapify, buit


class GrafDirigitEtiquetat:
 # Feu una implementació simple (la més simple possible?) 
 # amb llistes d'adjacència. 
 # =====> Recordeu la que ja vam fer servir
 # Els vèrtexos es representen amb nombres: n vèrtexos => nombres 0...n-1
 def __init__(self, n = 0):
    self._vertexos = [None] * n # Llista de vèrtexos
    for i in range(n):
       self._vertexos[i] = [] # Inicialment les llistes d'adjacència estan buides.
 
 def afegir_aresta(self, src, dst, weight):
   assert 0 <= src,dst < self.nombre_vertexos()

   self._vertexos[src].append((weight,dst))

 def veins_vertex(self, u):
    assert 0 <= u < self.nombre_vertexos()
    veins = []
    for dst in self._vertexos[u]:
     veins.append(dst[1])
     return veins
   
 def nombre_vertexos(self):
   return len(self._vertexos)
 

 def llegir_graf_etiquetat(self):
    self.nombre_vertexos = int(f_item())   # nombre de vertexos |V|
    m = int(f_item())   # nombre d'arestes |E|
    self._vertexos = [[] for _ in range(self.nombre_vertexos)]
    for i in range(m):     # m parelles u,v: aresta u -> v
        u = int(f_item())
        v = int(f_item())
        w = int(f_item())
        self.vertexos[u].append((w,v))
    return self._vertexos
 



 def bfs_vertex(self,s): 
   assert 0 <= s < self.nombre_vertexos()
   
   visitats = [False] * self.nombre_vertexos()
   arestes = []
   q = deque();  q.append(s) 
   visitats[s] = True
   u = []
   while len(q) > 0:
       u = q.popleft()
       for vertexos, weight in self.veins_vertex(u):
           if not visitats[self.veins_vertex]:
               visitats[self.veins_vertex] = True
               q.append(self.veins_vertex)
               arestes.append(((u,self.veins_vertex), weight))             
   return arestes
 



 def dfs_vertex(self,s):
   assert 0 <= s < self.nombre_vertexos
    # Entrada: Graf G(V, E), començant al vèrtex s.
    # Sortida: La llista d'arestes, en l'ordre en que s'han recorregut.

   def dfs_vertex_aux(self,prev,v):
        visitats[v] = True
        if prev is not None:
            arestes.append((prev,v))
        for u in self._vertexos[v]:
            if not visitats[u]:
                dfs_vertex_aux(self,v,u)
                
   visitats = { u:False for u in range(len(self._vertexos)) }
   arestes  = []
   dfs_vertex_aux(self,None,s)
   return arestes
 
 fitxer = sys.argv[1]  # Hem de passar el nom del fitxer com a argument
 with open(fitxer) as f:
    f_item = pytokr(f)
    G = llegir_graf_etiquetat()

 """ 
 Retorna la llista d'arestes, en l'ordre en que s'han recorregut.
 """
 def dijkstra(self,s):
   assert 0 <= s < self.nombre_vertexos
   N = self.nombre_vertexos                  # Nombre de vertexos
   prev = [None]*N
   dist = [float('inf')]*N
   dist[s] = 0

   minheap = [(0,s)]
   minheap = heapify(minheap)
    
   while not buit(minheap):
        d,u = obtenir_min(minheap)
        if d == dist[u]:
            for p in self._vertexos[u]:
                w,v = p
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w 
                    prev[v] = u 
                    inserir(minheap,(dist[v],v))
   fitxer = sys.argv[1]  
   with open(fitxer) as f:
    f_item = pytokr(f)
    self.vertexos = self.llegir_graf_etiquetat()
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
 """
 Retorna una llista amb els costos d'anar al node des de s
 i una llista de llistes amb els camins corresponents
 """
 def cami_minim(self,u,v):
   assert 0 <= u,v < self.nombre_vertexos
   N = self.nombre_vertexos
   dist = {u:float('inf') for u in range(N)}
   dist[u] = 0
   camí = []
   q = deque();  q.append(u) 
   visitats[u] = True
   u = []
   while len(q) > 0:
       u = q.popleft()
       for vertexos, weight in self.veins_vertex(u):
           if not visitats[self.veins_vertex]:
               visitats[self.veins_vertex] = True
               q.append(self.veins_vertex)
               camí.append(((u,self.veins_vertex), weight))

   visitats = { u:False for u in range(len(self._vertexos)) }
   return camí 


 
 
 """
 Retorna el cost d'anar des de u a v, i una llista amb el camí
 """
 def bellman_ford(self,s):
   assert 0 <= s < self.nombre_vertexos
 """
 Retorna una llista amb els costos d'anar al node des de s
 i una llista de llistes amb els camins corresponents
 """
 def _calcul_camins(self,s,prev):
    pass