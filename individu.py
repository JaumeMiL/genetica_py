from cromosoma import Cromosoma

class Individu:
    def __init__(self,parell,num_gen):
        """
        Inicialitza un individu amb el parell de cromosomes 'parell' i 'num_gen' gens.
        """
        # Parell és el parell de gens que s'han llegit anteriorment
        # Num_gen és el número de gens
        self._cromosoma = Cromosoma(parell,num_gen)
        self._lst_trets = [] 
    
    def cromosoma_1(self):
        """
        Retorna el primer cromosoma.
        """
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        """
        Retorna el segon cromosoma.
        """
        return self._cromosoma.segon_cromosoma()
    
    def parell_cromosomes(self):
        """
        Retorna el parell de cromosomes.
        """
        return self._cromosoma

    def llista_trets(self):
        """
        Retorna la llista de trets.
        """
        return self._lst_trets
    
    def nou_tret(self,tret): 
        """
        Afegeix un tret a l'individu.
        """
        if self.existeix_tret(tret):
            return False 
        else:
            self._lst_trets.append(tret)
            return True
    
    def existeix_tret(self,tret):
        """
        Retorna True si el tret 'tret' existeix a l'individu, False en cas contrari.
        """
        return tret in self._lst_trets
    
    def consulta_individu(self): 
        """
        Retorna la consulta de l'individu.
        """
        # Adaptem primer i segon perquè siguin una cadena
        primer,segon = self.cromosoma_1(),self.cromosoma_2()
        list_t = sorted(self.llista_trets())
        trets = ''
        for i in list_t:
            trets = trets + f'\n  {i}'
        return '  '+ primer + '\n  '+ segon + trets