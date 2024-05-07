from cromosoma import Cromosoma

class Individu:
    def __init__(self,parell,num_gen):
        #parell es el par de genes que se se han leído antes
        #num_gen es el nº de genes
        self._cromosoma = Cromosoma(parell,num_gen)
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    
