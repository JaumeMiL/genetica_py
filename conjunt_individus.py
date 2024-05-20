from arbre_binari import Node
from individu import Individu

class ConjuntIndividus:
    def __init__(self):
        self.individus = {}  # diccionari amb tots els individus
        self.arbre_genealogic = None

    def inicialitzar_individus(self, preordre):
        preordre_list = list(preordre)  # Converteixo a llista els elements del preordre
        self.arbre_genealogic = self.construir_arbre(preordre_list)  # faig larbre genealògic cridant a la funció anterior

        # Inicialitzo self.individus
        for id in preordre_list:
            individu = Individu(id)
            self.individus[id] = individu

    def construir_arbre(self, preordre):
        if not preordre:
            return None
        clau_a_afegir = preordre.pop(0)
        if clau_a_afegir == 0:
            return None
        node = Node(clau_a_afegir)
        node.left = self.construir_arbre(preordre)
        node.right = self.construir_arbre(preordre)
        return node



    def obtenir_individu(self, id):
        return self.individus.get(id)

    def __repr__(self):
        return f"ConjuntIndividus({self.individus}, Arbre: {self.arbre_genealogic})"
