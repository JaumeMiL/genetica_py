from cromosoma import Cromosoma
from tret import Tret

class Individu:
    def __init__(self,parell,num_gen):
        #parell es el par de genes que se se han leído antes
        #num_gen es el nº de genes
        self._cromosoma = Cromosoma(parell,num_gen)
    
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    

    # NO ESTIC SEGUR QUE AIXÒ HO POGUEM FER AQUÏ

    def consulta_tret(self, nom_tret):
        return self._cromosoma.consulta_tret(nom_tret)
    

    
