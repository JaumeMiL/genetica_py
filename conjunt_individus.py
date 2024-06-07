from arbre_binari import ArbreBinari
from individu import Individu
from pytokr import pytokr

item, items = pytokr(iter = True)


class ConjuntIndividus:
    def __init__(self,num_ind):
        self._num_ind = num_ind
        self._list_ind = [None for _ in range(num_ind + 1)]
        self._individus = {}  # diccionari amb tots els individus
        self._arbre_genealogic = None

    def list_ind(self):
        return self._list_ind
    
    def ind(self,individu):
        lst = self.list_ind()
        return lst[int(individu)]
    
    def afegir_tret(self,nom_tret,persona):
        return self.ind(persona).nou_tret(nom_tret)

    def llegir_individu(self, num_gen):
        for i in range(1, self._num_ind + 1):
            cromosoma = item()
            self._list_ind[i] = Individu(cromosoma, num_gen)
    
    def consulta_individu(self, individu):
        return self.ind(individu).consulta_individu() 

    def retornar_arbre(self):
        return self._arbre_genealogic


    def obtenir_individu(self, id):
        return self._individus.get(id)

    def __repr__(self):
        return f"ConjuntIndividus({self._individus}, Arbre: {self._arbre_genealogic})"
