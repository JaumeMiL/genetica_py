class Cromosoma:
    def __init__(self,parell,num_gen):
        """
        Inicialitza un cromosoma amb el parell de cromosomes 'parell' i 'num_gen' gens.
        """
        self._primer_cromosoma = parell[:num_gen]
        self._segon_cromosoma = parell[num_gen:]

    def primer_cromosoma(self):
        """
        Retorna el primer cromosoma.
        """
        return self._primer_cromosoma
    
    def segon_cromosoma(self):
        """
        Retorna el segon cromosoma.
        """
        return self._segon_cromosoma
    
    def interseccio(self,altre):
        """
        Retorna la intersecció del cromosoma amb un altre cromosoma 'altre'. La intersecció es fa per caràcter.
        Això vol dir que si els caràcters són iguals, el caràcter de la intersecció és el mateix, si no, el caràcter de la intersecció és '-'.
        """
        primer = self.primer_cromosoma()
        segon = self.segon_cromosoma()
        primer_a = altre.primer_cromosoma()
        segon_a = altre.segon_cromosoma()
        def interseccio_aux(crom_1,crom_2,interseccio):
            for i in range(len(crom_1)):
                if crom_1[i] == crom_2[i]:
                    interseccio += crom_1[i]
                else:
                    interseccio += '-'
            return interseccio
        interseccio_1 = ''
        interseccio_2 = ''
        interseccio_1 = interseccio_aux(primer,primer_a,interseccio_1)
        interseccio_2 = interseccio_aux(segon,segon_a,interseccio_2)
        for i in range(len(interseccio_1)):
            if interseccio_1[i] == '-' or interseccio_2[i] == '-':
                interseccio_1 = interseccio_1[:i] + '-' + interseccio_1[i + 1:]
                interseccio_2 = interseccio_2[:i] + '-' + interseccio_2[i + 1:]

        return interseccio_1, interseccio_2
    
    