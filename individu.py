from cromosoma import Cromosoma


class Individu:
    def __init__(self,parell,num_gen):
        #parell es el par de genes que se se han leído antes
        #num_gen es el nº de genes
        self._cromosoma = Cromosoma(parell,num_gen)
        self._lst_trets = []
        self.__trets = set()
    
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    
    def llista_trets(self):
        return self._lst_trets
    
    def nou_tret(self,tret):
        self._lst_trets.append(tret)
    
    def existeix_tret(self,tret):
        return True if tret in self._lst_trets else False
    
    def consulta_individu(self):
        primer,segon = self.cromosoma_1(),self.cromosoma_2
        trets = self.llista_trets()
        return primer,segon,trets

    # NO ESTIC SEGUR QUE AIXÒ HO POGUEM FER AQUÏ
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

    def consulta_tret(self, nom_tret):
        return self._cromosoma.consulta_tret(nom_tret)
    