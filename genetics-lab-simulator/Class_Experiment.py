from Class_Individu import Individu
from Class_Tret import Tret

class Experiment:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.individus = {}
        self.trets = {}
        self.arbre_genealogic = {}

    def afegir_individu(self, id, cromosomes):
      """
        Afegeix un individu a l'experiment

        Paràmetres:
        - id (int): L'identificador de l'individu.
        - cromosomes (list): Els cromosomes de l'individu.
      """
      if id in self.individus:
        while True:
          print("\nAquest identificador no està disponible, esculli entre les dues opcions:")
          print("\n1: No fer cap canvi")
          print(f"2: Sobreescriure els cromosomes de l'individu amb identificador {id}")
          opcio = input("\nIntrodueixi la seva opció (1 o 2): ")

          if opcio == '1':
            print("No s'ha fet cap canvi.")
            return
          elif opcio == '2':
            self.individus[id].cromosomes = cromosomes
            print(f"\nS'han sobreescrit els cromosomes de l'individu amb identificador {id}.")
            return
          else:
              print("Opció invàlida, si us plau introdueixi 1 o 2.")              
      else:
        self.individus[id] = Individu(id, cromosomes)
        print(f"S'ha afegit l'individu {id} a l'experiment")
      
    def afegir_filiació(self, fill, pare1_id, pare2_id):
      """
        Afegeix una filiació a l'experiment.

        Paràmetres:
        - fill (int): L'identificador del fill
        - pare1_id (int): L'identificador del primer parent.
        - pare2_id (int): L'identificador del segon parent.
      """
      self.arbre_genealogic[fill] = (pare1_id, pare2_id)

    def afegir_tret(self, id, nom_tret):
        """
          Afegeix un tret a l'experiment

          Paràmetres:
          - id (int): l'identificador de l'individu.
          - nom_tret (str): El nom del tret.
        """
        if nom_tret not in self.trets:
          self.trets[nom_tret] = Tret(nom_tret)
        if id not in self.individus:
          print(f"L'individu {id} no existeix")
          return
        else:
          individu = self.individus[id]
          individu.afegir_tret(nom_tret)
          self.trets[nom_tret].afegir_individu(individu)
          print(f"\nA l'individu {id} se li ha afegit el tret {nom_tret}")

    def consulta_individu(self, id):
        """
          Consulta un individu de l'experiment

          Paràmetres:
          - id (int): L'identificador de l'individu.
        """
        print(f"\n---CONSULTA INDIVIDU: {id}---")
        if id not in self.individus:
          print(f"Error: L'individu {id} no existeix.")
          return
        else:
          individu = self.individus[id]
          print(f'Cromosomes: ')
          for cromosoma in individu.cromosomes:
                print(' '.join(map(str, cromosoma)))
          print(f'Trets: {individu.trets}')

    def consulta_tret(self, nom_tret):
        """
          Consulta un tret de l'experiment.

          Paràmetres
          - nom_tret (str): El nom del tret.
        """
        print("")
        print(f"---CONSULTA TRET: {nom_tret}---")
        if nom_tret not in self.trets:
          print(f"Error: El tret {nom_tret} no existeix.")
          return
        else:
          tret = self.trets[nom_tret]
          print(f'Combinació de gens que fa que es manifesti el tret :')
          for linia in tret.combinacio_gens:
                print(' '.join(map(str, linia)))
          print(f'Individus amb aquest tret: ')
          for individu in tret.individus:
            print(individu.id)
        
    def distribucio_tret(self, nom_tret):
      """
        Calcula la distribució de trets a l'arbre genealògic.

        Paràmetres:
        - nom_tret (str): El nom del tret.
      """
      if nom_tret not in self.trets:
        print(f'\n---PORTADORS TRET {nom_tret}:---\n')
        print(f"Error: El tret {nom_tret} no existeix.")
        return
      else:
        tret = self.trets[nom_tret]
        id_portadors = []
        for t_individual in tret.individus:
          id_portadors.append(t_individual.id)   
        print(f'\n---PORTADORS TRET {nom_tret}: {id_portadors}---\n')

        for t_ind in id_portadors:
          print(f'Subarbre del portador amb identificador {t_ind}:')
          pare_esquerre = self.arbre_genealogic[t_ind][0]
          pare_dret = self.arbre_genealogic[t_ind][1]
          if pare_esquerre is not None:
            if pare_esquerre not in id_portadors:
              pare_esquerre = "-" + str(pare_esquerre)
          if pare_dret is not None:
            if pare_dret not in id_portadors:
              pare_dret = "-" + str(pare_dret)

          print([pare_esquerre, t_ind, pare_dret])
          print(f'{pare_esquerre}   {pare_dret}')
          if self.arbre_genealogic[t_ind][0] is not None:
            print(" \ /")
            print(f'  {t_ind}  ')
          else:
            print(" \    /")
            print(f'   {t_ind}    ')

    def finalitzar_experiment(self):
        """
          Finalitza l'experiment i mostra un resum final.

        """
        print("\n--- RESUM FINAL DE L'EXPERIMENT ---\n")

        print("--- INDIVIDUS ---")
        for id, individu in self.individus.items():
            print(f"\nID: {id}, Cromosomes:")
            for cromosoma in individu.cromosomes:
              print(' '.join(map(str, cromosoma)))
            print(f"Trets: {individu.trets}")
        
        print("--- TRETS ---")
        for nom_tret, tret in self.trets.items():
            print(f"\nTret: {nom_tret}, Combinació de gens:")
            for linia in tret.combinacio_gens:
                print(' '.join(map(str, linia)))
            print("Individus amb aquest tret: ", [individu.id for individu in tret.individus])
        
        print("\n--- ARBRE GENEALÒGIC ---")
        for fill, (pare1_id, pare2_id) in self.arbre_genealogic.items():
            print(f"Fill: {fill}, Pare 1: {pare1_id}, Pare 2: {pare2_id}")
        
        print("\nL'experiment ha finalitzat.\n")
    

