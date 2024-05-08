from experiment import *

class Tret:
    def __init__(self, parell_tret, individus):
        """
        Pre: parell_tret és una instància de la classe parell_cromosomes.
        Inicialitza el tret amb el parell de cromosomes i la llista d'individus.
        """
        self.parell_tret = parell_tret
        self.individus = individus


    def afegir_tret(self, tret, individu):
        self.individus.add(individu)
        self.parell_tret.interseccio(self.__experiment.individu(individu).parell())

    def treure_tret(self, tret, individu):
        self.individus.remove(individu)
        self.parell_tret.reiniciar()
        for a in self.individus:
            self.parell_tret.interseccio(self.__experiment.individu(a).parell())

    def consulta_tret(self):
        print(f"  {tret}")
        print(self.parell_tret)
        individus = sorted(self.individus)
        for a in individus:
            print(f"  {a}")

