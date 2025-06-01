class Individu:
    def __init__(self, id, cromosomes):
        self.id = id
        self.cromosomes = cromosomes
        self.progenitors = []
        self.fills = []
        self.trets = []

class Tret:
    def __init__(self, nom):
        self.nom = nom
        self.individus = []
        self.combinacio_gens = None

    def calcular_combinacio(self):
        if not self.individus:
            return None
        num_cromosomes = len(self.individus[0].cromosomes)
        longitud_cromosomes = len(self.individus[0].cromosomes[0])
        
        combinacio = [['-'] * longitud_cromosomes for _ in range(num_cromosomes)]
        
        for i in range(num_cromosomes):
            for j in range(longitud_cromosomes):
                gen_actual = self.individus[0].cromosomes[i][j]
                consistent = True
                for individu in self.individus[1:]:
                    if individu.cromosomes[i][j] != gen_actual and individu.cromosomes[i][j] != '-':
                        consistent = False
                        break
                if consistent:
                    combinacio[i][j] = gen_actual

        self.combinacio_gens = combinacio

class Experiment:
    def __init__(self):
        self.individus = {}
        self.trets = {}
        self.arrel = None

    def afegir_individu(self, id, cromosomes):
        individu = Individu(id, cromosomes)
        self.individus[id] = individu
        if not self.arrel:
            self.arrel = individu
        else:
            self._assignar_progenitor(individu)

    def _assignar_progenitor(self, individu):
        for existent in self.individus.values():
            if existent != individu:
                existent.fills.append(individu)
                individu.progenitors.append(existent)
                return

    def afegir_tret(self, id, nom_tret):
        if nom_tret not in self.trets:
            self.trets[nom_tret] = Tret(nom_tret)
        tret = self.trets[nom_tret]
        individu = self.individus[id]
        if nom_tret in individu.trets:
            print(f"Error: L'individu {id} ja té aquest tret")
            return
        individu.trets.append(nom_tret)
        tret.individus.append(individu)
        tret.calcular_combinacio()

    def consultar_tret(self, nom_tret):
        if nom_tret in self.trets:
            tret = self.trets[nom_tret]
            print(f"---CONSULTA TRET: {nom_tret}---")
            if not tret.combinacio_gens:
                print("Error: No hi ha informació sobre la combinació de gens per a aquest tret.")
                return
            print(f"Combinació que suposadament fa que es manifesti el tret '{nom_tret}':")
            for linia in tret.combinacio_gens:
                print(' '.join(map(str, linia)))
            print("Individus que manifesten aquest tret:")
            manifestants = sorted([ind.id for ind in tret.individus])
            for id in manifestants:
                print(id)
        else:
            print(f"Error: Tret '{nom_tret}' no existeix")

    def consultar_individu(self, id):
        if id in self.individus:
            individu = self.individus[id]
            print(f"Individu {id}:")
            print("Cromosomes:")
            for cromosoma in individu.cromosomes:
                print(' '.join(map(str, cromosoma)))
            print("Trets:", sorted(individu.trets))
        else:
            print(f"Error: Individu {id} no existeix")

    def distribucio_tret(self, nom_tret):
        if nom_tret in self.trets:
            tret = self.trets[nom_tret]
            resultat = []
            self._subarbre_genealogic_inordre(self.arrel, tret.individus, resultat)
            print(f"Distribució de individus amb el tret '{nom_tret}':")
            print(' '.join(map(str, resultat)))
        else:
            print(f"Error: Tret '{nom_tret}' no existeix")

    def _subarbre_genealogic_inordre(self, node, individus_tret, resultat):
        if node is None:
            return
        for fill in node.fills:
            self._subarbre_genealogic_inordre(fill, individus_tret, resultat)
        if node in individus_tret:
            resultat.append(node.id)
        else:
            resultat.append(-node.id)

# Crear nuevo experimento con 5 individuos y 8 cromosomas cada uno
exp = Experiment()


exp.afegir_individu(1, [[1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1]])
exp.afegir_individu(2, [[0,0,0,0,0,0,0,0], [1,1,1,1,1,1,1,1]])
exp.afegir_individu(3, [[0,1,0,1,0,1,0,1], [0,0,0,0,1,1,1,1]])
exp.afegir_individu(4, [[1,0,1,0,1,0,1,0], [1,0,1,0,1,0,1,0]])
exp.afegir_individu(5, [[1,1,0,0,1,1,0,0], [1,0,1,0,1,0,1,0]])

# Ejecutar comandos según el archivo de prueba
exp.consultar_individu(1)
exp.consultar_individu(2)
exp.consultar_individu(3)
exp.consultar_individu(4)
exp.consultar_individu(5)

exp.afegir_tret(3,'qwerty_12')
exp.distribucio_tret('qwerty_12')
exp.consultar_tret('qwerty_12')

exp.afegir_tret(5, 'asdf_34')
exp.distribucio_tret('asdf_34')
exp.consultar_tret('asdf_34')

exp.afegir_tret(4, 'asdf_34')
exp.distribucio_tret('asdf_34')
exp.consultar_tret('asdf_34')

exp.afegir_tret(2, 'asdf_34')
exp.distribucio_tret('asdf_34')
exp.consultar_tret('asdf_34')





