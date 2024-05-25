from cromosoma import Cromosoma

class Tret:
    def __init__(self, tret, num_gen):
        """
        Pre: parell_tret és una instància de la classe parell_cromosomes.
        Inicialitza el tret amb el parell de cromosomes i la llista d'individus.
        """
        self._num_gen = num_gen
        self._tret = tret
        self._list_individus = {}
        #self._individus = individus

    def lst_individus(self):
        return self._list_individus

    def afegir_individu(self, tret, individu):
        if individu in self.lst_individus():
            return False
        else:
            self.lst_individus[individu].append(individu)
            self._parell_tret.interseccio(self.__experiment.individu(individu).parell())
            return True



    def consulta_tret(self,con_ind): # Jordi no quería que hicieramos input/output desde las clases. Es decir, solo hacer prints desde el main.

        individus = sorted(self.individus)
        for a in individus:
            print(f"  {a}")
        if len(self.lst_individus()) > 1:
            keys = self.lst_individus().keys()
            primer_crom, segon_crom = self.lst_individus()[keys[0]].interseccio(self.lst_individus()[keys[1]])
            if len(self.lst_individus()) > 2:
                for i in keys[2:]:
                    crom_aux = Cromosoma(primer_crom + segon_crom, self._num_gen)
                    primer_crom, segon_crom = self.lst_individus()[i].interseccio(crom_aux)
        else:
            primer_crom, segon_crom = self.lst_individus()[self.lst_individus().keys()[0]].parell_cromosomes()

        portadors = ''
        for i in self.lst_individus().keys():
            portadors.append('\n  ' + i)
        return '  '+ self._tret + '\n  '+ primer_crom + '\n  ' + segon_crom + portadors

