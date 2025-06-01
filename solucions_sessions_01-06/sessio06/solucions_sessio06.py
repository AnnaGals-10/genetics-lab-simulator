#############    
# Sessió 06 # 
#############

from arbre_binari import ArbreBinari

def inversio(t):
    """
    Pre: t és un ArbreBinari
    """
    if t.buit():
        return ArbreBinari()
    else:
        il = inversio(t.fill_esq())
        ir = inversio(t.fill_dre())
        return ArbreBinari(t.valor_arrel(),ir,il)

# Prova

def crea_arbre_exemple():
    g = ArbreBinari('G')
    h = ArbreBinari('H')
    i = ArbreBinari('I')
    j = ArbreBinari('J')
    k = ArbreBinari('K')
    d = ArbreBinari('D',esq=g,dre=h)
    e = ArbreBinari('E',dre=i)
    f = ArbreBinari('F',esq=j,dre=k)
    b = ArbreBinari('B',esq=d,dre=e)
    c = ArbreBinari('C',esq=f)
    arbre = ArbreBinari('A',esq=b,dre=c)
    return arbre

