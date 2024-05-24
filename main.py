from experiment import Experiment
from individu import Individu
from pytokr import pytokr
from conjunt_individus import ConjuntIndividus as ci

def main():
    comanda = item()
    while comanda != 'fi':

        if comanda == 'experiment':
            print('experiment', end = " ")
            n = item() #nº de individuos
            m = item() #nº de genes
            print(n,m)
            llista_preordre = []
            for i in range(2*n+1):
                llista_preordre.append(item())
            ci.inicialitzar_individus(llista_preordre)
            a = ci.retornar_arbre()
            experiment = Experiment(n, m, a)

        elif comanda == 'consulta_individu':
            print('consulta_individu', end = " ")
            id_ind = item()
            print(id_ind)
            consulta = experiment.consulta_individu(id_ind)
            print(consulta)
        
        elif comanda == 'consulta_tret':
            print('consulta_tret', end = " ")
            nom_tret = item()
            print(nom_tret)
            consulta = experiment.consulta_tret(nom_tret)
            print(consulta)

        elif comanda == 'distribucio_tret':
            print('distribucio_tret', end = " ")
            nom_tret = item()
            distribucio = experiment.distribucio_tret(nom_tret)
            print(distribucio)

        elif comanda == 'afegir_tret':
            print('afegir_tret', end = " ")
            nom_tret = item()
            persona = item()
            experiment.afegir_tret(nom_tret,persona)
        
        comanda = item()
        
item, items = pytokr(iter = True)