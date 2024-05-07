class Cromosoma:
    def __init__(self,parell,num_gen):
        self._primer_cromosoma = parell[:num_gen]
        self._segon_cromosoma = parell[num_gen:]
    def primer_cromosoma(self):
        return self._primer_cromosoma
    def segon_cromosoma(self):
        return self._segon_cromosoma