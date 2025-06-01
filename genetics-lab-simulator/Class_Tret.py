class Tret:
    def __init__(self, name):
        self.name = name
        self.combinacio_gens = None
        self.individus = []

    def calcular_interseccio(self, cromosomes, gene_comb):
        """
          Calcula la interseccio de dos cromosomes.

          Paràmetres:
          - cromosomes (list): Els cromosomes a ser intersecats..
          - gene_comb (list): La combinació de gens amb la que ser intersecada.

          Retorna:
          - interseccio (list): La interseccio de dos cromosomes.
        """
        interseccio = [[0]*len(cromosomes[0]), [0]*len(cromosomes[1])]
        for i in range(len(cromosomes[0])):
          if cromosomes[0][i] == gene_comb[0][i]:
            if cromosomes[1][i] == gene_comb[1][i]:
              interseccio[0][i] = cromosomes[0][i]
              interseccio[1][i] = cromosomes[1][i]
              continue
          interseccio[0][i] = "-"
          interseccio[1][i] = "-"
        return interseccio

    def calcular_combinacio(self, new_ind_cromosomes):
        """
          Calcula la cominació de gens del nou individu.

          Paràmetres:
          - new_ind_cromosomes (list): Els cromosomes del nou individu.
        """
        if self.combinacio_gens is None:
            self.combinacio_gens = new_ind_cromosomes
        else:
          self.combinacio_gens = self.calcular_interseccio(self.combinacio_gens, new_ind_cromosomes)

    def afegir_individu(self, individu):
        """
          Afegeix un individu al tret.

          Paràmetres:
          - individu (Individu): L'individu a ser afegit.
        """
        for individu_afegit in self.individus:
          if individu_afegit.id == individu.id:
            return
        self.individus.append(individu)
        self.calcular_combinacio(individu.cromosomes)
