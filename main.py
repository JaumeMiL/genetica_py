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
            con_trets = ct(m)
            con_trets.llegeix_arbrebinari_int()
            con_ind.llegir_individu(m)


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
            consulta = con_trets.consulta_tret(nom_tret, con_ind)
            print(consulta)

        elif comanda == 'distribucio_tret':
            print('distribucio_tret', end = " ")
            nom_tret = item()
            print(nom_tret)
            distribucio = con_trets.distribucio_tret(nom_tret)
            print(distribucio)

        elif comanda == 'afegir_tret':
            print('afegir_tret', end = " ")
            nom_tret = item()
            persona = item()
            comp_t = con_ind.afegir_tret(nom_tret,persona)
            comp_i = con_trets.afegir_tret(nom_tret,persona,con_ind)
            print(nom_tret, persona)
            if not comp_t and not comp_i:
                print('  error')
        
        comanda = item()
    print('fi')
item, items = pytokr(iter = True)

main()