from cromosoma import Cromosoma

class Individu:
    def __init__(self,parell,num_gen):
        # Parell és el parell de gens que s'han llegit anteriorment
        # Num_gen és el número de gens
        self._cromosoma = Cromosoma(parell,num_gen)
        self._lst_trets = [] 
    
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    
    def parell_cromosomes(self):
        return self._cromosoma

    def llista_trets(self):
        return self._lst_trets
    
    def nou_tret(self,tret): 
        if self.existeix_tret(tret):
            return False 
        else:
            self._lst_trets.append(tret)
            return True
    
    def existeix_tret(self,tret):
        return tret in self._lst_trets
    
    def consulta_individu(self): 
        # Adaptem primer i segon perquè siguin una cadena
        primer,segon = self.cromosoma_1(),self.cromosoma_2()
        list_t = sorted(self.llista_trets())
        trets = ''
        for i in list_t:
            trets = trets + f'\n  {i}'
        return '  '+ primer + '\n  '+ segon + trets