# Exercici 21
def transposat(G):
    T = {u: [] for u in G}
    for u, adj in G.items():
        for v in adj:
            T[v].append(u)
    G.clear()
    G.update(T)


# Exercici 22
def quadrat(G):
    G2 = {u: set() for u in G}
    for u, neighbors in G.items():
        for w in neighbors:
            for v in G.get(w, []):
                G2[u].add(v)
    return {u: list(neighbors) for u, neighbors in G2.items()}






# Exercicis 26, 27, 28 i 29

import math

class Punt:
    def __init__(self, x, y):
        "S'accepten coordenades cartesianes, però internament es converteixen a coordenades polars."
        self._r = math.sqrt(x**2 + y**2)
        self._theta = math.atan2(y, x)  

    def getX(self):
        return self._r * math.cos(self._theta)

    def getY(self):
        return self._r * math.sin(self._theta)

    def radi(self):
        "Retorna el radi"
        return self._r

    def angle(self):
        "Retorna l'angle" 
        return self._theta

    def distancia(self, p):
        dx = self.getX() - p.getX()
        dy = self.getY() - p.getY()
        return math.sqrt(dx*dx + dy*dy)

    def __add__(self, p):
        return Punt(self.getX() + p.getX(), self.getY() + p.getY())

    # Afegim els mètodes  __str__, __repr__ i __eq__
    def __str__(self):
        return f"Punt(x={self.getX():.2f}, y={self.getY():.2f})"

    def __repr__(self):
        return f"Punt({self.getX():.2f}, {self.getY():.2f})"

    def __eq__(self, other):
        if isinstance(other, Punt):
            return (math.isclose(self.getX(), other.getX(), rel_tol=1e-9) and 
                    math.isclose(self.getY(), other.getY(), rel_tol=1e-9))
        return False

