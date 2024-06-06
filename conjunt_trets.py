from tret import Tret

class Conjunt_trets:
    def __init__(self,num_ind):
        self._list_tret = {} # lo he cambiado a diccionario para poder usar el nombre del tret como referencia
        self._num_ind = num_ind
    
    def list_tret(self):
        return self._list_tret

    def element_llista(self,element):
        return self.list_tret()[element]

    def afegir_tret(self,nom_tret,persona,con_ind): # no sé si puedo coger la intancia de cromosoma de la otra clase

        if nom_tret in self.list_tret(): # si no se tiene pero existe el tret se le añade al ind.
            self.element_llista(nom_tret).afegir_individu(persona,con_ind)

        else: # si no existe se tiene que crear
            instancia_tret = Tret(nom_tret, self._num_ind)
            self.list_tret()[nom_tret] = instancia_tret
            self.element_llista(nom_tret).afegir_individu(persona,con_ind)
    
    def consulta_tret(self, tret, con_ind):
        if not tret in self.list_tret():
            return '  error'
        else:
            consulta = self._list_tret[tret].consulta_tret(con_ind)
            return consulta
    
    def distribucio_tret(self,tret):
        if not tret in self.list_tret():
            return '  error'