class Individu:
    def __init__(self, id, cromosomes):
        self.id = id
        self.cromosomes = cromosomes
        self.trets = []

    def afegir_tret(self, tret):
        """
          Afegeix un tret a l'individu.

          Paràmetres:
          - tret (str): El nom del tret a ser afegit.
        """
        if tret in self.trets:
          print(f"Error: Lindividu {self.id} ja té el tret {tret}.")
          return
        else:
          self.trets.append(tret)