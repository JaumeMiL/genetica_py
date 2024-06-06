import random
import string
from arbre_binari import ArbreBinari

# Definim unes variables constants
NUM_EXPERIMENTS = 3
MAX_INDIVIDUS = 30
MAX_LLARG_CROMO = 10
NUM_MAXIM_INSTRUCCIONS = 20
NOM_TRET_LLARGADA = 5

# Generarem un arbre aleatori amb n nodes amb n senar
def generar_arbre_binari(n):
    assert n % 2 == 1, "n ha de ser imparell"

    # Creem una llista i la desordenem
    valors = list(range(1, n + 1))
    random.shuffle(valors)

    def auxiliar(v):
        if len(v) == 1:
            return ArbreBinari(v[0], ArbreBinari(0), ArbreBinari(0))
        else:
            a = (len(v) - 2) // 2
            m = random.randint(0, a) * 2 + 1
            l = auxiliar(v[1:m + 1])
            r = auxiliar(v[m + 1:])
            return ArbreBinari(v[0], l, r)

    return auxiliar(valors)

# Fem una funció que ens anirà generant instruccions aleatòries
def generar_instruccions(n):
    comandes = ["consulta_individu", "distribucio_trets", "consulta_tret", "afegir_tret"]
    trets = set()
    
    for j in range(random.randint(1, NUM_MAXIM_INSTRUCCIONS)):
        comanda = random.choices(comandes, k=1)[0]

        if comanda == "consulta_individu":
            print(f"{comanda} {random.randint(1, n)}")

        elif comanda in ["afegir_tret", "distribucio_trets", "consulta_tret"]:
            ran = ''.join(random.choices(string.ascii_lowercase + string.digits, k=NOM_TRET_LLARGADA))
            if trets and random.randint(0, 1):
                ran = random.sample(sorted(trets), 1)[0]
            trets.add(ran)

            if comanda == "afegir_tret":
                print(f"{comanda} {ran} {random.randint(1, n)}")
            else:
                print(f"{comanda} {ran}")

# Anem generant els experiments i les instruccions
for i in range(NUM_EXPERIMENTS):
    n = random.randint(2, MAX_INDIVIDUS)
    if n % 2 == 0:
        n = n - 1

    m = random.randint(1, MAX_LLARG_CROMO)
    print(f"experiment {n} {m}")

    arbre = generar_arbre_binari(n)
    print(' '.join(map(str, arbre.preordre())))

    for j in range(n):
        print(''.join(random.choices(["0", "1"], k=2*m)))

    generar_instruccions(n)

print("fi")

# Per guardar-ho en un fitxer:
# python3 tests_creador.py > tests.txt