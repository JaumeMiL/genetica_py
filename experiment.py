from individu import Individu
from tret import Tret

class Experiment:
    def __init__(self,num_ind,num_gen):
        self._list_ind = [None for _ in range(num_ind + 1)]
        self._list_tret = {} # lo he cambiado a diccionario para poder usar el nombre del tret como referencia
        for i in range(num_ind):
            cromosoma = input()
            self._list_ind()[i] = Individu(cromosoma,num_gen)

    def list_ind(self):
        return self._list_ind
    
    def ind(self,individu):
        lst = self.list_ind()
        return lst[individu]
    
    def consulta_individu(self, individu):
        primer_cromosoma, segon_cromosoma, trets = self.ind(individu).consulta_individu()
        return primer_cromosoma, segon_cromosoma, trets
    
    def consulta_tret(self,tret):
        pass

    def afegir_tret(self,nom_tret): # se puede cambiar, es solo como una idea
        persona = input()
        if self.ind(persona).existeix_tret(nom_tret): # se mira si el ind. al que se le quiere añadir lo tiene
            return 'error' # si es así se generará el error
        
        elif nom_tret in self._list_tret: # si no se tiene pero existe el tret se le añade al ind.
            self.ind(persona).nou_tret(nom_tret)

        else: # si no existe se tiene que crear
        
            instancia_tret = Tret(nom_tret)
            self._list_tret[str(nom_tret)] = instancia_tret
