

def main():
    comanda = input()
    while comanda != 'fi':

        if comanda == 'experiment':
            print('experiment')
            #aquí falta cosa per llegir i llavors cridarem a experiment
            experiment()

        elif comanda == 'consulta_individu':
            print('consulta_individu')
            id_ind = input()
            consulta_individu(id_ind)
        
        elif comanda == 'consulta_tret':
            print('consulta_tret')
            nom_tret = input()
            consulta_tret(nom_tret)

        elif comanda == 'distribucio_tret':
            print('distribucio_tret')
            nom_tret = input()
            distribucio_tret(nom_tret)

        elif comanda == 'afegir_tret':
            print('afegir_tret')
            nom_tret = input()
            afegir_tret(nom_tret)
        
        comanda = input()
        