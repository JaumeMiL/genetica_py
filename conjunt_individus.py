from arbre_binari import *
from individu import Individu
from pytokr import pytokr

item, items = pytokr(iter = True)


class ConjuntIndividus:
    def __init__(self,num_ind):
        self._num_ind = num_ind
        self._list_ind = [None for _ in range(num_ind + 1)]
        self.individus = {}  # diccionari amb tots els individus
        self.arbre_genealogic = ArbreBinari()

    def get_parell_cromosomes(self,individu): # No sé si esto se puede hacer
        return self.ind(individu).parell_cromosomes()

    def list_ind(self):
        return self._list_ind
    
    def ind(self,individu):
        lst = self.list_ind()
        return lst[individu]
    
    def afegir_tret(self,nom_tret,persona):
        return self.ind(persona).nou_tret(nom_tret)

    def llegir_individu(self,num_gen):
        for i in range(self._num_ind):
            cromosoma = item()
            self._list_ind()[i] = Individu(cromosoma,num_gen)
    
    def consulta_individu(self, individu):
        return self.ind(individu).consulta_individu() 

    def retornar_arbre(self):
        return self.arbre_genealogic

    def llegeix_arbrebinari_int(self):
        x = int(item())
        if x != 0:
            l = self.llegeix_arbrebinari_int()
            r = self.llegeix_arbrebinari_int()
            self.arbre_genealogic = ArbreBinari(x,l,r)

    def obtenir_individu(self, id):
        return self.individus.get(id)

    def __repr__(self):
        return f"ConjuntIndividus({self.individus}, Arbre: {self.arbre_genealogic})"
