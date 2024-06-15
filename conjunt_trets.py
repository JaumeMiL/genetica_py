from tret import Tret
from arbre_binari import ArbreBinari
from pytokr import pytokr

item, items = pytokr(iter = True)

class Conjunt_trets:
    def __init__(self,num_ind):
        """
        Inicialitza un conjunt de trets amb 'num_ind' individus.
        """
        self._list_tret = {} 
        self._num_ind = num_ind
        self._arbre_genealogic = None
    
    def list_tret(self):
        """
        Retorna la llista de trets.
        """
        return self._list_tret

    def element_llista(self,element):
        """
        Retorna l'element corresponent a la posició 'element' de la llista de trets.
        """
        return self.list_tret()[element]

    def afegir_tret(self,nom_tret,persona,con_ind):
        """
        Afegeix un tret a l'individu 'persona'.
        """ 
        if nom_tret in self.list_tret():
            self.element_llista(nom_tret).afegir_individu(persona,con_ind)

        else: 
            instancia_tret = Tret(nom_tret, self._num_ind)
            self.list_tret()[nom_tret] = instancia_tret
            self.element_llista(nom_tret).afegir_individu(persona,con_ind)
    
    def consulta_tret(self, tret, con_ind):
        """
        Retorna la consulta del tret 'tret'.
        """
        if not tret in self.list_tret():
            return '  error'
        else:
            consulta = self._list_tret[tret].consulta_tret(con_ind)
            return consulta
    
    def llegeix_arbrebinari_int(self):
        """
        Llegeix un arbre binari d'enters.
        """
        def llegeix_arbrebinari_int_aux(marca):
            x = int(item())
            if x != marca:
                l = llegeix_arbrebinari_int_aux(marca)
                r = llegeix_arbrebinari_int_aux(marca)
                return ArbreBinari(x,l,r)
            else:
                return ArbreBinari()
        self._arbre_genealogic = llegeix_arbrebinari_int_aux(0)

    def distribucio_tret(self,tret):
        """
        Retorna la distribució del tret 'tret'.
        """
        if not tret in self.list_tret():
            return '  error'
        else:
            inordre = self._arbre_genealogic.inordre()
            distribucio = self.element_llista(tret).distribucio_tret(inordre,self._arbre_genealogic)
            return distribucio