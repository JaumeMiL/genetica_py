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

    def _lst_individus(self):
        """
        Retorna la llista dels individus que presenten el tret.
        """
        return self._list_individus

    def afegir_individu(self, individu,con_ind):
        """
        Afegeix el nou individu a la llista i modifica la instància de Cromosoma.
        """
        if individu in self._lst_individus():
            return False
        else:
            if self._list_individus == []:
                primer_c, segon_c = con_ind.ind(individu).parell_cromosomes().primer_cromosoma(), con_ind.ind(individu).parell_cromosomes().segon_cromosoma()
            else:
                primer_c, segon_c = con_ind.ind(individu).parell_cromosomes().interseccio(self._cromosoma)
                
            self._cromosoma = Cromosoma(primer_c + segon_c,self._num_gen)
            self._lst_individus().append(individu)
            return True

    def _camins(self,lst,arbre):
        """
        Troba tots els camins de l'arrel de l'arbre als elements de lst.
        """
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
        """
        Retorna la distribució del tret en forma de l'inorde de l'arbre principal.
        """
        distribucio = ' '
        cami = self._camins(self._lst_individus(),arbre_gen)
        for i in range(len(inordre)):
            if inordre[i] in cami:
                if str(inordre[i]) in self._lst_individus():
                    distribucio += ' ' + str(inordre[i])
                else:
                    distribucio += ' ' + str(-inordre[i])
        return distribucio


    def consulta_tret(self):
        """
        Retorna una string que representa la informació desitjada sobre el tret.
        """
        primer_crom, segon_crom = self._cromosoma.primer_cromosoma(),self._cromosoma.segon_cromosoma()
        portadors = ''
        for i in sorted(self._lst_individus()[::-1]):
            portadors += '\n  ' + i
        return '  '+ self._tret + '\n  '+ primer_crom + '\n  ' + segon_crom + portadors

