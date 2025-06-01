import sys
from collections import deque

# pytokr.py ha de definir "pytokr(f)" que retorna una funció f_item()
from pytokr import pytokr

# dijkstra.py ha de definir inserir, surar, obtenir_min, heapify, buit
from dijkstra import inserir, surar, obtenir_min, heapify, buit

class GrafDirigitEtiquetat:
    def __init__(self, n=0):
        """
        Crea un graf dirigit (possiblement etiquetat) amb n vèrtexs (0..n-1).
        self._vertexos[u] serà una llista de tuples (pes, v),
        indicant aresta u->v amb pes 'pes'.
        """
        self._vertexos = [[] for _ in range(n)]

    def nombre_vertexos(self):
        """Retorna el nombre de vèrtexs del graf."""
        return len(self._vertexos)

    def afegir_aresta(self, src, dst, weight=1):
        """
        Afegeix una aresta src -> dst de pes 'weight' (per defecte 1 si no s'especifica).
        """
        assert 0 <= src < self.nombre_vertexos()
        assert 0 <= dst < self.nombre_vertexos()
        self._vertexos[src].append((weight, dst))

    def llegir_graf_etiquetat(self, f_item):
        """
        Llegeix el format:
           n m
           u1 v1 w1
           u2 v2 w2
           ...
        i omple self._vertexos amb aquestes arestes.
        Si el fitxer fos 'no etiquetat' (sense w), 
        hauries de modificar aquesta part perquè no esperi w,
        o bé posar un pes per defecte.
        """
        n = int(f_item())   # nombre de vèrtexs
        m = int(f_item())   # nombre d'arestes
        self._vertexos = [[] for _ in range(n)]
        for _ in range(m):
            u = int(f_item())
            v = int(f_item())
            w = int(f_item())  # Si no tens pes al fitxer, això fallarà. En tal cas, posa w=1 per defecte
            self.afegir_aresta(u, v, w)

    def bfs_vertex(self, s):
        """
        Fa un BFS des del vèrtex s i retorna **la llista d'arestes**
        en l'ordre en què es descobreixen.
        PER SIMPLICITAT, IGNORAREM el pes a la sortida i 
        només retornarem (u, v).
        
        Si vols mantenir el pes, pots fer edges.append(((u, v), w)).
        """
        assert 0 <= s < self.nombre_vertexos()

        visitats = [False]*self.nombre_vertexos()
        edges    = []
        cua = deque()

        visitats[s] = True
        cua.append(s)

        while cua:
            u = cua.popleft()
            for (w, nxt) in self._vertexos[u]:
                if not visitats[nxt]:
                    visitats[nxt] = True
                    cua.append(nxt)
                    # Aresta descoberta u->nxt
                    edges.append((u, nxt))
        return edges

    def dfs_vertex(self, s):
        """
        Fa un DFS des del vèrtex s i retorna la llista d'arestes
        en l'ordre en què es descobreixen.
        Igual que a BFS, ignorem el pes i només retornem (u, v).
        """
        assert 0 <= s < self.nombre_vertexos()
        visitats = [False]*self.nombre_vertexos()
        edges    = []

        def dfs(u):
            visitats[u] = True
            for (w, nxt) in self._vertexos[u]:
                if not visitats[nxt]:
                    edges.append((u, nxt))  # descobreixes aresta u->nxt
                    dfs(nxt)

        dfs(s)
        return edges

    def dijkstra(self, s):
        """
        Calcula la distància mínima (en termes de pes) des de s a tots els altres
        vèrtexs, i retorna:
          - dist: llista on dist[u] és la dist mínima s->u
          - camins: llista de llistes representant camins mínims
        """
        assert 0 <= s < self.nombre_vertexos()
        N = self.nombre_vertexos()

        dist = [float('inf')] * N
        prev = [None] * N
        dist[s] = 0

        arr = [(0, s)]
        arr = heapify(arr)  # convertim la llista en un heap

        while not buit(arr):
            d, u = obtenir_min(arr)
            if d == dist[u]:
                for (w, v) in self._vertexos[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        prev[v] = u
                        inserir(arr, (dist[v], v))

        camins = self._calcul_camins(s, prev)
        return dist, camins

    def _calcul_camins(self, s, prev):
        """ Reconstrueix els camins mínims a partir de la llista prev. """
        N = self.nombre_vertexos()
        camins = [None]*N
        for u in range(N):
            if u == s:
                camins[u] = [s]
                continue
            if prev[u] is None:
                camins[u] = None
            else:
                path = []
                curr = u
                while curr is not None:
                    path.append(curr)
                    curr = prev[curr]
                path.reverse()
                if path[0] == s:
                    camins[u] = path
                else:
                    camins[u] = None
        return camins

    def cami_minim(self, u, v):
        """
        Retorna un camí no ponderat (BFS) de u fins a v, com a llista de vèrtexs, 
        si existeix. 
        """
        assert 0 <= u < self.nombre_vertexos()
        assert 0 <= v < self.nombre_vertexos()

        visitats = [False]*self.nombre_vertexos()
        pare     = [None]*self.nombre_vertexos()

        cua = deque()
        visitats[u] = True
        cua.append(u)

        while cua:
            act = cua.popleft()
            if act == v:
                break
            for (w, nxt) in self._vertexos[act]:
                if not visitats[nxt]:
                    visitats[nxt] = True
                    pare[nxt] = act
                    cua.append(nxt)

        if not visitats[v]:
            return None
        else:
            cami = []
            node = v
            while node is not None:
                cami.append(node)
                node = pare[node]
            cami.reverse()
            return cami

    def bellman_ford(self, s):
        """ (No implementat) """
        pass

# -------------------------------------------------------------------
# CODI PRINCIPAL
# -------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: cal especificar el nom del fitxer amb el graf.")
        sys.exit(1)

    fitxer = sys.argv[1]
    with open(fitxer) as f:
        f_item = pytokr(f)  # Lector de tokens
        G = GrafDirigitEtiquetat()
        # Llegim n, m i arestes. Si és no etiquetat, fes que la línia w = 1 per defecte:
        # (això requeriria modificar 'llegir_graf_etiquetat')
        G.llegir_graf_etiquetat(f_item)

    # Exemple: BFS des de 0 (només té sentit si 0 està dins l'interval de vèrtexs)
    arestes_bfs = G.bfs_vertex(0)
    print("Arestes BFS (ignorant pes):", arestes_bfs)


