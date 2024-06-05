from experiment import Experiment
from pytokr import pytokr
from conjunt_individus import ConjuntIndividus as ci
from conjunt_trets import Conjunt_trets as ct

def main():
    comanda = item()
    while comanda != 'fi':

        if comanda == 'experiment':
            print('experiment', end = " ")
            n = int(item()) #nº de individuos
            m = int(item()) #nº de genes
            print(n,m)
            con_ind = ci(n)
            con_ind.llegir_individu(m)
            con_trets = ct(m)
            con_ind.llegeix_arbrebinari_int()
            a = con_ind.retornar_arbre()

        elif comanda == 'consulta_individu':
            print('consulta_individu', end = " ")
            id_ind = int(item()) 
            print(id_ind)
            consulta = con_ind.consulta_individu(id_ind)
            print(consulta)
        
        elif comanda == 'consulta_tret':
            print('consulta_tret', end = " ")
            nom_tret = item()
            print(nom_tret)
            consulta = con_trets.consulta_tret(nom_tret)
            print(consulta)

        elif comanda == 'distribucio_tret':
            print('distribucio_tret', end = " ")
            nom_tret = item()
            distribucio = con_trets.distribucio_tret(nom_tret)
            print(distribucio)

        elif comanda == 'afegir_tret':
            print('afegir_tret', end = " ")
            nom_tret = item()
            persona = item()
            comp_i, crom = con_trets.afegir_tret(nom_tret,persona)
            comp_t = con_ind.afegir_tret(nom_tret,persona,crom)
            if not comp_t and not comp_i:
                print('  error')
            elif (not comp_t and comp_i) or (not comp_i and comp_t):
                print('~~~~~~~~~~~~~')
        
        comanda = item()
        
item, items = pytokr(iter = True)

main()