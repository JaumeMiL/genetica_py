from individu import Individu

class Experiment:
    def __init__(self,num_ind,num_gen):
        self._list_ind = [None for _ in range(num_ind + 1)]
        self._list_tret = [None for _ in range(num_ind + 1)]
        for i in range(num_ind):
            cromosoma = input()
            self._list_ind()[i] = Individu(cromosoma,num_gen)

    def list_ind(self):
        return self._list_ind
    
    def consulta_individu(self, individu):
        primer_cromosoma = self.list_ind()[individu].primer_cromosoma()
        segon_cromosoma = self.list_ind()[individu].segon_cromosoma()
        return primer_cromosoma, segon_cromosoma