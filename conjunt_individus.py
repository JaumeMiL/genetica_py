from arbre_binari import Node
from individu import Individu

class ConjuntIndividus:
    def __init__(self):
        self.individus = {}  # diccionari amb tots els individus
        self.arbre_genealogic = None

    def inicialitzar_individus(self, preordre):
        for id in preordre:
            individu = Individu(id)
            self.individus[id] = individu

        self.arbre_genealogic = self.construir_arbre(preordre)       

    def retornar_arbre(self):
        return self.arbre_genealogic

    def construir_arbre(self, preordre): #En principi l'arbre només el crearem amb els identificadors dels individus
        if not preordre:
            return None
        clau_a_afegir = preordre.pop(0)
        if clau_a_afegir == 0:
            return None
        arbre = Node(clau_a_afegir)
        arbre.left = self.construir_arbre(preordre)
        arbre.right = self.construir_arbre(preordre)
        return arbre

    def obtenir_individu(self, id):
        return self.individus.get(id)

    def __repr__(self):
        return f"ConjuntIndividus({self.individus}, Arbre: {self.arbre_genealogic})"