print("_______________________")
print("EXPERIMENT1")
print("_______________________")
print("")

n1 = 3
m1 = 8

exp1 = Experiment(n1, m1)
exp1.afegir_individu(1, [[1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]])
exp1.afegir_individu(2, [[0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1]])
exp1.afegir_individu(3, [[0,1,0,1,0,1,0,1], [0,0,0,0,1,1,1,1]])
exp1.afegir_individu(4, [[1,0,1,0,1,0,1,0], [1,0,1,0,1,0,1,0]])
exp1.afegir_individu(5, [[1,1,0,0,1,1,0,0], [1,0,1,0,1,0,1,0]])

exp1.afegir_filiació(1, 2, 3)
exp1.afegir_filiació(2, None, None)
exp1.afegir_filiació(3, 4, 5)
exp1.afegir_filiació(4, None, None)
exp1.afegir_filiació(5, None, None)

exp1.consulta_individu(1)
exp1.consulta_individu(2)
exp1.consulta_individu(3)
exp1.consulta_individu(4)
exp1.consulta_individu(5)

exp1.afegir_tret(1,'qwerty_12')
exp1.afegir_tret(1,'qwerty_12') #repeteció tret a un individu
exp1.afegir_tret(2,'qwerty_12')
exp1.consulta_tret('qwerty_12')
exp1.distribucio_tret('qwerty_12')

exp1.afegir_tret(4,'asdf_34')
exp1.afegir_tret(5,'asdf_34')
exp1.consulta_tret('asdf_34')
exp1.distribucio_tret('asdf_34')

exp1.afegir_tret(1,'asdf_34')

exp1.consulta_individu(1)
exp1.consulta_tret('asdf_34')
exp1.distribucio_tret('asdf_34')
exp1.finalitzar_experiment()


print("_______________________")
print("EXPERIMENT2")
print("_______________________")
print("")

n2 = 3
m2 = 3

exp2 = Experiment(n2, m2)
exp2.afegir_individu(1, [[1,1,1], [0,1,1]])
exp2.afegir_individu(2, [[1,1,1], [0,0,0]])
exp2.afegir_individu(3, [[1,1,0], [1,1,1]])

exp2.consulta_individu(1)
exp2.consulta_individu(2)
exp2.consulta_individu(3)

exp2.afegir_individu(3, [[1,1,1], [1,1,1]])  #repetició id 
exp2.consulta_individu(3)

exp2.afegir_filiació(1, 2, 3)
exp2.afegir_filiació(2, None, None)

exp2.consulta_tret('qwert1')
exp2.afegir_tret(1, 'qwert1')
exp2.consulta_tret('qwert1')

exp2.afegir_tret(2, 'qwert1')
exp2.consulta_tret('qwert1')

exp2.distribucio_tret('qwert1')
exp2.finalitzar_experiment()


print("_______________________")
print("EXPERIMENT3")
print("_______________________")
print("")

n3 = 3
m3 = 3

exp3 = Experiment(n3, m3)
exp3.afegir_individu(1, [[1,1,1], [1,1,1]])
exp3.afegir_individu(2, [[1,1,1], [1,1,1]])
exp3.afegir_individu(3, [[1,1,1], [1,1,1]])

exp3.consulta_individu(1)
exp3.consulta_individu(2)
exp3.consulta_individu(3)

exp3.afegir_filiació(1, 2, 3)
exp3.afegir_filiació(2, None, None)

exp3.afegir_tret(1, 'qwert1')
exp3.consulta_individu(1)
exp3.consulta_tret('qwert1')
exp3.consulta_tret('asdf')  # tret no existent
exp3.distribucio_tret('qwert1')
exp3.distribucio_tret('asdf') #tret no existent a l'experiment
exp3.finalitzar_experiment()