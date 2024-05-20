from experiment import *

class Tret:
    def __init__(self, parell_tret, individus):
        """
        Pre: parell_tret és una instància de la classe parell_cromosomes.
        Inicialitza el tret amb el parell de cromosomes i la llista d'individus.
        """
        self._parell_tret = parell_tret
        self._individus = individus


    def afegir_tret(self, tret, individu):
        self._individus.add(individu)
        self._parell_tret.interseccio(self.__experiment.individu(individu).parell())



    def consulta_tret(self,tret): # Jordi no quería que hicieramos input/output desde las clases. Es decir, solo hacer prints desde el main.
        print(f"  {tret}")
        print(self.parell_tret)
        individus = sorted(self.individus)
        for a in individus:
            print(f"  {a}")

