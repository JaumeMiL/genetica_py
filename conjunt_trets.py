from tret import Tret

class Conjunt_trets:
    def __init__(self):
        self._list_tret = {} # lo he cambiado a diccionario para poder usar el nombre del tret como referencia
    
    def list_tret(self):
            return self._list_tret

    def afegir_tret(self,nom_tret,persona): # se puede cambiar, es solo como una idea
        if self.ind(persona).existeix_tret(nom_tret): # se mira si el ind. al que se le quiere añadir lo tiene
            return '  error' # si es así se generará el error
        
        elif nom_tret in self._list_tret: # si no se tiene pero existe el tret se le añade al ind.
            self.ind(persona).nou_tret(nom_tret)

        else: # si no existe se tiene que crear
        
            instancia_tret = Tret(nom_tret, self._num_ind)
            self._list_tret[nom_tret] = instancia_tret
    
    def consulta_tret(self,tret):
        if not tret in self.list_tret():
            return '  error'
        else:
            consulta = self._list_tret[tret].consulta_tret()
            return '  ' + tret + consulta
    
    def distribucio_tret(self,tret):
        if not tret in self.list_tret():
            return '  error'