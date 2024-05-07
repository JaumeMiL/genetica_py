from experiment import Experiment
from individu import Individu

def main():
    comanda = input()
    while comanda != 'fi':

        if comanda == 'experiment':
            print('experiment', end = " ")
            #aquí falta cosa per llegir i llavors cridarem a experiment
            n = input() #nº de individuos
            m = input() #nº de genes
            print(n,m)
            experiment = Experiment(n,m)
                    

        elif comanda == 'consulta_individu':
            print('consulta_individu', end = " ")
            id_ind = input()
            print(id_ind)
            primer,segon = experiment.consulta_individu(id_ind)
            print("  " + primer)
            print("  " + segon)
        
        elif comanda == 'consulta_tret':
            print('consulta_tret', end = " ")
            nom_tret = input()
            consulta_tret(nom_tret)

        elif comanda == 'distribucio_tret':
            print('distribucio_tret', end = " ")
            nom_tret = input()
            distribucio_tret(nom_tret)

        elif comanda == 'afegir_tret':
            print('afegir_tret', end = " ")
            nom_tret = input()
            afegir_tret(nom_tret)
        
        comanda = input()

#Prova