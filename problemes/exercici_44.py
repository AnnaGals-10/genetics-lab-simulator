# Problema 3 sessions 12&13; problema 44 col·lecció
    def splice(self,x,lst):
        # Pre: lst és una instància de Llista
        if self.buida():
            self._sentinella = lst._sentinella
            self._cursor     = self._sentinella
            self._n          = lst._n
        elif not lst.buida():
            # referències importants d'lst
            primer_lst = lst._sentinella._next
            darrer_lst = lst._sentinella._prev
            # buscar x
            p = self._sentinella._next
            while p != self._sentinella and p._element != x:
                p = p._next
            # tant si he trobat x com si no, he de fer el mateix
            q = p._prev
            q._next = primer_lst
            primer_lst._prev = q
            p._prev = darrer_lst
            darrer_lst._next = p
            self._n += lst._n
        # buidem lst, NO puc fer lst = Llista()
        lst.__init__()