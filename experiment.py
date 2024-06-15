from individu import Individu
from tret import Tret
from pytokr import pytokr

item, items = pytokr(iter = True)

class Experiment:
    def __init__(self, num_ind, num_gen, arbre):
        """
        Inicialitza un experiment amb 'num_ind' individus i 'num_gen' gens.
        """
        self._num_ind = num_ind
        self._list_ind = [None for _ in range(num_ind + 1)]
        self._list_tret = {} 
        self._arbre_genealogic = arbre
        for i in range(num_ind):
            cromosoma = item()
            self._list_ind()[i] = Individu(cromosoma,num_gen)

    def list_ind(self):
        """
        Retorna la llista d'individus.
        """
        return self._list_ind
    
    def ind(self,individu):
        """
        Retorna l'individu corresponent a la posició 'individu' de la llista d'individus.
        """
        lst = self.list_ind()
        return lst[individu]
    
    def list_tret(self):
        """
        Retorna la llista de trets.
        """
        return self._list_tret
    
    def consulta_individu(self, individu):
        """
        Retorna la consulta de l'individu corresponent a la posició 'individu' de la llista d'individus.
        """
        consulta = self.ind(individu).consulta_individu()
        return consulta
    
    def consulta_tret(self,tret):
        """
        Retorna la consulta del tret 'tret'.
        """
        if not tret in self.list_tret():
            return '  error'
        else:
            consulta = self._list_tret[tret].consulta_tret()
            return '  ' + tret + consulta

    def afegir_tret(self,nom_tret,persona): 
        """
        Afegeix un tret a l'individu 'persona'.
        """
        if self.ind(persona).existeix_tret(nom_tret): # Si trobem el tret a l'individu --> error
            return '  error' 
        
        elif nom_tret in self._list_tret: # Si ja existeix el tret però l'individu no el té --> afegir tret a l'individu
            self.ind(persona).nou_tret(nom_tret)

        else: # Si no existeix el tret --> el creem i l'afegim a l'individu
        
            instancia_tret = Tret(nom_tret, self._num_ind)
            self._list_tret[nom_tret] = instancia_tret
    
    def distribucio_tret(self,tret):
        """
        Retorna la distribució del tret 'tret'.
        """
        if not tret in self.list_tret():
            return '  error'



