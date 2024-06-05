from cromosoma import Cromosoma


class Individu:
    def __init__(self,parell,num_gen):
        #parell es el par de genes que se se han leído antes
        #num_gen es el nº de genes
        self._cromosoma = Cromosoma(parell,num_gen)

        self._lst_trets = [] #1

        self.__trets = set() #2
    
    def cromosoma_1(self):
        return self._cromosoma.primer_cromosoma()
    
    def cromosoma_2(self):
        return self._cromosoma.segon_cromosoma()
    
    def parell_cromosomes(self):
        return self._cromosoma

    def llista_trets(self): # 1
        return self._lst_trets
    
    def nou_tret(self,tret): # 1
        if self.existeix_tret(tret): # se mira si el ind. al que se le quiere añadir lo tiene
            return False # si es así se generará el error
        else:
            self._lst_trets.append(tret)
            return True
    
    def existeix_tret(self,tret): # 1
        return tret in self._lst_trets
    
    def consulta_individu(self): # 1
        # Adaptem primer i segon perquè siguin una cadena
        primer,segon = self.cromosoma_1(),self.cromosoma_2()
        list_t = self.llista_trets()
        trets = ''
        for i in list_t:
            trets = trets + f'\n  {i}'
        return '  '+ primer + '\n  '+ segon + trets

    def afegir_tret(self, tret): # 2
        self.__trets.add(tret)

    def te_tret(self, tret): # 2
        return tret in self.__trets
    
    def __str__(self): # 2
        trets = ""
        for i in sorted(self.__trets):
            trets += f"\n  {i}"
        return str(self._cromosoma) + trets

    # NO ESTIC SEGUR QUE AIXÒ HO POGUEM FER AQUÏ
    def consulta_tret(self, nom_tret):
        return self._cromosoma.consulta_tret(nom_tret)
    