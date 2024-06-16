from arbre_binari import ArbreBinari
from individu import Individu
from pytokr import pytokr

item, items = pytokr(iter = True)


class ConjuntIndividus:
    def __init__(self,num_ind):
        """
        Inicialitza un conjunt de trets amb 'num_ind' individus.
        """
        self._num_ind = num_ind
        self._lst_ind = [None for _ in range(num_ind + 1)]
        self._individus = {}  

    def _list_ind(self):
        """
        Retorna la llista d'individus.
        """
        return self._lst_ind
    
    def ind(self,individu):
        """
        Retorna l'individu corresponent a la posició 'individu' de la llista d'individus.
        """
        lst = self._list_ind()
        return lst[int(individu)]
    
    def afegir_tret(self,nom_tret,persona):
        """
        Afegeix un tret a l'individu 'persona'.
        """
        return self.ind(persona).nou_tret(nom_tret)

    def llegir_individu(self, num_gen):
        """
        Llegeix un individu amb 'num_gen' gens.
        """
        for i in range(1, self._num_ind + 1):
            cromosoma = item()
            self._lst_ind[i] = Individu(cromosoma, num_gen)
    
    def consulta_individu(self, individu):
        """
        Retorna la consulta de l'individu corresponent a la posició 'individu' de la llista d'individus.
        """
        return self.ind(individu).consulta_individu() 

    def obtenir_individu(self, id):
        """
        Retorna l'individu corresponent a l'identificador 'id'.
        """
        return self._individus.get(id)

    def __repr__(self):
        """
        Retorna una representació.
        """
        return f"ConjuntIndividus({self._individus})"
