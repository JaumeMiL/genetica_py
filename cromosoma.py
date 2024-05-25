class Cromosoma:
    def __init__(self,parell,num_gen):
        self._primer_cromosoma = parell[:num_gen]
        self._segon_cromosoma = parell[num_gen:]

    def primer_cromosoma(self):
        return self._primer_cromosoma
    def segon_cromosoma(self):
        return self._segon_cromosoma
    
    def interseccio(self,altre):
        primer = self.primer_cromosoma()
        segon = self.segon_cromosoma()
        primer_a = altre.primer_cromosoma()
        segon_a = altre.segon_cromosoma()
        def interseccio_aux(crom_1,crom_2,interseccio):
            for i in range(len(crom_1)):
                if crom_1[i] == crom_2[i]:
                    interseccio.append(crom_1[i])
                else:
                    interseccio.append('-')
            return interseccio
        interseccio_1 = ''
        interseccio_2 = ''
        interseccio_1 = interseccio_aux(primer,primer_a,interseccio_1)
        interseccio_2 = interseccio_aux(segon,segon_a,interseccio_2)

        return interseccio_1, interseccio_2
    
    