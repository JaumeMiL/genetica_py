from cromosoma import Cromosoma
from tret import Tret

class Individu:
    def __init__(self,parell,num_gen):
        #parell es el par de genes que se se han leído antes
        #num_gen es el nº de genes
        self._cromosoma = Cromosoma(parell,num_gen)
        self.__trets = set()
    
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    
    def afegir_tret(self, tret):
        self.__trets.add(tret)

    def treure_tret(self, tret):
        self.__trets.remove(tret)

    def te_tret(self, tret):
        return tret in self.__trets
    
    def __str__(self):
        trets = ""
        for i in sorted(self.__trets):
            trets += f"\n  {i}"
        return str(self._cromosoma) + trets
