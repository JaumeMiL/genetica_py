from cromosoma import Cromosoma

class Tret:
    def __init__(self, tret, num_gen):
        """
        Pre: parell_tret és una instància de la classe parell_cromosomes.
        Inicialitza el tret amb el parell de cromosomes i la llista d'individus.
        """
        self._num_gen = num_gen
        self._tret = tret
        self._list_individus = []
        self._cromosoma = None
        #self._individus = individus

    def lst_individus(self):
        return self._list_individus

    def afegir_individu(self, individu,con_ind):
        if individu in self.lst_individus():
            return False
        else:
            if self._list_individus == []:
                primer_c, segon_c = con_ind.ind(individu).cromosoma_1(), con_ind.ind(individu).cromosoma_2()
                self._cromosoma = Cromosoma(primer_c + segon_c, self._num_gen)
            else:
                primer_c, segon_c = con_ind.ind(individu).parell_cromosomes().interseccio(self._cromosoma)
                self._cromosoma = Cromosoma(primer_c + segon_c,self._num_gen)
            self.lst_individus().append(individu)
            #self._parell_tret.interseccio(self.__experiment.individu(individu).parell())
            return True

    def _camins(self,lst,arbre):
        def camins_aux(arbre,node,cami):
            if arbre.valor_arrel() == node:
                cami.append(node)
                return cami
            else:
                cami.append(arbre.valor_arrel())
                esq = camins_aux(arbre.fill_esq(),node,[]) if not arbre.fill_esq().buit() else None
                dre = camins_aux(arbre.fill_dre(),node,[]) if not arbre.fill_dre().buit() else None
                if esq != None:
                    cami += esq
                elif dre != None:
                    cami+= dre
                else:
                    cami = None
                return cami
        cami = set()
        for i in lst:
            resultat = camins_aux(arbre,int(i),[])
            for j in resultat:
                cami.add(j)
        return cami

    def distribucio_tret(self,inordre,arbre_gen):
        distribucio = ' '
        cami = self._camins(self.lst_individus(),arbre_gen)
        for i in range(len(inordre)):
            if inordre[i] in cami:
                if str(inordre[i]) in self.lst_individus():
                    distribucio += ' ' + str(inordre[i])
                else:
                    distribucio += ' ' + str(-inordre[i])
        return distribucio


    def consulta_tret(self,con_ind): # No sé si lo que estoy haciendo aquí se puede hacer.

        primer_crom, segon_crom = self._cromosoma.primer_cromosoma(),self._cromosoma.segon_cromosoma()
        portadors = ''
        for i in self.lst_individus()[::-1]:
            portadors += '\n  ' + i
        return '  '+ self._tret + '\n  '+ primer_crom + '\n  ' + segon_crom + portadors

