from cromosoma import Cromosoma


class Individu:
    def __init__(self,parell,num_gen):
        #parell es el par de genes que se se han leído antes
        #num_gen es el nº de genes
        self._cromosoma = Cromosoma(parell,num_gen)

        self._lst_trets = [] #1

        self.__trets = set() #2
    
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    
    def llista_trets(self): # 1
        return self._lst_trets
    
    def nou_tret(self,tret): # 1
        self._lst_trets.append(tret)
    
    def existeix_tret(self,tret): # 1
        return True if tret in self._lst_trets else False
    
    def consulta_individu(self): # 1
        primer,segon = self.cromosoma_1(),self.cromosoma_2
        trets = self.llista_trets()
        return primer,segon,trets

    def afegir_tret(self, tret): # 2
        self.__trets.add(tret)

    def treure_tret(self, tret): # diría que no es necesario
        self.__trets.remove(tret)

    def te_tret(self, tret): # 2
        return tret in self.__trets
    
    def __str__(self): # 2
        trets = ""
        for i in sorted(self.__trets):
            trets += f"\n  {i}"
        return str(self._cromosoma) + trets

    # NO ESTIC SEGUR QUE AIXÒ HO POGUEM FER AQUÏ
    def consulta_tret(self, nom_tret):
        return self._cromosoma.consulta_tret(nom_tret)
    