class Cromosoma:
    def __init__(self,parell,num_gen):
        self._primer_cromosoma = parell[:num_gen]
        self._segon_cromosoma = parell[num_gen:]

    def primer_cromosoma(self):
        return self._primer_cromosoma
    def segon_cromosoma(self):
        return self._segon_cromosoma
    
    def bin_primer_cromosoma(self):
        prim = "0b" + self.primer_cromosoma()
        return prim
    def bin_segon_cromosoma(self):
        segon = "0b" + self.segon_cromosoma()
        return segon
    
    def interseccio(self,altre):
        primer = self.primer_cromosoma()
        segon = self.segon_cromosoma()
        primer_a = altre.primer_cromosoma()
        segon_a = altre.segon_cromosoma()
        interseccio_1 = ''
        interseccio_2 = ''
        for i in range(len(primer)):
            if primer[i] == primer_a[i]:
                interseccio_1.append(primer[i])
            else:
                interseccio_1.append('-')

        for i in range(len(segon)):
            if segon[i] == segon_a[i]:
                interseccio_2.append(segon[i])
            else:
                interseccio_2.append('-')

        return interseccio_1, interseccio_2