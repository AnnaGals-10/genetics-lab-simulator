from math import gcd

class Racional:
    
    def __init__(self,n,d):
        """ Retorna el nombre racional n/d, suposant n i d són enters i d != 0 """
        assert(d != 0)
        g = gcd(n, d)
        self.__numerador   = n // g
        self.__denominador = d // g
        
    # Mètodes consultors / 'getters'
        
    def numerador(self):
        """ Retorna el numerador del nombre racional r amb valor absolut més petit """
        return self.__numerador
    
    def denominador(self):
        """ Retorna el denominador del nombre racional r amb valor > 0 més petit """
        return self.__denominador

    # Operacions amb racionals

    def suma_racional(self,q):
        n1 = self.numerador() * q.denominador()
        n2 = q.numerador() * self.denominador()
        d  = self.denominador() * q.denominador()
        return Racional(n1+n2,d)
    
    def producte_racional(self,q):
        n = self.numerador() * q.numerador()
        d = self.denominador() * q.denominador()
        return Racional(n,d)
    
    def str_racional(self):
        n = self.numerador()
        d = self.denominador()
        return str(n) if d == 1 else f"{n}/{d}"
    
    def igual(self,q):
        n1 = self.numerador() * q.denominador()
        n2 = q.numerador() * self.denominador()
        return (n1 == n2)
    
def nombre_harmonic_exacte(n):
    """ Retorna 1 + 1/2 + 1/3 + ... + 1/n com a nombre racional """
    s = Racional(0,1)
    for k in range(1,n+1):
        s = s.suma_racional(Racional(1,k))
    return s.str_racional()
