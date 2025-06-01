from llista import Llista

def estirar(lst):
    nova = Llista()
    lst.move_to_front()
    posicio = 1
    while not lst.is_at_end():
        valor = lst.front()
        for _ in range(posicio):
            nova.insert(valor)
        lst.move_forward()
        posicio += 1

    nova.reverse()

    # Retorna la llista com string amb format x -- x -- x
    s = ''
    nova.move_to_front()
    primer = True
    while not nova.is_at_end():
        if not primer:
            s += ' -- '
        s += str(nova.front())
        nova.move_forward()
        primer = False
    return s



# Ejemplo de uso:
if __name__ == "__main__":
    l = Llista()
    l.insert(3)
    l.insert(2)
    l.insert(1)
    print("Lista original:", l)
    estirada = estirar(l)
    print("Lista estirada:", estirada)  # Debería mostrar: 3 -- 3 -- 3 -- 2 -- 2 -- 1 --


